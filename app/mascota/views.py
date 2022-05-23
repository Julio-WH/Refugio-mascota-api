import copy
import json

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from rest_framework.parsers import JSONParser
from rest_framework.request import Request

from app.API.view.view_apiview import ListMascotas, DetalleMascota, MascotaPersonaList
from app.API.view.view_decorador import list_mascotas, detail_mascota, mascota_persona_list
from app.API.view.view_generic import MascotaListGeneric, MascotaDetailsGeneric, MascotaPersonaListGeneric
from app.API.view.view_set import MascotaViewset
from app.mascota.forms import MascotaForm, MascotaApiForm
from app.mascota.models import Mascota
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

# Rest Framework
from rest_framework import status


# -----------funciones-------------------
def index_mascota(request):
    return render(request, 'mascota/index.html')


def mascota_view(request):  # agregar
    if request.method == 'POST':
        form = MascotaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mascota:mascota_lista')
    else:
        form = MascotaForm()

    return render(request, 'mascota/mascota_form.html', {'form': form})


def mascota_list(request):
    mascota = Mascota.objects.all()
    datos = {'mascotas': mascota, 'func': 'f'}
    return render(request, 'mascota/mascota_list.html', datos)


def mascota_edit(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'GET':
        form = MascotaForm(instance=mascota)
    else:
        form = MascotaForm(request.POST, request.FILES, instance=mascota)
        if form.is_valid():
            form.save()
            return redirect('mascota:mascota_lista')
    return render(request, 'mascota/mascota_form.html', {'form': form})


def mascota_delete(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'POST':
        mascota.delete()
        return redirect('mascota:mascota_lista')
    return render(request, 'mascota/mascota_delete.html', {'mascota': mascota})


# ----------------class-----------------------------------------------
class MascotaList(ListView):
    model = Mascota
    template_name = 'mascota/mascota_list.html'


class MascotaCreate(CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascota_form.html'
    success_url = reverse_lazy('mascota:mascota_class_lista')


class MascotaUpdate(UpdateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascota_form.html'
    success_url = reverse_lazy('mascota:mascota_class_lista')


class MascotaDelete(DeleteView):
    model = Mascota
    template_name = 'mascota/mascota_delete.html'
    success_url = reverse_lazy('mascota:mascota_class_lista')


"-----------------------API------------------------"

def add_errors_form(form, response):
    for field in response:
        for error in response.get(field):
            form.add_error(field, error)
    return form


def format_mascota(mascota):
    mascota = json.loads(json.dumps(mascota))
    return mascota


def api_list(request, tipo_api):
    tipo = ""
    if tipo_api == "Decorador":
        tipo = "Decorador"
        mascota_instance = list_mascotas(request)
        pass
    elif tipo_api == "ApiView":
        tipo = "ApiView"
        mascota_instance = ListMascotas.as_view()(request)
        # mascota_instance = instance.get(request)
    elif tipo_api == "Genericview":
        tipo = "Genericview"
        mascota_instance = MascotaListGeneric.as_view()(request)

    elif tipo_api == "ViewSet":
        tipo = "ViewSet"
        mascota_instance = MascotaViewset.as_view({'get': 'list'})(request)
        # mascota_instance = instance.list(request)
    mascota_list = mascota_instance.data
    datos = {'mascotas': mascota_list, 'tipo': tipo}
    return render(request, 'mascota/api_mascota_list.html', datos)


def api_edit(request, tipo_api, id_mascota):
    if request.method == "POST":
        form = MascotaApiForm(request.POST)
        request.data = request.POST
        if form.is_valid():
            """
            Hay que espeficarle el resquest.method ya que la API tiene varios protocolos HTTP y no acepta el POST para
            realizar esta peticion
            """
            request.method = "PUT"

            if tipo_api == "ApiView":
                instance = DetalleMascota()
                # Forma 1 para hacer una peticion haciendo una instancia
                mascota_instance = instance.put(request=request, pk=id_mascota)

            if tipo_api == "ViewSet":
                instance = MascotaViewset()
                mascota_instance = instance.update(request=request, pk=id_mascota)

            elif tipo_api == "Genericview":
                # Forma 2 para hacer una peticion accediendo direntamente al la funcion
                mascota_instance = MascotaDetailsGeneric.as_view()(request=request, pk=id_mascota)

            elif tipo_api == "Decorador":
                mascota_instance = detail_mascota(request=request, pk=id_mascota)

            if mascota_instance.status_code == status.HTTP_200_OK:
                messages.success(request, "Se Edito Correctamente la Mascota")
                return HttpResponseRedirect((reverse('mascota:api_list', args=[tipo_api])))
            else:
                # En caso de errores provenientes del endpoint los agregamos manualmente al formulario
                serializers_errors = mascota_instance.data.serializer.errors
                for error in serializers_errors:
                    if error == 'non_field_errors':
                        form.add_error('__all__', serializers_errors.get(error)[0])
                    else:
                        form.add_error(error, serializers_errors.get(error)[0])
    else:
        if tipo_api == "ApiView":
            instance = DetalleMascota()
            mascota_instance = instance.get(request=request, pk=id_mascota)


        elif tipo_api == "ViewSet":
            # Forma 2 para hacer una peticion accediendo direntamente al la funcion
            mascota_instance = MascotaViewset.as_view({'get': 'retrieve'})(request=request, pk=id_mascota)
            # instance = MascotaViewset()
            # mascota_instance = instance.retrieve(request=request, pk=id_mascota)

        elif tipo_api == "Genericview":
            # Forma 2 para hacer una peticion accediendo direntamente al la funcion
            mascota_instance = MascotaDetailsGeneric.as_view()(request=request, pk=id_mascota)

        elif tipo_api == "Decorador":
            mascota_instance = detail_mascota(request=request, pk=id_mascota)

        # mascota_instance = mascota_instance.data
        # mascota_instance = format_mascota(mascota_instance)
        # mascota_instance['vacuna'] = vacunas = [d['id'] for d in mascota_instance.get('vacuna')]
        # mascota_instance['persona'] = mascota_instance.get('persona').get('id')
        # form = MascotaApiForm(initial=mascota_instance)

        mascota_instance.data.update({
            'persona': mascota_instance.data.get('persona').get('id'),
            'vacuna': [d['id'] for d in mascota_instance.data.get('vacuna')],
        })
        form = MascotaApiForm(initial=mascota_instance.data)

    datos = {'form': form, 'tipo': tipo_api}
    return render(request, 'mascota/api_mascota_form.html', datos)


def api_edit2(request, id_mascota):
    """
    Se obtiene la instancia del modelo desde la respuesta del APIVIEW en mascota.data.serializer.instance
     y se manda a un modelForm.
    """

    tipo_api = 'ApiView2'

    if request.method == 'POST':

        request.method = 'GET'
        mascota = DetalleMascota.as_view()(request=request, pk=id_mascota)
        mascota = mascota.data.serializer.instance

        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid:
            request.method = "PUT"
            mascota_instance = DetalleMascota.as_view()(request=request, pk=id_mascota)

            if mascota_instance.status_code == status.HTTP_200_OK:
                messages.success(request, "Se Edito Correctamente la Mascota")
                return HttpResponseRedirect((reverse('mascota:api_list', args=['ApiView'])))
            else:
                # En caso de errores provenientes del endpoint los agregamos manualmente al formulario
                serializers_errors = mascota_instance.data.serializer.errors
                for error in serializers_errors:
                    if error == 'non_field_errors':
                        form.add_error('__all__', serializers_errors.get(error)[0])
                    else:
                        form.add_error(error, serializers_errors.get(error)[0])
    else:
        mascota = DetalleMascota.as_view()(request=request, pk=id_mascota)

        mascota = mascota.data.serializer.instance
        form = MascotaForm(instance=mascota)

    datos = {'form': form, 'tipo': tipo_api}
    return render(request, 'mascota/api_mascota_form.html', datos)


def api_edit3(request, id_mascota):
    """
    Se obtiene la instancia del modelo desde DB con get_object_or_404(Mascota, id=id_mascota)
    y se manda a un modelForm.
    """

    tipo_api = 'ApiView2 get_object_or_404 '

    mascota = get_object_or_404(Mascota, id=id_mascota)
    form = MascotaForm(instance=mascota)

    if request.method == 'POST':
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid:
            request.method = "PUT"
            mascota_instance = DetalleMascota.as_view()(request=request, pk=id_mascota)

            if mascota_instance.status_code == status.HTTP_200_OK:
                messages.success(request, "Se Edito Correctamente la Mascota")
                return HttpResponseRedirect((reverse('mascota:api_list', args=['ApiView'])))
            else:
                # En caso de errores provenientes del endpoint los agregamos manualmente al formulario
                serializers_errors = mascota_instance.data.serializer.errors
                for error in serializers_errors:
                    if error == 'non_field_errors':
                        form.add_error('__all__', serializers_errors.get(error)[0])
                    else:
                        form.add_error(error, serializers_errors.get(error)[0])

    datos = {'form': form, 'tipo': tipo_api}
    return render(request, 'mascota/api_mascota_form.html', datos)


def api_add(request, tipo_api):
    form = MascotaApiForm(request.POST or None)
    if request.POST and form.is_valid():
        # request2 = request.POST.copy()
        # del request2['sexo']
        # request.POST = request2
        if tipo_api == "ApiView":
            mascota_instance = ListMascotas.as_view()(request)

        elif tipo_api == "ViewSet":
            instance = MascotaViewset()
            mascota_instance = instance.create(request=request)

        elif tipo_api == "Genericview":
            mascota_instance = MascotaListGeneric.as_view()(request)

        elif tipo_api == "Decorador":
            mascota_instance = list_mascotas(request=request)

        if mascota_instance.status_code == status.HTTP_201_CREATED:
            messages.success(request, "Se agrego Correctamente la Nueva Mascota")
            return HttpResponseRedirect((reverse('mascota:api_list', args=[tipo_api])))
        else:
            # En caso de errores provenientes del endpoint los agregamos manualmente al formulario
            serializers_errors = mascota_instance.data.serializer.errors
            for error in serializers_errors:
                if error == 'non_field_errors':
                    form.add_error('__all__', serializers_errors.get(error)[0])
                else:
                    form.add_error(error, serializers_errors.get(error)[0])
    datos = {'form': form, 'tipo': tipo_api}
    return render(request, 'mascota/api_mascota_form.html', datos)


def api_delete(request, tipo_api, id_mascota):
    if request.method == "POST":
        if tipo_api == "ApiView":
            instance = DetalleMascota()
            mascota_instance = instance.delete(request=request, pk=id_mascota)

        elif tipo_api == "ViewSet":
            instance = MascotaViewset()
            mascota_instance = instance.destroy(request=request, pk=id_mascota)

        """
        Hay que espeficarle el resquest.method ya que la API tiene varios protocolos HTTP y no acepta el POST para
        realizar esta peticion
        """

        request.method = "DELETE"
        if tipo_api == "Genericview":
            # Forma 2 para hacer una peticion accediendo direntamente al la funcion
            mascota_instance = MascotaDetailsGeneric.as_view()(request=request, pk=id_mascota)

        elif tipo_api == "Decorador":
            mascota_instance = detail_mascota(request=request, pk=id_mascota)

        if mascota_instance.status_code == status.HTTP_204_NO_CONTENT:
            messages.success(request, "Se Elimino Correctamente la  Mascota")
            return HttpResponseRedirect((reverse('mascota:api_list', args=[tipo_api])))
        else:
            messages.warning(request, message=str(mascota_instance.text))

    else:
        if tipo_api == "ApiView":
            instance = DetalleMascota()
            mascota_instance = instance.get(request=request, pk=id_mascota)

        elif tipo_api == "ViewSet":
            instance = MascotaViewset()
            mascota_instance = instance.retrieve(request=request, pk=id_mascota)

        elif tipo_api == "Genericview":
            # Forma 2 para hacer una peticion accediendo direntamente al la funcion
            mascota_instance = MascotaDetailsGeneric.as_view()(request=request, pk=id_mascota)

        elif tipo_api == "Decorador":
            mascota_instance = detail_mascota(request=request, pk=id_mascota)

        mascota_instance = mascota_instance.data

    datos = {'mascota': mascota_instance, 'tipo': tipo_api}
    return render(request, 'mascota/api_mascota_delete.html', datos)


def api_mascota_persona(request, tipo_api, id_mascota):
    if tipo_api == "ApiView":
        instance = MascotaPersonaList()
        mascota_persona_instance = instance.get(request=request, pk=id_mascota)

    elif tipo_api == "ViewSet":
        instance = MascotaViewset()
        mascota_persona_instance = instance.persona(request=request, pk=id_mascota)

    elif tipo_api == "Genericview":
        mascota_persona_instance = MascotaPersonaListGeneric.as_view()(request=request, pk=id_mascota)

    elif tipo_api == "Decorador":
        mascota_persona_instance = mascota_persona_list(request=request, pk=id_mascota)
    mascota_persona_instance = mascota_persona_instance.data

    datos = {'persona': mascota_persona_instance, 'tipo': tipo_api}
    return render(request, 'mascota/api_mascota_persona.html', datos)

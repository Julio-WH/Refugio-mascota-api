from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from app.adopcion.models import Persona,Solicitud
from app.adopcion.forms import AdopcionForm,solicitudForm
# ----------------class-----------------------------------------------
def index_adopcion(request):
    return render(request,'adopcion/index.html')

class AdopcionList(ListView):
    model = Persona
    template_name='adopcion/adopcion_list.html'

class SolicitudList(ListView):
    model=Solicitud
    template_name='adopcion/solicitud_list.html'

class AdopcionCreate(CreateView):
    model= Persona
    form_class=AdopcionForm
    template_name='adopcion/adopcion_form.html'
    success_url=reverse_lazy('adopcion:adopcion_lista')

class SolicitudCreate(CreateView):
    model= Solicitud
    form_class=solicitudForm
    template_name='adopcion/solicitud_form.html'
    second_form_class=AdopcionForm
    success_url=reverse_lazy('adopcion:solicitud_lista')

    def get_context_data(self,**kwargs):
        context=super(SolicitudCreate,self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form']=self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2']=self.second_form_class(self.request.GET)
        return context
    def post(self,request,*args,**kwargs):
        self.object=self.get_object
        form=self.form_class(request.POST)
        form2=self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            solicitud=form.save(commit=False)
            solicitud.persona=form2.save()
            solicitud.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form,form2=form))

class AdopcionUpdate(UpdateView):
    model = Persona
    form_class=AdopcionForm
    template_name='adopcion/adopcion_form.html'
    success_url=reverse_lazy('adopcion:adopcion_lista')

class AdopcionDelete(DeleteView):
    model = Persona
    template_name='adopcion/adopcion_delete.html'
    success_url=reverse_lazy('adopcion:adopcion_lista')

class SolicitudUpdate(UpdateView):
    model=Solicitud
    second_model=Persona
    template_name='adopcion/solicitud_form.html'
    form_class=solicitudForm
    second_form_class=AdopcionForm
    success_url=reverse_lazy('adopcion:solicitud_lista')
    def get_context_data(self,**kwargs):
        context=super(SolicitudUpdate,self).get_context_data(**kwargs)
        pk=self.kwargs.get('pk',0)
        solicitud=self.model.objects.get(id=pk)
        persona=self.second_model.objects.get(id=solicitud.persona_id)
        if 'form' not in context:
            context['form']=self.form_class()
        if 'form2' not in context:
            context['form2']=self.second_form_class(instance=persona)
        context['id']=pk
        return context
    def post(self,request,*arg,**kwargs):
        self.object=self.get_object
        id_solicitud = kwargs['pk']
        solicitud=self.model.objects.get(id=id_solicitud)
        persona=self.second_model.objects.get(id=solicitud.persona_id)
        form=self.form_class(request.POST,instance=solicitud)
        form2=self.second_form_class(request.POST,instance=persona)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())

class SolicitudDelete(DeleteView):
    model=Solicitud
    template_name='adopcion/solicitud_delete.html'
    success_url=reverse_lazy('adopcion:solicitud_lista')


# ----------------Funciones-----------------------------------------------
def adopcion_list(request):
    adopcion=Persona.objects.all()
    datos = {'adopcion':adopcion,'func':'f'}
    return render(request,'adopcion/adopcion_list.html',datos)

def adopcion_view(request):#agregar
    if request.method=='POST':
        form=AdopcionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adopcion:adopcion_funct_lista')
    else:
        form=AdopcionForm()
    
    return render(request,'adopcion/adopcion_form.html',{'form':form})

def adopcion_edit(request,id_adopcion):
    adopcion=Persona.objects.get(id=id_adopcion)
    if request.method=='GET':
        form = AdopcionForm(instance=adopcion)
    else:
        form=AdopcionForm(request.POST,instance=adopcion)
        if form.is_valid():
            form.save()
            return redirect('adopcion:adopcion_funct_lista')
    return render(request,'adopcion/adopcion_form.html',{'form':form})

def adopcion_delete(request,id_adopcion):
    adopcion=Persona.objects.get(id=id_adopcion)
    if request.method=='POST':
        adopcion.delete()
        return redirect('adopcion:adopcion_funct_lista')
    return render(request,'adopcion/adopcion_delete.html',{'adopcion':adopcion,'def':'def'})

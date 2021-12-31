from django.shortcuts import render,redirect
from django.http import HttpResponse
from app.mascota.forms import MascotaForm
from app.mascota.models import Mascota


# Create your views here.
def index_mascota(request):
    return render(request,'mascota/index.html')

def mascota_view(request):
    if request.method=='POST':
        form=MascotaForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mascota:mascota_lista')
    else:
        form=MascotaForm()
    
    return render(request,'mascota/mascota_form.html',{'form':form})

def mascota_list(request):
    mascota=Mascota.objects.all()
    datos = {'mascotas':mascota}
    return render(request,'mascota/mascota_list.html',datos)

def mascota_edit(request,id_mascota):
    mascota=Mascota.objects.get(id=id_mascota)
    if request.method=='GET':
        form = MascotaForm(instance=mascota)
    else:
        form=MascotaForm(request.POST,request.FILES,instance=mascota)
        if form.is_valid():
            form.save()
        return redirect('mascota:mascota_lista')
    return render(request,'mascota/mascota_form.html',{'form':form})

def mascota_delete(request,id_mascota):
    mascota=Mascota.objects.get(id=id_mascota)
    if request.method=='POST':
        mascota.delete()
        return redirect('mascota:mascota_lista')
    return render(request,'mascota/mascota_delete.html',{'mascota':mascota})



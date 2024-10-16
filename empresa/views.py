from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Empresa
from .form import UpdateFormEmpresa
from users.models import User


# actualizar empresa
def actualizar_empresa(request):
    if request.user.es_reclutador:
        empresa = Empresa.objects.get(user=request.user)
        if request.method == 'POST':
            form = UpdateFormEmpresa(request.POST, instance=empresa)
            if form.is_valid():
                var = form.save(commit=False)
                user = User.objects.get(id=request.user.id)
                user.tiene_empresa = True
                var.save()
                user.save()
                messages.info(request,'La información de tu empresa ha sido actualizada')
                return redirect('dashboard')
            else: 
                messages.warning(request,'Error al actualizar empresa')
        else:
            form = UpdateFormEmpresa(instance=empresa)
            context = {'formulario':form}
            return render(request,'empresa/UpdateEmpresa.html',context)
    else:
        messages.warning(request,'Permiso denegado')
        return redirect('dashboard')
    

# detalles de empresa
def details_empresa(request,pk):
    empresa = Empresa.objects.get(pk=pk)
    context = {'empresa':empresa}
    return render(request,'empresa/DetailsEmpresa.html',context)



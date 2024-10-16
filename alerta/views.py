from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Alerta
from .form import AddFormAlerta, UpdateFormAlerta


#crear una alerta
def create_alerta(request):
    if request.user.es_reclutador and request.user.tiene_empresa:
        if request.method == 'POST':
            form = AddFormAlerta(request.POST)
            if form.is_valid():
                var = form.save(commit=False)
                var.user = request.user
                var.empresa = request.user.empresa
                var.save()
                messages.info(request,'Se ha creado una nueva alerta de empleo')
            else:
                messages.warning(request,'Error al crear la alerta de empleo')
                return redirect('create-alerta')
        else:
            form = AddFormAlerta()
            context = {'formulario':form}
            return render(request,'alerta/AddAlerta.html',context)
    else:
        messages.warning(request,'Permiso denegado')
        return redirect('dashboard')
    

#actualizar una alerta
def update_alerta(request, pk):
    alerta = Alerta.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateFormAlerta(request.POST, instance=alerta)
        if form.is_valid():
            form.save()
            messages.info(request,'Se ha actualizado la alerta de empleo')
        else:
            messages.warning(request,'Error al actualizar la alerta de empleo')
    else:
        form = UpdateFormAlerta(instance=alerta)
        context = {'formulario':form}
        return render(request,'alerta/UpdateAlerta.html',context)
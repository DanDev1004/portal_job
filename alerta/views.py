from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Alerta, AplicarTrabajo
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
                return redirect('dashboard')
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
            return redirect('dashboard')
        else:
            messages.warning(request,'Error al actualizar la alerta de empleo')
    else:
        form = UpdateFormAlerta(instance=alerta)
        context = {'formulario':form}
        return render(request,'alerta/UpdateAlerta.html',context)
    


def gestion_alertas(request):
    alertas = Alerta.objects.filter(user=request.user,empresa=request.user.empresa)
    context = {'alertas':alertas}
    return render(request, 'alerta/GestionAlertas.html',context)



def aplicando_para_trabajo(request, pk):
    if request.user.is_authenticated and request.user.es_aplicante:
        alerta = Alerta.objects.get(pk=pk)

        if AplicarTrabajo.objects.filter(user=request.user, job=pk).exists():
            messages.warning(request,'Permiso denegado')
            return redirect('dashboard')
        else:
            AplicarTrabajo.objects.create(
                alerta=alerta,
                user=request.user,
                postulacion='Pendiente'
            )
            messages.info(request,'Aplicaste al trabajo de forma exitosa.')
            return redirect('dashboard')
    else:
        messages.info(request,'Inicia sesión para continuar')
        return redirect('login')
    


def aplicantes_list(request, pk):
    alerta = Alerta.objects.get(pk=pk)
    aplicantes = alerta.aplicartrabajo_set.all()
    print("Hola",aplicantes)
    context = {'alerta':alerta,'aplicantes':aplicantes}
    return render(request,'alerta/aplicanteList.html',context)
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Curriculum
from users.models import User
from .form import UpdateFormCurriculum

def update_curriculum(request):
    if request.user.es_aplicante:
        curriculum = Curriculum.objects.get(user=request.user)
        if request.method == 'POST':
            form = UpdateFormCurriculum(request.POST, request.FILES, instance=curriculum)
            if form.is_valid():
                var = form.save(commit=False)
                user = User.objects.get(pk=request.user.id)
                user.tiene_curriculum = True
                user.save()
                var.save()
                messages.info(request,'Tu curriculum ha sido actualizado.')
                return redirect('dashboard')
            else:
                messages.warning(request,'Error al actualizar curriculum')
        else:
            form = UpdateFormCurriculum(instance=curriculum)
            context = {'formulario':form}
            return render(request,'curriculum/UpdateCurriculum.html',context)
    else:
        messages.warning(request,'Permiso denegado')
        return redirect('dashboard')

def details_curriculum(request,pk):
    curriculum = Curriculum.objects.get(pk=pk)
    context = {'curriculum':curriculum}
    return render(request,'curriculum/DetailsCurriculum.html',context)

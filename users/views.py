from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .models import User
from .form import FormAddUser
from curriculum.models import Curriculum
from empresa.models import Empresa


#registro para aplicante
def registrar_aplicante(request):
    if request.method == 'POST':
        form = FormAddUser(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.es_aplicante = True
            var.username = var.email
            var.save()
            Curriculum.objects.create(user=var)
            messages.info(request, 'Su cuenta ha sido creada.')
            return redirect('login')
        else:
            messages.warning(request, 'Error al registrar usuario aplicante')
            context = {'formulario':form}
            print(form.errors) 
            return render(request, 'users/AddUser-aplicante.html', context)
    else:
        form = FormAddUser()
        context = {'formulario':form}
        print(form.errors) 
        return render(request, 'users/AddUser-aplicante.html', context)
    

#registro para reclutador
def registrar_reclutador(request):
    if request.method == 'POST':
        form = FormAddUser(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.es_reclutador = True
            var.username = var.email
            var.save()
            Empresa.objects.create(user=var)
            messages.info(request, 'Su cuenta ha sido creada.')
            return redirect('login')
        else:
            messages.warning(request, 'Error al registrar usuario reclutador')
            print(form.errors) 
            return redirect('AddUser-reclutador')
    else:
        form = FormAddUser()
        context = {'formulario':form}
        print(form.errors) 
        return render(request, 'users/AddUser-reclutador.html', context)
    

#login 
def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request,username=email,password=password)
        if user is not None and user.is_active:
            login(request,user)
            return redirect('home')
        else:
            messages.warning(request, 'Error al iniciar sesión')
            return redirect('login')
    else:
        return render(request, 'users/login.html')
    

#logout
def logout_user(request):
    logout(request)
    messages.info(request,'Tu sesión ha sido finalizada')
    return redirect('login')

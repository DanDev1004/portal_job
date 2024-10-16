from django.urls import path
from .import views

urlpatterns = [
    path('AddUser-aplicante/', views.registrar_aplicante, name='AddUser-aplicante'),
    path('AddUser-reclutador/', views.registrar_reclutador, name='AddUser-reclutador'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout')
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('alerta-list/', views.listar_alertas, name='alerta-list'),
    path('alerta-details/<int:pk>/',views.detalles_alerta, name='alerta-details')
]

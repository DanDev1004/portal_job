from django.urls import path
from . import views

urlpatterns = [
    path('obtener-provincias/<int:departamento_id>/', views.obtener_provincias, name='obtener_provincias'),
    path('obtener-distritos/<int:provincia_id>/', views.obtener_distritos, name='obtener_distritos'),
]

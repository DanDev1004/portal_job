from django.urls import path 
from . import views

urlpatterns = [
    path('update-empresa/',views.actualizar_empresa,name='update-empresa'),
    path('details-empresa/<int:pk>/',views.details_empresa,name='details-empresa')
]

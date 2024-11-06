from django.urls import path
from . import views

urlpatterns = [
    path('create-alerta/',views.create_alerta,name='create-alerta'),
    path('update-alerta/<int:pk>/',views.update_alerta,name='update-alerta'),
    path('gestion-alertas/',views.gestion_alertas, name='gestion-alertas'),
    path('aplicando-para-trabajo/<int:pk>/',views.aplicando_para_trabajo, name='aplicando-para-trabajo'),
    path('aplicante-list/<int:pk>/',views.aplicantes_list, name='aplicante-list')
]

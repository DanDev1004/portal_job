from django.urls import path
from . import views

urlpatterns = [
    path('create-alerta/',views.create_alerta,name='create-alerta'),
    path('update-alerta/<int:pk>/',views.update_alerta,name='update-alerta')
]

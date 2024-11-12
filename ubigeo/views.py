# ubigeo/views.py
from django.http import JsonResponse
from .models import Provincia, Distrito

def obtener_provincias(request, departamento_id):
    provincias = Provincia.objects.filter(departamento_id=departamento_id).values('id', 'nombre')
    return JsonResponse(list(provincias), safe=False)

def obtener_distritos(request, provincia_id):
    distritos = Distrito.objects.filter(provincia_id=provincia_id).values('id', 'nombre')
    return JsonResponse(list(distritos), safe=False)

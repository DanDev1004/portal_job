from django.shortcuts import render
from alerta.models import Alerta, AplicarTrabajo
from .filter import FiltrosAlerta

def home(request):
    alertasFiltradas = FiltrosAlerta(request.GET, queryset=Alerta.objects.filter(disponible=True).order_by('-apertura'))
    context = {'alertas_filtradas':alertasFiltradas}
    return render(request,'website/home.html', context)

def listar_alertas(request):
    alertas = Alerta.objects.filter(disponible=True).order_by('-apertura')
    context = {'alertas':alertas}
    return render(request,'website/alertaList.html', context)

def detalles_alerta(request, pk):
    alerta = Alerta.objects.get(pk=pk)
    ya_aplicaste = False

    if request.user.is_authenticated and request.user.es_aplicante:
        if AplicarTrabajo.objects.filter(user=request.user, alerta=pk).exists():
            ya_aplicaste = True

    context = {'alerta':alerta, 'ya_aplicaste':ya_aplicaste}
    return render(request,'website/alertaDetails.html',context)
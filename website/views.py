from django.shortcuts import render
from alerta.models import Alerta, AplicarTrabajo

def home(request):
    return render(request,'website/home.html')

def listar_alertas(request):
    alertas = Alerta.objects.filter(disponible=True).order_by('-apertura')
    context = {'alertas':alertas}
    return render(request,'website/alertaList.html', context)

def detalles_alerta(request, pk):
    if AplicarTrabajo.objects.filter(user=request.user, alerta=pk).exists():
        ya_aplicaste = True
    else:
        ya_aplicaste = False

    alerta = Alerta.objects.get(pk=pk)
    context = {'alerta':alerta, 'ya_aplicaste':ya_aplicaste}
    return render(request,'website/alertaDetails.html',context)
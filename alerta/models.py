from django.db import models
from empresa.models import Empresa
from users.models import User

class Alerta(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    salario = models.PositiveIntegerField(default=1200)
    requerimientos = models.TextField()
    candidato_ideal = models.TextField()
    disponible = models.BooleanField(default=False)
    apertura = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.titulo
    

class AplicarTrabajo(models.Model):
    estados_postulacion = (
        ('Aceptado','Aceptado'),
        ('Rechazado','Rechazado'),
        ('Pendiente','Pendiente')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    alerta = models.ForeignKey(Alerta, on_delete=models.CASCADE)
    postulacion = models.CharField(max_length=20, choices=estados_postulacion)
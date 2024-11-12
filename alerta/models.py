from django.db import models
from users.models import User
from empresa.models import Empresa
from ubigeo.models import Departamento, Provincia, Distrito 


class Industria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Alerta(models.Model):
    opciones_alerta = (
        ("Remoto", "Remoto"),
        ("Presencial", "Presencial"),
        ("Semipresencial", "Semipresencial")
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    #salario = models.PositiveIntegerField(default=1200)
    salario = models.DecimalField(max_digits=10, decimal_places=2, default=1200.00)
    requerimientos = models.TextField()
    candidato_ideal = models.TextField()
    disponible = models.BooleanField(default=False)
    apertura = models.DateTimeField(auto_now_add=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.DO_NOTHING, null=True, blank=True)
    provincia = models.ForeignKey(Provincia, on_delete=models.DO_NOTHING, null=True, blank=True)
    distrito = models.ForeignKey(Distrito, on_delete=models.DO_NOTHING, null=True, blank=True)
    industria = models.ForeignKey(Industria, on_delete=models.DO_NOTHING, null=True, blank=True)
    tipo_alerta = models.CharField(max_length=20, choices=opciones_alerta, null=True, blank=True)

    def __str__(self):
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
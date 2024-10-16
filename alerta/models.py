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

    def __str__(self) -> str:
        return self.titulo
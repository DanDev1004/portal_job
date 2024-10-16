from django.db import models
from users.models import User

class Curriculum(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=100, null=True, blank=True)
    apellidos = models.CharField(max_length=100, null=True, blank=True)
    ubicacion = models.CharField(max_length=100, null=True, blank=True)
    titulo_profesional = models.CharField(max_length=100, null=True, blank=True)
    #insertar cv

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'

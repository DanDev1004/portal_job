from django.db import models
from users.models import User

class Empresa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100, null=True, blank=True)
    est_date = models.PositiveIntegerField(null=True, blank=True)
    distrito = models.CharField(max_length=100, null=True, blank=True)
    provincia = models.CharField(max_length=100, null=True, blank=True)
    departamento = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nombre

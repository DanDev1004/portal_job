from django.db import models
from users.models import User
from ubigeo.models import Departamento, Provincia, Distrito  

class Empresa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100, null=True, blank=True)
    est_date = models.PositiveIntegerField(null=True, blank=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.DO_NOTHING, null=True, blank=True)
    provincia = models.ForeignKey(Provincia, on_delete=models.DO_NOTHING, null=True, blank=True)
    distrito = models.ForeignKey(Distrito, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.nombre

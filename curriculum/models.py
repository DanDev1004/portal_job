from django.db import models
from users.models import User
from ubigeo.models import Departamento, Provincia, Distrito 



class Curriculum(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=100, null=True, blank=True)
    apellidos = models.CharField(max_length=100, null=True, blank=True)
    ubicacion = models.CharField(max_length=100, null=True, blank=True)
    titulo_profesional = models.CharField(max_length=100, null=True, blank=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.DO_NOTHING, null=True, blank=True)
    provincia = models.ForeignKey(Provincia, on_delete=models.DO_NOTHING, null=True, blank=True)
    distrito = models.ForeignKey(Distrito, on_delete=models.DO_NOTHING, null=True, blank=True)
    cargar_curriculum = models.FileField(upload_to='curriculum', null=True, blank=True)

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'

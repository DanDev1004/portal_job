from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    es_reclutador = models.BooleanField(default=False)
    es_aplicante = models.BooleanField(default=False)

    tiene_curriculum = models.BooleanField(default=False)
    tiene_empresa = models.BooleanField(default=False)

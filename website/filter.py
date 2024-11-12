import django_filters
from alerta.models import Alerta

class FiltrosAlerta(django_filters.FilterSet):
    class Meta:
        model = Alerta
        fields = ['titulo','departamento','provincia','distrito','tipo_alerta','industria']
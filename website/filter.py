import django_filters
from alerta.models import Alerta

class FiltrosAlerta(django_filters.FilterSet):
    titulo = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Alerta
        fields = ['titulo','departamento','provincia','distrito','tipo_alerta','industria']
from django.urls import path
from . import views

urlpatterns = [
    path('update-curriculum/',views.update_curriculum,name='update-curriculum'),
    path('details-curriculum/',views.details_curriculum,name='details-curriculum')
]

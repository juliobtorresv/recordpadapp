from django.urls import path


from . import views
from unidadEducativa import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ingresoue/', views.ingresoUE),
    path('ingresoue/datosue/', views.datosUE),

]

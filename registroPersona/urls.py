
from django.urls import path
from registroPersona import views


urlpatterns = [
    path('inicioSesion',views.inicioSesion),
    path('principal',views.principal),
    path('persona',views.persona_view),
]

from django.urls import path
from registroPersona import views


urlpatterns = [
     path('',views.inicioPersona),
    path('principal',views.principal),
    path('persona',views.persona_view),
]
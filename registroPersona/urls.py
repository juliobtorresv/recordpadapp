
from django.urls import path
from registroPersona import views


urlpatterns = [
     path('',views.inicio),
    path('principal',views.principal),
    path('persona',views.persona_view),
]
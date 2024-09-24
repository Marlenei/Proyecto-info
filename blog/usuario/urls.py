from django.urls import path
from . import views

urlpatterns = [
        path("registro", views.Usuario_created, name = "registro"),
        path("inicio", views.inicio, name="inicio"),

]
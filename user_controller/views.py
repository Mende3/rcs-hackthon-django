from django.shortcuts import render
from rest_framework import generics

from .UsuarioSerializer import UsuarioSerializer
from .models import UsuariosDoSistema

class listAndCreateUser (generics.ListCreateAPIView) :
    serializer_class = UsuarioSerializer
    def get_queryset(self):
        return UsuariosDoSistema.objects.filter(nivel_de_acesso="usario")
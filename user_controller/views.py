from django.shortcuts import render
from django.utils.decorators import method_decorator

from rest_framework import generics

from rolepermissions.roles import assign_role
from rolepermissions.decorators import has_role_decorator, has_permission_decorator

from .UsuarioSerializer import UsuarioSerializer
from .models import UsuariosDoSistema

@method_decorator(has_permission_decorator("criar_novo_usuario"), name="dispatch")
class ListCreateNormalUser (generics.ListCreateAPIView) :
    serializer_class = UsuarioSerializer

    def get_queryset(self):
        return UsuariosDoSistema.objects.filter(cargo="usuario")
    
    def perform_create(self, serializer):
        user = serializer.save()

        assign_role (user, 'usuario_normal')

@method_decorator(has_permission_decorator("criar_admin"), name="dispatch")
class ListCreateAdmin(generics.ListCreateAPIView):
    serializer_class = UsuarioSerializer

    def get_queryset(self):
        return UsuariosDoSistema.objects.filter(cargo="admin")

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['cargo'] = 'admin'
        return context

    def perform_create(self, serializer):
        user = serializer.save()
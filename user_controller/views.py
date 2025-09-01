# views.py
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import UsuariosDoSistema
from .UsuarioSerializer import UsuarioSerializer, CustomTokenObtainPairSerializer
from .permissions import CargoBasedPermission

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class ListCreateNormalUser(generics.ListCreateAPIView):
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated, CargoBasedPermission]
    required_permission = "criar_novo_usuario"  # Atributo personalizado

    def get_queryset(self):
        return UsuariosDoSistema.objects.filter(cargo="usuario normal")
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['cargo'] = 'usuario normal'
        return context

class ListCreateAdmin(generics.ListCreateAPIView):
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated, CargoBasedPermission]
    required_permission = "criar_admin"  # Atributo personalizado

    def get_queryset(self):
        return UsuariosDoSistema.objects.filter(cargo="admin")

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['cargo'] = 'admin'
        return context
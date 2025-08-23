from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UsuariosDoSistema (AbstractUser) :

    NIVEIS = (
        ("admin", "Administrador"),
        ("usuario", "Usuario normal")
    )

    telefone = models.CharField (max_length=20, blank=True, null=True)
    cargo = models.CharField (max_length=100, blank=False, null=False, default="Sem cargo")
    nivel_de_acesso = models.CharField (
        max_length=20,
        choices=NIVEIS,
        default="usuario"
    )

    def is_admin (self):
        return self.nivel_de_acesso == "admin"

    def is_usuario (self):
        return self.nivel_de_acesso == "usuario"
    
    def __str__(self):
        return (f"{self.email} - {self.nivel_de_acesso}")
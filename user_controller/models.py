from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UsuariosDoSistema (AbstractUser) :
    telefone = models.CharField (max_length=20, blank=True, null=True)
    cargo = models.CharField (
        max_length=50,
        default="usuario normal"
    )
    
    def __str__(self):
        return (f"{self.email} - {self.cargo}")
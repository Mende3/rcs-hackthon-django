from rest_framework import serializers
from .models import UsuariosDoSistema

class UsuarioSerializer (serializers.ModelSerializer) :
    class Meta :
        model = UsuariosDoSistema
        fields = ["id", "username", "email", "telefone", "cargo", "nivel_de_acesso", "password"]
        extra_kwargs = {
            "password": {"write_only": True}
        }
    
    def create(self, validated_data):
        nivel = validated_data.get("nivel_de_acesso", "usuario")
        user = UsuariosDoSistema (
            username = validated_data ["username"],
            email = validated_data["email"],
            telefone = validated_data["telefone"],
            cargo = validated_data.get["cargo"],
            nivel_de_acesso = nivel,
        )
        user.set_password (validated_data["password"])

        if nivel == "admin" :
            user.is_superuser = True
            user.is_staff = True
        
        user.save
        return user
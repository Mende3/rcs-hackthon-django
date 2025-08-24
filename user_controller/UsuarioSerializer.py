from rest_framework import serializers
from .models import UsuariosDoSistema
from rolepermissions.roles import assign_role

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuariosDoSistema
        fields = ["id", "first_name", "last_name", "username", "email", "telefone", "password", "cargo"]
        extra_kwargs = {
            "password": {"write_only": True}
        }
    
    def create(self, validated_data):
        cargo = self.context.get('cargo', 'usuario normal')
        user = UsuariosDoSistema(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            username=validated_data["username"],
            email=validated_data["email"],
            telefone=validated_data.get("telefone", None),  # Use .get() para lidar com campos opcionais
            cargo=cargo  # Atribuir o valor de cargo ao modelo
        )
        user.set_password(validated_data["password"])
        user.save()
        
        if cargo == 'admin':
            assign_role(user, 'administrador')  # Atribui o papel de admin
        else:
            assign_role(user, 'usuario_normal')  # Atribui o papel de usuário normal
        return user
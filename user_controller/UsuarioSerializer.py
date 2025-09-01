from rest_framework import serializers
from .models import UsuariosDoSistema
# serializers.py (ou no mesmo arquivo do seu serializer existente)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuariosDoSistema
        fields = ["id", "first_name", "last_name", "username", "email", "telefone", "password", "cargo"]
        extra_kwargs = {
            "password": {"write_only": True}
        }
    
# UsuarioSerializer.py - Adicione debug
    def create(self, validated_data):
        cargo = self.context.get('cargo', 'usuario normal')
        user = UsuariosDoSistema(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            username=validated_data["username"],
            email=validated_data["email"],
            telefone=validated_data.get("telefone", None),
            cargo=cargo
        )
        user.set_password(validated_data["password"])
        user.save()
        
        print(f"Atribuindo cargo: {cargo}")  # DEBUG
        
        if cargo == 'admin':
            print(" 'administrador' atribuída")
        else:
            print("Role 'usuario_normal' atribuída")
        
        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        # Adicionar a role ao token
        token['role'] = user.cargo
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['email'] = user.email
        
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        
        # Adicionar informações do usuário na resposta
        user = self.user
        data['user'] = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'role': user.cargo,
            'telefone': user.telefone
        }
        
        return data
from rest_framework import serializers
from .models import Emails, PedidosDeCotacao

class PedidosDeCotacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidosDeCotacao
        fields = ['empresa', 'numero', 'requisicao', 'resposta', 'status']

class EmailsSerializer(serializers.ModelSerializer):
    pedidos = PedidosDeCotacaoSerializer(many=True)
    email = serializers.EmailField(validators=[])
    
    class Meta:
        model = Emails
        fields = ['email', 'pedidos']
    
    def create(self, validated_data):
        pedidos_data = validated_data.pop('pedidos', [])
        email_obj, created = Emails.objects.get_or_create(email=validated_data['email'])
        for pedido in pedidos_data:
            PedidosDeCotacao.objects.create(email=email_obj, **pedido)
        return email_obj
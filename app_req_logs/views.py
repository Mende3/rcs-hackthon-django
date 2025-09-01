from django.shortcuts import render
from rest_framework import generics
from django.utils.decorators import method_decorator


from .SerializersEmail import EmailsSerializer, PedidosDeCotacaoSerializer
from .models import Emails, PedidosDeCotacao

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

from user_controller.permissions import CargoBasedPermission



class CrateEmails (generics.CreateAPIView):
    queryset = Emails.objects.all()
    serializer_class = EmailsSerializer
    permission_classes = [AllowAny]

#@method_decorator(has_permission_decorator("listar_emails_de_clientes"), name="dispatch")
class ListEmails (generics.ListAPIView):
    queryset = Emails.objects.all()
    serializer_class = EmailsSerializer
    permission_classes = [IsAuthenticated, CargoBasedPermission]
    required_permission = "listar_emails_de_clientes"

#@method_decorator(has_permission_decorator("apagar_emails_de_clientes"), name="dispatch")
class DeleteEmails (generics.DestroyAPIView):
    queryset = Emails.objects.all()
    serializer_class = EmailsSerializer
    permission_classes = [AllowAny]



class DeleteEmailsReq (generics.DestroyAPIView):
    queryset = PedidosDeCotacao.objects.all()
    serializer_class = PedidosDeCotacaoSerializer
    permission_classes = [IsAuthenticated, CargoBasedPermission]
    required_permission = "apagar_emails_de_clientes"
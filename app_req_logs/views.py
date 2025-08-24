from django.shortcuts import render
from rest_framework import generics
from django.utils.decorators import method_decorator


from .SerializersEmail import EmailsSerializer
from .models import Emails, PedidosDeCotacao
from rolepermissions.decorators import has_role_decorator, has_permission_decorator


class CrateEmails (generics.CreateAPIView):
    queryset = Emails.objects.all()
    serializer_class = EmailsSerializer

@method_decorator(has_permission_decorator("listar_emails_de_clientes"), name="dispatch")
class ListEmails (generics.ListAPIView):
    queryset = Emails.objects.all()
    serializer_class = EmailsSerializer

@method_decorator(has_permission_decorator("apagar_emails_de_clientes"), name="dispatch")
class DeleteEmails (generics.DestroyAPIView):
    queryset = Emails.objects.all()
    serializer_class = EmailsSerializer


from django.shortcuts import render
from rest_framework import generics

from .SerializersEmail import EmailsSerializer
from .models import Emails, PedidosDeCotacao


class ListEmails (generics.ListCreateAPIView):
    queryset = Emails.objects.all()
    serializer_class = EmailsSerializer
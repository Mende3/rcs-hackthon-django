from django.urls import path
from .views import CrateEmails, ListEmails, DeleteEmails

urlpatterns = [
    path('criar_pedidos_de_quote/', CrateEmails.as_view()),
    path('listar_pedidos_de_quote/', ListEmails.as_view()),
    path('delete_pedidos_de_quote/<pk>', DeleteEmails.as_view()),
]
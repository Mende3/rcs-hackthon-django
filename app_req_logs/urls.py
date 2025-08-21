from django.urls import path
from .views import ListEmails

urlpatterns = [
    path('criar_pedidos_de_quote/', ListEmails.as_view()),
]
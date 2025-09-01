from django.contrib import admin
from .models import Emails, PedidosDeCotacao

# Register your models here.
admin.site.register ([Emails, PedidosDeCotacao])
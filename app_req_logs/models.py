from django.db import models

# Create your models here.
class Emails (models.Model) :
    email = models.EmailField (
        max_length=254,
        null=False,
        blank=False,
        unique=True,
    )
    date_registrada = models.DateField(auto_now_add=True)
    hora_registrada = models.TimeField(auto_now_add=True)
    
    def __str__(self) :
        return self.email
    
    def total_pedidos (self):
        return self.pedidos.count()
    
    def pedidos_pendentes (self) :
        return self.pedidos.filter(status='pendente').count()
    
class PedidosDeCotacao (models.Model) :
    
    STATUS_CHOICES = (
        ('pendente', 'Pendente'),
        ('respondido', 'Respondido'),
        ('cancelado', 'Cancelado'),
    )
    
    email = models.ForeignKey (
        Emails,
        on_delete=models.CASCADE,
        related_name='pedidos'
    )
   
    n_pedido = models.IntegerField()
    empresa = models.CharField(max_length=255)
    numero = models.CharField(max_length=50)
    requisicao = models.TextField()
    resposta = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    data = models.CharField(max_length=20)
    hora = models.CharField(max_length=20)
    
    def save(self, *args, **kwargs):
        if not self.n_pedido:  # só atribui se ainda não tiver número
            # pega o maior número de pedido do email e adiciona 1
            ultimo_pedido = PedidosDeCotacao.objects.filter(email=self.email).order_by('-n_pedido').first()
            self.n_pedido = 1 if not ultimo_pedido else ultimo_pedido.n_pedido + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Pedido {self.n_pedido} - {self.empresa}"


from django.db import models
from accounts.models import UserProfile
# Create your models here.
class Material(models.Model):
    nome = models.CharField(max_length=50)
    quantidade_total = models.PositiveIntegerField(default=0)
    quantidade_disponivel = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nome
    
class Pedido(models.Model):
    usuário = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    criado = models.DateTimeField(auto_now_add=True)
    data_prevista = models.DateTimeField()
    pendência = models.BooleanField(default=True) 
    aprovado = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.usuário} | {self.material} | {self.pendência} | {self.aprovado}'
    
    class Meta:
        ordering = ['-criado']



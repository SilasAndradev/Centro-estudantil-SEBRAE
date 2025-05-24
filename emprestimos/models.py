from django.db import models
from accounts.models import UserProfile
from moderator.models import Material


class Emprestimo(models.Model):
    usuário = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING, related_name='aluno')
    material = models.ForeignKey(Material, on_delete=models.DO_NOTHING)
    quem_aprovou = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING, related_name='aprovou_o_pedido', null=True, blank=True)
    quantidade = models.PositiveIntegerField()
    data_prevista = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    data_devolvida = models.DateTimeField(blank=True, null=True)
    devolvido = models.BooleanField(default=False)
    devolução_confirmada = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.aluno} | {self.material} | {self.devolvido} | {self.devolução_confirmada}'
    
    class Meta:
        ordering = ['-created']

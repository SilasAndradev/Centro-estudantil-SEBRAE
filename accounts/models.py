from django.db import models
from django.contrib.auth.models import User



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)

    nome_completo = models.CharField(max_length=255)

    matricula = models.CharField(max_length=15, unique=True)

    curso = models.CharField(blank=True, null=True, max_length=15)

    aprovado = models.BooleanField(default=False)

    CommentPermission = models.BooleanField(default=True)

    bloqueado = models.BooleanField(default=False)



    
    def __str__(self):
        return self.user.username
    

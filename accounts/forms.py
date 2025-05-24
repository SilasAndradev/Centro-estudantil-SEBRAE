from django.forms import ModelForm
from accounts.models import UserProfile
from django import forms


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ['user', 'bloqueado', 'moderador', 'CommentPermission', 'aprovado']
        widgets = {
            'nome_completo':forms.TextInput(attrs={'class': 'form-control'}),
            'matricula':forms.TextInput(attrs={'class': 'form-control'}),
            'curso':forms.Select(
                attrs={
                    'placeholder': 'Escolha o seu curso',
                    'class': 'form-control'
                    }, 
                choices={
                    'Informática':'Informática', 'Agropecuária':'Agropecuária', 'Alimentos':'Alimentos', 'Zootecnia':'Zootecnia'
                    }
                    ),
        }
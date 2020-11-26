from django.forms import ModelForm
# Importo o modelo que será implementado no meu form
from .models import Cliente
from django import forms


class ClienteForm(forms.ModelForm):
    # O meta copia o modelo de form a ser implementado
    class Meta:
        model = Cliente
        # Defino os campos que estarão presentes no form
        fields = ('nome', 'identificador', 'email', 'telefone', 'foto')

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'identificador': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.NumberInput(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control-file'})
        }
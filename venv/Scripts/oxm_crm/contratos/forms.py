from django.forms import ModelForm
# Importo o modelo que será implementado no meu form
import clientes
from .models import Contrato
from django import forms


class ContratoForm(forms.ModelForm):
    # O meta copia o modelo de form a ser implementado
    class Meta:
        model = Contrato
        # Defino os campos que estarão presentes no form
        fields = ('nome', 'bioContrato', 'codigo', 'cliente', 'valorContrato', 'valorGasto', 'profit', 'dataContrato', 'dataEntrega', 'arquivos')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['cliente'].queryset = clientes.objects.none()

            # Procura o cliente na lista de clientes
            if 'cliente' in self.data:
                try:
                    cliente_id = int(self.data.get('cliente'))
                    # Utiliza o campo cliente do contrato para procurar na lista de clientes
                    self.fields['cliente'].queryset = clientes.objects.filter(cleinte_id=cliente_id).order_by('nome')
                except (ValueError, TypeError):
                    pass  # Entrada inválida
            elif self.instance.pk:
                self.fields['cliente'].queryset = self.instance.cliente.nome.order_by('nome')

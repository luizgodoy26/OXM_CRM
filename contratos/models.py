
from django.db import models
from clientes.models import Cliente


class Contrato(models.Model):
    nome = models.CharField(max_length=60)
    bioContrato = models.TextField(null=True, blank=True)

    # Dropdown com listagem de clientes
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)

    valorContrato = models.FloatField(max_length=45, null=True, blank=True, default=0)
    valorGasto = models.FloatField(max_length=45, null=True, blank=True, default=0)


    dataContrato = models.DateField(null=True, blank=True)
    dataEntrega = models.DateField(null=True, blank=True)

    arquivos = models.FileField(upload_to='arquivos_contratos', null=True, blank=True)


    def __str__(self):
        return self.nome

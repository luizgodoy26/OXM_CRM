from datetime import timezone

from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import activate
from clientes.models import Cliente
from oxm_crm import settings


class Contrato(models.Model):
    nome = models.CharField(max_length=60)
    bioContrato = models.TextField(null=True, blank=True)

    codigo = models.IntegerField()
    # Dropdown com listagem de clientes
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)

    valorContrato = models.FloatField(max_length=45, null=True, blank=True)
    valorGasto = models.FloatField(max_length=45, null=True, blank=True)
    profit = models.FloatField(max_length=45, null=True, blank=True)


    dataContrato = models.DateField(null=True, blank=True)
    dataEntrega = models.DateField(null=True, blank=True)
    # Adiciona data atual do sistema
    #dataIncusao = models.DateTimeField(editable=False)

    arquivos = models.FileField(upload_to='arquivos_contratos', null=True, blank=True)

    #Para que seja exibido o nome do cliente no admin, deve ser feito este método
    def __str__(self):
        return self.nome

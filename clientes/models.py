from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=60)

    # O null=True, blank=True fazem com que o parâmetro seja opcional
    identificador = models.BigIntegerField(null=True, blank=True)
    email = models.CharField(max_length=45, null=True, blank=True)
    telefone = models.BigIntegerField(null=True, blank=True)

    # upload_to='fotos_clientes' permite que o arquivo seja salvo em pasta específica
    foto = models.ImageField(upload_to='fotos_clientes', null=True, blank=True)

    # Para que seja exibido o nome do cliente no admin, deve ser feito este método
    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=60)

    # O null=True, blank=True fazem com que o parâmetro seja opcional
    identificador = models.BigIntegerField(null=True, blank=True)
    email = models.CharField(max_length=45, null=True, blank=True)
    telefone = models.BigIntegerField(null=True, blank=True)

    # upload_to='fotos_clientes' permite que o arquivo seja salvo em pasta específica
    foto = models.ImageField(upload_to='fotos_clientes', null=True, blank=True)



    #Para que seja exibido o nome do cliente no admin, deve ser feito este método
    def __str__(self):
        return self.nome


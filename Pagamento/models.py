from django.db import models

class estabelecimento(models.Model):
    nome = models.CharField(max_length=250,null=False)
    cnpj = models.CharField(max_length=250,null=False)
    dono = models.CharField(max_length=30,null=False)
    telefone = models.CharField(max_length=250)
    data_de_transacao = models.DateFild(auto_now_add=True) #auto

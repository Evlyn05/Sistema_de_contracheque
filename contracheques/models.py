from django.db import models
from django.contrib.auth.models import User

class ContraCheque(models.Model):
    nome_funcionario = models.CharField(max_length=100)
    data_criacao = models.DateField()
    conta = models.CharField(max_length=20)
    agencia = models.CharField(max_length=20)
    arquivo = models.FileField(upload_to='contracheques/')
    ano = models.IntegerField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"ContraCheque de {self.nome_funcionario} - {self.ano}"

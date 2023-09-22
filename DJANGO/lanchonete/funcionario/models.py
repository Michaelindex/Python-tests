from django.db import models

# Create your models here.
class Funcionario(models.Model): 
    nome = models.CharField(max_length=200)
    funcao= models.CharField(max_length=200, default='')
    email = models.CharField(max_length=200)
    def __str__(self):
        return self.nome

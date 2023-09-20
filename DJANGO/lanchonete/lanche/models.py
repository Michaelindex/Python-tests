from django.db import models
from funcionario.models import Funcionario
from datetime import datetime
import uuid
def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

# Create your models here.
class Lanche(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    nome=models.CharField('Nome', max_length=100)
    preco=models.DecimalField('Preco', decimal_places=2, max_digits=8)
    categoria=models.CharField('Categoria', max_length=20, default='cat')
    ingredientes = models.TextField('Ingredientes', max_length=300)
    date_lanche = models.DateTimeField(default=datetime.now, blank=True)
    foto_lanche = models.ImageField(upload_to=get_file_path, blank=True)
    publicado = models.BooleanField(default=False)
    def __str__(self):
        return self.nome
    
from distutils.command.upload import upload
from statistics import mode
from django.db import models

# Create your models here.

class Livro(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, verbose_name="Título")
    image = models.ImageField(upload_to='imagens/',verbose_name="Imagem",null=True)
    description = models.TextField(verbose_name="Descrição", null=True)

    def __str__(self) -> str:
        fila = "Titulo: " + self.title + " - "+ "Description: "+ self.description
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()
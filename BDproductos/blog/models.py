from django.db import models
from django.contrib.auth.models import User
import os


# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, null=False, unique=True, verbose_name='Nombre')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'categories'
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        ordering = ['id']

class Post(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100, unique=True, null=False, verbose_name='Título')
    contenido = models.TextField(null=True, verbose_name='Contenido del post')
    imagen = models.ImageField(upload_to='posts/%Y/%m/%d',null=True, blank=True, verbose_name='Imagen del post')
    fecha_alta = models.DateTimeField(auto_now=True, verbose_name='Fecha de alta')
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    def delete(self, *args, **kwargs):
        if os.path.isfile(self.imagen.path):         
            os.remove(self.imagen.path)
        super(Post, self).delete(*args, **kwargs)
        

    def __str__(self):
        return self.titulo
    
    class Meta:
        db_table = 'posts'
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ['-id']

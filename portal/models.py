from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from cloudinary.models import CloudinaryField


class Categoria(models.Model):
    nombre = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL,
                                null=True,
                                on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return self.nombre

class Noticia(models.Model):
    STATUS_CHOICES = (
        ('pendiente', 'Pendiente'),
        ('publicado', 'Publicado'),
    )
    titulo = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='fecha_publicacion')
    usuario = models.ForeignKey(User,
                                null=True,
                                on_delete=models.SET_NULL)
    categoria = models.ForeignKey(Categoria,
                                unique=False,
                                null=True,
                                on_delete=models.SET_NULL)
    descripcion = models.TextField(null=True)
    nota = models.TextField()
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                            choices=STATUS_CHOICES,
                            default='pendiente')
    img = CloudinaryField('img', null=True)
    class Meta:
        ordering = ('-fecha_publicacion',)

    def __str__(self):
        return self.titulo

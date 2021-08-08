from django.db import models
from django.utils import timezone
from portal.models import Categoria
from users.models import User
from django.conf import settings


class Post(models.Model):
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
    categoria = models.OneToOneField(Categoria,
                                null=True,
                                on_delete=models.CASCADE)
    nota = models.TextField()
    media_url = models.TextField()
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                            choices=STATUS_CHOICES,
                            default='pendiente')
    class Meta:
        ordering = ('-fecha_publicacion',)
    def __str__(self):
        return self.titulo


from django.db import models
from django.conf import settings

class Usuario(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL,
                                    on_delete=models.CASCADE)
    nombre = models.CharField('Nombre', max_length = 255, blank = True, null = True)
    apellido = models.CharField('Apellido', max_length = 255, blank = True, null = True)
    imagen = models.ImageField(upload_to='users/perfil/',
                                blank=True)
    is_admin = models.BooleanField(default = False)
    
    def __str__(self):
        return f'Perfil de usuario {self.usuario.email}'
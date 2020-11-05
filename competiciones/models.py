from django.db import models
from portal.models import Categoria
from django.contrib.auth.models import User

from django.core.validators import MaxValueValidator, MinValueValidator

# Este modulo gestionara las competiciones creadas.

class Competicion(models.Model):
    categoria = models.ForeignKey(Categoria,
                                null=True,
                                on_delete=models.SET_NULL)
    nombre = models.CharField(max_length=250) # Nombre del torneo/competicion
    usuario = models.ForeignKey(User,
                                null=True,
                                on_delete=models.SET_NULL)
    class Meta:
        ordering = ('nombre',)
    def __str__(self):
        return self.nombre

class Fixture(models.Model):
    MODALIDAD_CHOICES = (
        ('partido_unico', 'Partido Unico'),
        ('torneo', 'Torneo'),
        ('playoff', 'Playoff'),
    )
    modalidad = models.CharField(max_length=100,
                            choices=MODALIDAD_CHOICES)
    nombre = models.CharField(max_length=250) # Nombre modalidad o instancia de la competicion
    cantidad_equipos = models.IntegerField(default=3,
                                    validators=[MaxValueValidator(64), MinValueValidator(2)])
    ida_vuelta = models.BooleanField(default=False)
    cantidad_partidos = models.IntegerField(blank=True)
    tabla_posiciones = models.BooleanField(default=False)
    puntos_por_ganados = models.IntegerField(null=True, default=0)
    puntos_por_empate = models.IntegerField(null=True, default=0)
    competicion = models.ForeignKey(Competicion,
                                on_delete=models.CASCADE)

class Equipo(models.Model):
    categoria = models.ForeignKey(Categoria,
                                on_delete=models.CASCADE)
    nombre = models.CharField(max_length=250)

    class Meta:
        ordering = ('nombre',)
    def __str__(self):
        return self.nombre

class Partido(models.Model):
    fixture = models.ForeignKey(Fixture,
                                on_delete=models.CASCADE)
    equipo_local = models.ForeignKey(Equipo,
                                on_delete=models.CASCADE,
                                related_name='local')
    equipo_visitante = models.ForeignKey(Equipo,
                                on_delete=models.CASCADE,
                                related_name='visitante')
    fecha_hora = models.DateTimeField()
    sede = models.TextField()
    goles_local = models.IntegerField(default=0)
    goles_visitante = models.IntegerField(default=0)
    tarjetas_local = models.IntegerField(default=0)
    tarjetas_visitante = models.IntegerField(default=0)

    def __str__(self):
        return self.sede

class Tabla(models.Model):
    fixture = models.ForeignKey(Fixture,
                                on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo,
                                on_delete=models.CASCADE)
    puntos = models.IntegerField(default=0)
    partidos_jugados = models.IntegerField(default=0)
    partidos_ganados = models.IntegerField(default=0)
    partidos_empatados = models.IntegerField(default=0)
    partidos_perdidos = models.IntegerField(default=0)
    goles_a_favor = models.IntegerField(default=0)
    goles_en_contra = models.IntegerField(default=0)

    class Meta:
        ordering = ('puntos',)

class Jugador(models.Model):
    equipo = models.ForeignKey(Equipo,
                                on_delete=models.CASCADE)
    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=250)
    
    class Meta:
        ordering = ('nombre',)
    def __str__(self):
        return self.nombre

class Ranking_Gol(models.Model):
    competicion = models.ForeignKey(Competicion,
                                on_delete=models.CASCADE)
    jugador = models.ForeignKey(Jugador,
                                on_delete=models.CASCADE)
    goles = models.IntegerField(default=0)

    class Meta:
        ordering = ('goles',)
    def __str__(self):
        return self.jugador

class Ranking_Tarjeta(models.Model):
    competicion = models.ForeignKey(Competicion,
                                on_delete=models.CASCADE)
    jugador = models.ForeignKey(Jugador,
                                on_delete=models.CASCADE)
    tarjetas_rojas = models.IntegerField(default=0)
    tarjetas_amarillas = models.IntegerField(default=0)

    def __str__(self):
        return self.jugador
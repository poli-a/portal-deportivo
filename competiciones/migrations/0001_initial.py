# Generated by Django 3.1.2 on 2020-11-03 04:34

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competicion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portal.categoria')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.categoria')),
            ],
            options={
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='Fixture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modalidad', models.CharField(choices=[('partido_unico', 'Partido Unico'), ('torneo', 'Torneo'), ('playoff', 'Playoff')], max_length=100)),
                ('nombre', models.CharField(max_length=250)),
                ('cantidad_equipos', models.IntegerField(default=3, validators=[django.core.validators.MaxValueValidator(64), django.core.validators.MinValueValidator(2)])),
                ('ida_vuelta', models.BooleanField(default=False)),
                ('cantidad_partidos', models.IntegerField(blank=True)),
                ('tabla_posiciones', models.BooleanField(default=False)),
                ('puntos_por_ganados', models.IntegerField(default=3, null=True)),
                ('puntos_por_empate', models.IntegerField(default=1, null=True)),
                ('competicion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competiciones.competicion')),
            ],
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_hora', models.DateTimeField()),
                ('sede', models.TextField()),
                ('goles_local', models.IntegerField(default=0)),
                ('goles_visitante', models.IntegerField(default=0)),
                ('tarjetas_local', models.IntegerField(default=0)),
                ('tarjetas_visitante', models.IntegerField(default=0)),
                ('equipo_local', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='local', to='competiciones.equipo')),
                ('equipo_visitante', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='visitante', to='competiciones.equipo')),
                ('fixture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competiciones.fixture')),
            ],
        ),
    ]

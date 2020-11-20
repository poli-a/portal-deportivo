# Generated by Django 3.1.2 on 2020-11-03 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competiciones', '0004_ranking_gol'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ranking_Tarjeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarjetas_rojas', models.IntegerField(default=0)),
                ('tarjetas_amarillas', models.IntegerField(default=0)),
                ('competicion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competiciones.competicion')),
                ('jugador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competiciones.jugador')),
            ],
        ),
    ]

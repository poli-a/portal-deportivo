# Generated by Django 3.1.3 on 2021-01-16 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_auto_20210111_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]

# Generated by Django 3.1.7 on 2021-02-23 20:11

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_noticia_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='img',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='img'),
        ),
    ]
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contenidos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='foto',
            options={'ordering': ['importancia', '-pub_date']},
        ),
        migrations.AlterModelOptions(
            name='novedad',
            options={'ordering': ['-pub_date'], 'verbose_name_plural': 'novedades'},
        ),
        migrations.AddField(
            model_name='diapositiva',
            name='posicion_imagen',
            field=models.CharField(default=b'bottom', max_length=12, choices=[(b'top', b'Arriba'), (b'center', b'Al centro'), (b'bottom', b'Abajo')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='album',
            name='descripcion',
            field=ckeditor.fields.RichTextField(null=True, blank=True),
        ),
    ]

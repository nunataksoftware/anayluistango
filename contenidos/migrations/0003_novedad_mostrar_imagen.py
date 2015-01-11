# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenidos', '0002_auto_20141010_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='novedad',
            name='mostrar_imagen',
            field=models.BooleanField(default=True, help_text=b'Indicar si la imagen se va a mostrar en la vista detalle'),
            preserve_default=True,
        ),
    ]

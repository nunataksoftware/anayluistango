# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=60, null=True, editable=False, blank=True)),
                ('descripcion', models.TextField(null=True, blank=True)),
                ('pub_date', models.DateTimeField(verbose_name=b'fecha publicada', editable=False)),
            ],
            options={
                'ordering': ['-pub_date'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Diapositiva',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=60, null=True, editable=False, blank=True)),
                ('contenidos', ckeditor.fields.RichTextField(null=True, blank=True)),
                ('importancia', models.IntegerField(default=0)),
                ('imagen', models.ImageField(upload_to=b'diapositivas', verbose_name=b'Imagen')),
            ],
            options={
                'ordering': ['-importancia', 'id'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'fecha publicada', editable=False)),
                ('importancia', models.IntegerField(default=0)),
                ('imagen', models.ImageField(upload_to=b'fotos', verbose_name=b'Imagen')),
                ('album', models.ForeignKey(to='contenidos.Album')),
            ],
            options={
                'ordering': ['-pub_date'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Idioma',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200)),
                ('codigo', models.CharField(max_length=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Novedad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=60, null=True, editable=False, blank=True)),
                ('contenidos', ckeditor.fields.RichTextField(null=True, blank=True)),
                ('pub_date', models.DateTimeField(verbose_name=b'fecha publicada', editable=False)),
                ('imagen', models.ImageField(upload_to=b'noticias', verbose_name=b'Imagen')),
                ('idioma', models.ForeignKey(to='contenidos.Idioma')),
            ],
            options={
                'ordering': ['-pub_date'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pagina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=60, null=True, editable=False, blank=True)),
                ('contenidos', ckeditor.fields.RichTextField(null=True, blank=True)),
                ('idioma', models.ForeignKey(to='contenidos.Idioma')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoDiapositiva',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=60, null=True, editable=False, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='diapositiva',
            name='idioma',
            field=models.ForeignKey(to='contenidos.Idioma'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='diapositiva',
            name='tipo_diapositiva',
            field=models.ForeignKey(to='contenidos.TipoDiapositiva'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='album',
            name='idioma',
            field=models.ForeignKey(to='contenidos.Idioma'),
            preserve_default=True,
        ),
    ]

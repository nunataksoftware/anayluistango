#!env/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from ckeditor.fields import RichTextField
from webanayluis import utilerias
from django.utils.encoding import smart_unicode
from django.utils import timezone
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit, Adjust

from django.core.urlresolvers import reverse

import re


ARRIBA = 'top'
CENTRO = 'center'
ABAJO = 'bottom'
POSICIONES_CHOICES = (
    (ARRIBA, 'Arriba'),
    (CENTRO, 'Al centro'),
    (ABAJO, 'Abajo'),
)

# Create your models here.

class ContenidoManager(models.Manager):

    def all_language(self, language):
        return self.filter(idioma__codigo=language)


class Idioma(models.Model):
    titulo = models.CharField(max_length=200)
    codigo = models.CharField(max_length=5)

    def __unicode__(self):
        return smart_unicode(self.titulo)


class TipoDiapositiva(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(
        max_length=60, blank=True, null=True, editable=False)

    def save(self, **kwargs):
        slug_str = "%s" % (self.titulo)
        utilerias.unique_slugify(self, slug_str)
        super(TipoDiapositiva, self).save(**kwargs)

    def __unicode__(self):
        return smart_unicode(self.titulo)


class Diapositiva(models.Model):



    titulo = models.CharField(max_length=200)
    slug = models.SlugField(
        max_length=60, blank=True, null=True, editable=False)
    contenidos = RichTextField(blank=True, null=True)
    importancia = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='diapositivas', verbose_name='Imagen')
    imagen_miniatura = ImageSpecField(
        processors=[Adjust(sharpness=1.1), ResizeToFill(50, 50)],
        source='imagen',
        format='JPEG')
    imagen_home = ImageSpecField(
        processors=[Adjust(sharpness=1.1), ResizeToFill(2048, 1370)],
        source='imagen',
        format='JPEG')

    posicion_imagen = models.CharField(max_length=12,
                                      choices=POSICIONES_CHOICES,
                                      default=ABAJO)

    tipo_diapositiva = models.ForeignKey(TipoDiapositiva)
    idioma = models.ForeignKey(Idioma)

    objects = ContenidoManager()

    def save(self, **kwargs):
        slug_str = "%s" % (self.titulo)
        utilerias.unique_slugify(self, slug_str)
        super(Diapositiva, self).save(**kwargs)

    def __unicode__(self):
        return smart_unicode(self.titulo)

    class Meta:
        ordering = ['-importancia', 'id']


class Novedad(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(
        max_length=60, blank=True, null=True, editable=False)
    contenidos = RichTextField(blank=True, null=True)
    pub_date = models.DateTimeField('fecha publicada', editable=False)
    imagen = models.ImageField(upload_to='noticias', verbose_name='Imagen')
    imagen_miniatura = ImageSpecField(
        processors=[Adjust(sharpness=1.1), ResizeToFill(50, 50)],
        source='imagen',
        format='JPEG')
    imagen_home = ImageSpecField(
        processors=[Adjust(sharpness=1.1), ResizeToFill(2048, 1370)],
        source='imagen',
        format='JPEG')
    imagen_novedad = ImageSpecField(
        processors=[Adjust(sharpness=1.1), ResizeToFill(368, 256)],
        source='imagen',
        format='JPEG')

    mostrar_imagen = models.BooleanField(default=True, help_text="Indicar si la imagen se va a mostrar en la vista detalle")

    idioma = models.ForeignKey(Idioma)

    objects = ContenidoManager()

    def get_absolute_url(self):

        return reverse('contenido-novedad-detalle', kwargs={'slug': self.slug})

    def save(self, **kwargs):
        slug_str = "%s" % (self.titulo)
        utilerias.unique_slugify(self, slug_str)

        if not self.id:
            self.pub_date = timezone.now()

        super(Novedad, self).save(**kwargs)

    def __unicode__(self):
        return smart_unicode(self.titulo)

    class Meta:
        ordering = ['-pub_date', ]
        verbose_name_plural = u"novedades"


class Album(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(
        max_length=60, blank=True, null=True, editable=False)
    descripcion = RichTextField(blank=True, null=True)
    pub_date = models.DateTimeField('fecha publicada', editable=False)
    idioma = models.ForeignKey(Idioma)

    objects = ContenidoManager()

    def save(self, **kwargs):
        slug_str = "%s" % (self.titulo)
        utilerias.unique_slugify(self, slug_str)

        if not self.id:
            self.pub_date = timezone.now()

        super(Album, self).save(**kwargs)

    class Meta:
        ordering = ['-pub_date', ]


class Foto(models.Model):
    titulo = models.CharField(max_length=200)
    pub_date = models.DateTimeField('fecha publicada', editable=False)
    importancia = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='fotos', verbose_name='Imagen')
    imagen_miniatura = ImageSpecField(
        processors=[Adjust(sharpness=1.1), ResizeToFill(50, 50)],
        source='imagen',
        format='JPEG')
    imagen_home_miniatura = ImageSpecField(
        processors=[Adjust(sharpness=1.1), ResizeToFill(440, 276)],
        source='imagen',
        format='JPEG')
    imagen_home = ImageSpecField(
        processors=[Adjust(sharpness=1.1), ResizeToFit(2048)],
        source='imagen',
        format='JPEG')

    album = models.ForeignKey(Album)

    def save(self, **kwargs):
        if not self.id:
            self.pub_date = timezone.now()

        super(Foto, self).save(**kwargs)

    def __unicode__(self):
        return smart_unicode(self.titulo)

    class Meta:
        ordering = ['importancia', '-pub_date', ]


class Pagina(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(
        max_length=60, blank=True, null=True, editable=False)
    contenidos = RichTextField(blank=True, null=True)
    idioma = models.ForeignKey(Idioma)

    objects = ContenidoManager()

    def get_absolute_url(self):

        return reverse('contenido-pagina-detalle', kwargs={'slug': self.slug})

    def save(self, **kwargs):
        slug_str = "%s" % (self.titulo)
        utilerias.unique_slugify(self, slug_str)

        super(Pagina, self).save(**kwargs)

    def __unicode__(self):
        return smart_unicode(self.titulo)

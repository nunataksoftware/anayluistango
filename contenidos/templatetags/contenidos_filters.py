#!env/bin/python
# -*- coding: utf-8 -*-
from django import template
from contenidos.models import Diapositiva, Novedad, Album
from django.utils import translation
from webanayluis import settings

register = template.Library()


def next(value, arg):
    """ Devuelve el próximo elemento de la lista """
    try:
        return value[int(arg) + 1]
    except:
        return {'slug': 'contenidos-extra'}

register.filter('next', next)

@register.inclusion_tag('contenidos/diapositivas.html')
def diapositivas():

    object_list = Diapositiva.objects.all_language(translation.get_language())

    return {
        'object_list': object_list,
    }

@register.inclusion_tag('contenidos/novedades.html')
def novedades(cantidad=False):

    object_list = Novedad.objects.all_language(translation.get_language())

    if cantidad:
        object_list = object_list[:cantidad]
    return {
        'object_list': object_list,
        'paginado': False,
    }

@register.inclusion_tag('contenidos/fotos.html')
def fotos():

    album = Album.objects.all_language(translation.get_language()).last()

    return {
        'album': album,
    }

@register.inclusion_tag('menu.html')
def menu():

    hay_novedades = Novedad.objects.all_language(translation.get_language()).exists()

    hay_album = Album.objects.all_language(translation.get_language()).exists()

    diapositivas = Diapositiva.objects.all_language(translation.get_language())

    idiomas = settings.LANGUAGES

    return {
        'hay_album': hay_album,
        'hay_novedades': hay_novedades,
        'diapositivas': diapositivas,
        'idiomas': idiomas,
    }

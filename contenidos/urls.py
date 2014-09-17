#!env/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf import settings
from contenidos.views import *
from django.views.generic import ListView
from django.views.generic import DetailView

from contenidos.models import Novedad, Album, Pagina

# Para hacer más brujería como la que hay en las urls, ver
# http://glitterbug.in/blog/django-class-based-generic-views-the-good-the-bad-/show/

urlpatterns = patterns('',
                       url(r'^novedades/((?P<page>\w+)/)?$', ListView.as_view(model=Novedad,
                                                                              paginate_by=settings.PAGINATE_BY), name="contenido-novedad-list"),
                       url(r'^albums/((?P<page>\w+)/)?$', ListView.as_view(model=Album,
                                                                           paginate_by=settings.PAGINATE_BY), name="contenido-album-list"),

                       url(r'^novedad/(?P<slug>[-_\w]+)/$', ExtraDetailView.as_view(
                           model=Novedad, extra_context={
                           }), name="contenido-novedad-detalle"),
                       url(r'^album/(?P<slug>[-_\w]+)/$', ExtraDetailView.as_view(
                           model=Album, extra_context={
                           }), name="contenido-album-detalle"),
                       url(r'^pagina/(?P<slug>[-_\w]+)/$', ExtraDetailView.as_view(
                           model=Pagina, extra_context={
                           }), name="contenido-pagina-detalle"),
                       )

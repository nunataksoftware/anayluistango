from django.shortcuts import render
from django.views import generic

from contenidos.models import Novedad, Album, Pagina

from django.conf import settings

from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

class ExtraContext(object):
    extra_context = {}

    def get_context_data(self, **kwargs):
        context = super(ExtraContext, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context

class ExtraListView(ExtraContext, ListView):
    pass

class ExtraDetailView(ExtraContext, DetailView):
    pass

class ExtraUpdateView(ExtraContext, UpdateView):
    pass

class ExtraCreateView(ExtraContext, CreateView):
    pass 

class ExtraDeleteView(ExtraContext, DeleteView):
    pass

class ExtraCloneView(ExtraUpdateView):
    def post(self, request, *args, **kwargs):
       return ExtraCreateView.as_view(model=self.model,
                              template_name=self.template_name,
                              extra_context=self.extra_context)(request, *args, **kwargs) 

from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView
from django.db import transaction

from Synthetica.models import *
from Synthetica.forms import *
# from django.http import HttpResponse, HttpResponseRedirect
# from django.urls import reverse, reverse_lazy
# from django.urls import reverse

# from django.forms import modelformset_factory, inlineformset_factory

# from django.shortcuts import get_object_or_404



def index(request):
    return render(request, 'index.html')


class ProjectDetailView(generic.DetailView):
    model = Project


class GenerateDetailView(generic.DetailView):
    model = Generate


class ProjectGenerateCreate(CreateView):
    model = Project
    fields = ['project_name', 'description', 'records']

    def get_context_data(self, **kwargs):
        data = super(ProjectGenerateCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['generate'] = GenerateFormSet(self.request.POST)
        else:
            data['generate'] = GenerateFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        generate = context['generate']
        with transaction.atomic():
            self.object = form.save()
            if generate.is_valid():
                generate.instance = self.object
                generate.save()
        return super(ProjectGenerateCreate, self).form_valid(form)
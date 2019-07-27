from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView
from django.db import transaction
from django.shortcuts import get_object_or_404

from .models import *
from .forms import *
from . import artificial



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


def generate(request, pk):
    project_instance = get_object_or_404(Project, pk=pk)
    records = project_instance.records
    where = Generate.objects.filter(project_id = project_instance).values_list('data_type', 'field_name', 'options')
    field_data = list(where)
    meta_data = []
    for val in field_data: 
        convert = list(val)
        meta_data.append(convert)
    syn = artificial.generate(records, meta_data)
    context = {
        'showtable':syn
    }
    return render(request, 'generation.html', context)
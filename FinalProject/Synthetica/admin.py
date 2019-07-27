from django.contrib import admin
from .models import *



@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'description', 'records')


@admin.register(Generate)
class GenerateAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_id', 'data_type','field_name', 'options')
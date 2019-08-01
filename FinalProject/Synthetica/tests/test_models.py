from django.test import TestCase
from Synthetica.models import *


class ProjectModelTest(TestCase):
    @classmethod

    def setUpTestData(cls):
        Project.objects.create(project_name="Test1", description="this a test on the model", records="100")

    def test_project_name_label(self):
        project = Project.objects.get(id=1)
        field_label = project._meta.get_field('project_name').verbose_name
        self.assertEquals(field_label, 'Project Name:')

    def test_description_label(self):
        project = Project.objects.get(id=1)
        field_label = project._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'Project Description:')

    def test_records_label(self):
        project = Project.objects.get(id=1)
        field_label = project._meta.get_field('records').verbose_name
        self.assertEquals(field_label, 'No. Of Records:')

    def test_get_absolute_url(self):
        project = Project.objects.get(id=1)
        self.assertEquals(project.get_absolute_url(), '/synthetica/generate/1')



class GenerateModelTest(TestCase):
    @classmethod

    def setUpTestData(cls):
        project = Project.objects.create(project_name="Test2", description="this tests with a primary key", records="200")
        Generate.objects.create(project_id=project,data_type="famrel", field_name="Family Relationships", options="1,4")

    def test_project_id_label(self):
        generate = Generate.objects.get(id=1)
        field_label = generate._meta.get_field('data_type').verbose_name
        self.assertEquals(field_label, 'Data Type')
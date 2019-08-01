from django.test import TestCase
from django.urls import reverse
from Synthetica.models import *


class ProjectGenerateCreateTest(TestCase):
    @classmethod

    def setUpTestData(cls):
        project = Project.objects.create(project_name="Test2", description="this tests with a primary key", records="200")
        Generate.objects.create(project_id=project,data_type="famrel", field_name="Family Relationships", options="1,4")

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('synthetica/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('generate'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'generation.html')

    def test_workspace_view_url_accessible_by_name(self):
        response = self.client.get(reverse('workspace'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, '/synthetica/project_form.html')
"""
from django.urls import reverse
from budget.models import project, Category, Expense
import json



class TestViews(TestCase):

    def setUp(self):
        self.client Client()
        self.list_url = reverse('list')

    def test_project_list_GET(self):
        respose = client.get(reverse(self.list_url))

        self.assertExuals(respose.status_code, 200)
        self.assertTemplateUsed(response, 'budget/project-list.html')

    def test_project_list
        test_project_list_GET
"""
from django.test import TestCase, client
from django.urls import reverse
from budget.models import Project,


class TestViews(TestCase):

    def test_project_list_GET(self):
        response = Client()

        response = client.get(reverse('list'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 900)

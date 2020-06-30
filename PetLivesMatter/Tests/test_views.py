from django.test import TestCase, client
from django.urls import reverse
from budget.models import Project,


class TestViews(TestCase):

    def test_project_list_GET(self):
        response = Client()

        response = client.get(reverse('list'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 900)

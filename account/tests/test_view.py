from django.test import TestCase, Client
from django.urls import reverse, resolve
from account.views import project_list
from account.models import *
import json


class TestViews(TestCase):
    def test_language_preference(self):
        response = reverse('list')
        print(resolve(response))
        self.assertEquals(resolve(response).func, project_list)

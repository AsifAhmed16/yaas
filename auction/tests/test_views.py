from django.test import TestCase, Client
from django.urls import reverse
from auction.models import *
import json


class TestViews(TestCase):
    def test_language_preference(self):
        client = Client()
        response = client.get(reverse('auction_browse'))
        self.assertEquals(response.status_code, 200)

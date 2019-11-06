from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('list')
        self.auc_url = reverse('auction_add')

    def test_language_store(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)

    def test_add_auction(self):
        response = self.client.get(self.auc_url)
        self.assertEquals(response.status_code, 302)

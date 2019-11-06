from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.bid_url = reverse('auction:auction_bid', args=[1])

    def test_bid_auction(self):
        response = self.client.get(self.bid_url)
        self.assertEquals(response.status_code, 302)

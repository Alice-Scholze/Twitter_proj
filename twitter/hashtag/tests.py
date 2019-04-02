from django.test import TestCase
from django.test.client import Client
from .views import instantiate_twitter, search_tweets, home


class HomeViewTest(TestCase):
    def test_instantiate_twitter(self):
        twitter = instantiate_twitter('ph1qcmgTRpAQbR9QYIQ3njL6u', 'vOR2XPM8HKZ1wNxC7QbVFZ3lMvfXsrd1hPwg9Z4d6fsPqsgAkq', '1108492892526600192-PEK9wbvbjBV4eu4AfLj5USPd6R9RFK', 'TwAMBTeErr2ZTvoKlkWwzV9CXGvtNAHaEzKeFOHWBBbnj')
        self.assertTrue(twitter)

    def test_search_tweets(self):
        tweets = search_tweets('#dog')
        self.assertGreater(len(tweets), 0)

    def test_home(self):
        client = Client()
        response = client.get(path=home)
        self.assertEqual(response.status_code, 200)
from django.test import TestCase
from django.test.client import Client
from .views import instantiate_twitter, search_tweets, home
from twitter.twitter.settings import consummer_key, consummer_secret, acess_key, acess_secret

class HomeViewTest(TestCase):
    def test_instantiate_twitter(self):
        twitter = instantiate_twitter(consummer_key, consummer_secret, acess_key, acess_secret)
        self.assertTrue(twitter)

    def test_search_tweets(self):
        tweets = search_tweets('#dog')
        self.assertGreater(len(tweets), 0)

    def test_home(self):
        client = Client()
        response = client.get(path=home)
        self.assertEqual(response.status_code, 200)
from django.shortcuts import render
from .models import Hashtag

import tweepy

def home(request):
    twitter = instanciate_twitter('ph1qcmgTRpAQbR9QYIQ3njL6u', 'vOR2XPM8HKZ1wNxC7QbVFZ3lMvfXsrd1hPwg9Z4d6fsPqsgAkq', '1108492892526600192-PEK9wbvbjBV4eu4AfLj5USPd6R9RFK', 'TwAMBTeErr2ZTvoKlkWwzV9CXGvtNAHaEzKeFOHWBBbnj')

    hashtags = Hashtag.objects.all().order_by('-hashtag')
    resultados = None

    for hashtag in hashtags:
        if resultados is None:
            resultados = twitter.search(q=hashtag.hashtag)
        else:
            resultados = resultados + twitter.search(q=hashtag.hashtag)
    return render(request, 'home.html', {'resultados': resultados, 'hashtags': hashtags})

def instanciate_twitter(consummer_key, consummer_secret, acess_key, acess_secret):
    autenticacao = tweepy.OAuthHandler(consummer_key, consummer_secret)
    autenticacao.set_access_token(acess_key, acess_secret)
    return tweepy.API(autenticacao)
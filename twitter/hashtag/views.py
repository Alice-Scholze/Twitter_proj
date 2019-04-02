from django.shortcuts import render
from .models import Hashtag
import tweepy

def home(request):
    filter = request.GET.get('order')
    if not filter:
        hashtags = Hashtag.objects.all()
    else:
        hashtags = Hashtag.objects.filter(pk=int(filter))
    resultados = None
    for hashtag in hashtags:
        if resultados is None:
            resultados = search_tweets(hashtag.hashtag)
        else:
            resultados = resultados + search_tweets(hashtag.hashtag)
    hashtags = Hashtag.objects.all()
    context = {
        'resultados': resultados,
        'hashtags': hashtags
    }
    return render(request, 'home.html', context)

def instantiate_twitter(consummer_key, consummer_secret, acess_key, acess_secret):
    autenticacao = tweepy.OAuthHandler(consummer_key, consummer_secret)
    autenticacao.set_access_token(acess_key, acess_secret)
    return tweepy.API(autenticacao)

def search_tweets(text):
    twitter = instantiate_twitter('ph1qcmgTRpAQbR9QYIQ3njL6u', 'vOR2XPM8HKZ1wNxC7QbVFZ3lMvfXsrd1hPwg9Z4d6fsPqsgAkq', '1108492892526600192-PEK9wbvbjBV4eu4AfLj5USPd6R9RFK', 'TwAMBTeErr2ZTvoKlkWwzV9CXGvtNAHaEzKeFOHWBBbnj')
    return twitter.search(q=text)

def search(request):
    hashtags = Hashtag.objects.all()
    resultados = None
    for hashtag in hashtags:
        if resultados is None:
            resultados = search_tweets(hashtag.hashtag)
        else:
            resultados = resultados + search_tweets(hashtag.hashtag)
    context = {
        'resultados': resultados,
        'hashtags': hashtags
    }
    return render(request, 'home.html', context, {'filter': hashtags})
    #return render(request, 'home.html'), {'filter': user_filter}
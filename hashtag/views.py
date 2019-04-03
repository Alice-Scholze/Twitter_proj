from django.shortcuts import render
from .models import Hashtag
import tweepy
from twitter.settings import consummer_key, consummer_secret, acess_key, acess_secret

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
    twitter = instantiate_twitter(consummer_key, consummer_secret, acess_key, acess_secret)
    return twitter.search(q=text)
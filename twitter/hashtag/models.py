from django.db import models

class Hashtag(models.Model):
    hashtag = models.CharField('Hashtag', max_length=100)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.hashtag

    #@models.permalink
    #def get_absolute_url(self):
    #    return ('home', (), {'hashtag': self.hashtag})
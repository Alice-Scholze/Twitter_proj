from django.urls import path
from .views import home, teste

urlpatterns = [
    path('', home),
    path('teste/', teste),
]
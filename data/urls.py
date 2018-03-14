from django.conf.urls import url
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^$', views.ask, name='ask'),
    url(r'^res/?$', views.res, name='res'),
]
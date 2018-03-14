from django.conf.urls import include, url
from django.conf import settings
from tastypie.api import Api
from .api import SurveyResource
from . import views


api = Api(api_name='api')
api.register(SurveyResource())

urlpatterns = [
    url(r'^$', views.ask, name='ask'),
    url(r'^res/?$', views.res, name='res'),
    url(r'^', include(api.urls)),
]
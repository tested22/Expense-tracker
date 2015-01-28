from django.views.generic import TemplateView
from django.conf.urls import patterns, url

from .views import Register

urlpatterns = patterns('',
    url(r'^$', Register.as_view(), name='rest_register'))



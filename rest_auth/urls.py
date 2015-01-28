from django.conf.urls import patterns, url

from rest_auth.views import (Login, Logout)

urlpatterns = patterns('',
    url(r'^login/$', Login.as_view(), name='rest_login'),
    url(r'^logout/$', Logout.as_view(), name='rest_logout'),
)

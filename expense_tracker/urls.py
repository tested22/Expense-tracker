from views import *
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="home.html"), name='home'),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^account/', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

router = DefaultRouter()
router.register(r'expense', ExpenseViewSet, base_name='expense')
router.register(r'by_week', WeeklyViewSet, base_name='by_week')

urlpatterns += patterns('',
    url(r'^api/', include(router.urls, namespace='api')),
)

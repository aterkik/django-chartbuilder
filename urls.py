from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'django_chartbuilder.views.home', name='home'),
)

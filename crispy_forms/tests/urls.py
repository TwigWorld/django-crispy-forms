import django

if django.VERSION >= (1, 5):
    from django.conf.urls import patterns, url
else:
    from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^simple/action/$', 'simpleAction', name = 'simpleAction'),
)

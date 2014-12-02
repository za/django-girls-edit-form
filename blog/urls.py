from django.conf.urls import patterns, include, url
from blog import views

urlpatterns = patterns('', 

    url(r'^posts/$', views.posts, name='posts'),
    url(r'^post/new$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
)

# coding=utf-8
from django.conf.urls import url, include
from . import views
import sys
reload(sys)
sys.setdefaultencoding('utf8')

app_name = 'elections'
urlpatterns = [
    url(r'^$', views.index),
    url(r'^areas/(?P<area>.+)/$', views.areas),
    url(r'^areas/(?P<area>.+)/results$', views.results),
    url(r'^polls/(?P<poll_id>\d+)$', views.polls),
]

# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from tracker import views

urlpatterns = patterns('tracker.views',
    url(r'^new_char/$', views.CharacterCreateView.as_view(), name='new_char'),
    url(r'^chars/$', 'my_chars', name='my_chars'),
    url(r'^del_char/(?P<char_id>\d+)/$', 'rm_char', name='rm_char'),
    url(r'^tracked/$', 'tracked_items', name='tracked_items'),
)

# -*- coding: utf-8 -*-
# @Time    : 2019-06-29 19:00
# @Author  : Olex
# @File    : urls.py
# @Software: PyCharm

# !/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__Olex__'
from django.urls import path

from zanhu.news import views

app_name = "news"

urlpatterns = [
    path('', views.NewsListView.as_view(), name='list'),
    path('post-news/', views.post_news, name='post_news'),
    path('delete/<pk>/', views.NewsDeleteView.as_view(), name='delete_news'),
    path('like/', views.like, name='like_post'),
    path('get-thread/', views.get_thread, name='get_thread'),
    path('post-comment/', views.post_comment, name='post_comments'),
]
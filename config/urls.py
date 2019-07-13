#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__Olex__'
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
# from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from zanhu.news.views import NewsListView

urlpatterns = [

                  path('', NewsListView.as_view(), name='home'),

                  # 第三方应用
                  path('markdownx/', include('markdownx.urls')),
                  path('comments/', include('django_comments.urls')),

                  # Django Admin, use {% url 'admin:index' %}
                  # path(settings.ADMIN_URL, admin.site.urls),
                  # User management
                  path("users/", include("zanhu.users.urls", namespace="users")),
                  path("accounts/", include("allauth.urls")),
                  path('search/', include('haystack.urls')),

                  # Your stuff: custom urls includes go here
                  path('news/', include('zanhu.news.urls', namespace='news')),
                  path('articles/', include('zanhu.articles.urls', namespace='articles')),
                  path('qa/', include('zanhu.qa.urls', namespace='qa')),
                  path('messages/', include('zanhu.messager.urls', namespace='messages')),
                  path('notifications/', include('zanhu.notifications.urls', namespace='notifications')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns

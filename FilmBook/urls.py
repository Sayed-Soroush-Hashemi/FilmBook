"""FilmBook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

import users.urls

urlpatterns = [
    url(r'^accounts/', include(users.urls), name='users_urls'),

    # url(r'^user/(\d+)', 'film_book.views.show_profile'),
    url(r'^movie/(\d+)', 'film_book.views.show_movie'),
    url(r'^post/(\d+)', 'film_book.views.show_post'),

    url(r'^admin/', include(admin.site.urls)),
]

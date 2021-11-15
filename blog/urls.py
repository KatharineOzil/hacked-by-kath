from django.urls import path
from django.conf.urls import include
from django.contrib import admin
from . import views

urlpatterns = [
   #path('', views.index, name='index'),
   #path(r'archive', views.archive, name='archive'),
   path('', views.archive, name='index'),
   path(r'article/(?P<id>\d+)/$', views.detail, name='detail'),
   path(r'aboutme', views.aboutme, name='aboutme'),
   path(r'404', views.page_not_found, name='404')
]


"""Katharine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles
from django.conf import settings
from django.conf.urls.static import static
from blog import views
from django.conf.urls import handler404, handler500
from django.conf.urls import url
from django.views import static

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'', include('blog.urls')),
    path(r'mdeditor/', include('mdeditor.urls')),
    url(r'^static/(?P<path>.*)$', static.serve,
      {'document_root': settings.STATIC_ROOT}, name='static'),
    url(r'^media/(?P<path>.*)$', static.serve,
      {'document_root': settings.MEDIA_ROOT}, name='media'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

handler404 = 'blog.views.page_not_found'
handler403 = 'blog.views.page_forbidden'
handler500 = 'blog.views.server_error'
handler502 = 'blog.views.bad_gateway'


"""quickpython URL Configuration

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
from django.conf.urls import patterns,include, url
from django.contrib import admin
import blog.views
import settings

urlpatterns=patterns('django.contrib.flatpages.views',
url(r'^admin/', include(admin.site.urls)),
url(r'^$', blog.views.mainindex),
url('^blog/',blog.views.main),
url('^post/(\d+)/$',blog.views.post),
url('^comment/(\d+)/$',blog.views.add_comment),
url('^msg/',blog.views.msg),
url('^contact/(\d+)/$',blog.views.addcontact),
url('^pages/',include('django.contrib.flatpages.urls')),
url('^reg/',blog.views.newreg),

)

urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )


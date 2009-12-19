from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from cloudwich.views import albums, album, photo, posts, post, index, about

urlpatterns = patterns('',
    # Example:
    # (r'^foo/', include('foo.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),

    # displays all our albums
    (r'^albums/$', albums),

    # single album with id passed in
    (r'^album/(\d+)/.*$', album),

    # single photo
    (r'^photo/(\d+)/(\d+)$', photo),

    # all posts
    (r'^posts/$', posts),

    # single post
    (r'^post/(\d+)/.*$', post),

    # index page
    (r'^$', index),
  
    # about page
    (r'^about$', about)
)

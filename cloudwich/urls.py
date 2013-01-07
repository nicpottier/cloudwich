from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from cloudwich.views import albums, album, photo, posts, post, index, about, clear, posts_tagged

urlpatterns = patterns('',
    # displays all our albums
    (r'^albums/$', albums),

    # single album with id passed in
    (r'^album/(\d+)/.*$', album),

    # single photo
    (r'^photo/(\d+)/(\d+)$', photo),

    # all posts with tag
    (r'^posts/tag/(\w+)$', posts_tagged),

    # all posts
    (r'^posts/$', posts),

    # single post
    (r'^post/(\d+)/.*$', post),

    # index page
    (r'^$', index),
  
    # about page
    (r'^about$', about),

    # clears our cache, displays index
    (r'^clear$', clear)
)

from django.shortcuts import render
from django.conf import settings

from cloudwich import picasa
from cloudwich import tumbler
from cloudwich import facebook

def albums(request):
    albums = picasa.get_albums(settings.PICASA_USER)
    return render(request, 'albums.html', locals())

def album(request, albumId):
    album = picasa.get_album(settings.PICASA_USER, albumId)
    return render(request, 'album.html', locals())

def photo(request, albumId, photoId):
    photo = picasa.get_photo(settings.PICASA_USER, albumId, photoId)
    return render(request, 'photo.html', locals())

def posts(request):
    posts = tumbler.get_posts(settings.TUMBLR_USER, settings.DISQUS_FORUM_NAME)
    return render(request, 'posts.html', locals())

def posts_tagged(request, tag):
    posts = tumbler.get_posts(settings.TUMBLR_USER, settings.DISQUS_FORUM_NAME, tag)
    return render(request, 'posts_tagged.html', locals())

def post(request, postId):
    post = tumbler.get_post(settings.TUMBLR_USER, postId)
    disqus_forum = settings.DISQUS_FORUM_NAME;
    return render(request, 'post.html', locals())

def index(request):
    posts = tumbler.get_home_posts(settings.TUMBLR_USER, settings.DISQUS_FORUM_NAME)
    albums = picasa.get_home_albums(settings.PICASA_USER)
    statuses =  facebook.get_status_feed(settings.FACEBOOK_USER_ID, settings.FACEBOOK_KEY)
    return render(request, 'index.html', locals())

def clear(request):
    tumbler.clear_cache()
    picasa.clear_cache()
    facebook.clear_cache()
    return index(request)

def about(request):
    return render(request, 'about.html', locals())

    
    
    

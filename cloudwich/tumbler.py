import requests
from datetime import datetime 
import re

from django.core.cache import cache
from django.conf import settings

POSTS_URL = 'http://api.tumblr.com/v2/blog/%s.tumblr.com/posts?api_key=%s'
POST_URL = 'http://api.tumblr.com/v2/blog/%s.tumblr.com/posts?api_key=%s&id=%s'

class Post:
    def __init__(self, entry):
        self.type = entry['type']
        self.title = entry.get('title', '')
        self.url = entry['short_url']
        self.date = datetime.utcfromtimestamp(entry['timestamp'])
        self.id = entry['id']

        if (entry.has_key('tags')):
            self.tags = entry['tags']

        if self.type == 'link':
            self.link = entry['url']
            self.body = entry['description']
        elif self.type == 'text':
            self.body = entry['body']
        elif self.type == 'video':
            self.player = entry['player'][1]
            self.body = entry['caption']
        elif self.type == 'photo':
            self.body = entry['caption']
            self.src = entry['photos'][0]['original_size']['url']

def get_post(username, postId):
    url = POST_URL % (username, settings.TUMBLR_API_KEY, postId)
    r = requests.get(url)
    post = None

    if r.status_code == 200:
        blob = r.json()

        for post_json in blob['response']['posts']:
            post = Post(post_json)
            
    return post

def clear_cache():
    cache.delete('posts')

def get_posts(username, forumName=None, tag=None):
    if not tag:
        key = 'posts'
    else:
        key = 'posts_%s' % tag

    posts = cache.get(key)
    posts = []
        
    if not posts:
        url = POSTS_URL % (username, settings.TUMBLR_API_KEY)
        r = requests.get(url)

        if r.status_code == 200:
            blob = r.json()

            for post_json in blob['response']['posts']:
                post = Post(post_json)
                posts.append(post)
                
            cache.set(key, posts)

    return posts

def get_home_posts(username, forumName):
    return get_posts(username, forumName)



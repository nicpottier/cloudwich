from tumblr import Api
import urllib
import re

class Post:
    def __init__(self, entry):
        self.type = entry['type']
        self.url = entry['url']
        self.date = entry['date']
        self.id = entry['id']

        if self.type == 'link':
            self.link = entry['link-url']
            self.body = entry['link-description']
            self.title = entry['link-text']
        elif self.type == 'regular':
            self.body = entry['regular-body']
            self.title = entry['regular-title']
        elif self.type == 'video':
            self.player = entry['video-player']
            self.body = entry['video-caption']

def get_post(username, postId):
    api = Api('%s.tumblr.com' % username)
    entry = api.read(postId)

    return Post(entry)

def get_posts(username, forumName=None):
    api = Api('%s.tumblr.com' % username)
    iter = api.read()

    query = "?"
    i=0
    posts = []
    for item in iter:
        post = Post(item)
        posts.append(post)
        query = '%surl%d=%s&' % (query, i, urllib.quote(post.url))
        i = i+1

    # grab our number of comments if appropraite
    if forumName:
        f = urllib.urlopen('http://disqus.com/forums/%s/get_num_replies.js%s' % (forumName, query))
        result = f.read()

        # find our actual number of replies
        #    var num_replies = '0,0,0'
        m = re.search("var num_replies = '(.*?)'", result)
        if m:
            counts = m.group(1).split(',')
            i = 0
            for post in posts:
                post.comment_count = counts[i]
                i = i+1

    return posts

def get_home_posts(username, forumName):
    return get_posts(username, forumName)



import feedparser
from datetime import datetime
from django.core.cache import cache

class Status:
    def __init__(self, entry):
        self.status = entry['title']
        # Mon, 14 Dec 2009 14:05:47 -0800
        self.date = datetime.strptime(entry['updated'], '%a, %d %b %Y %H:%M:%S -0800')

def clear_cache():
    cache.delete('facebook')

def get_status_feed(userId, key):
    feed = cache.get('facebook')

    if not feed:
        d = feedparser.parse('http://www.facebook.com/feeds/status.php?id=%s&viewer=%s&key=%s&format=rss20' %
                             (userId, userId, key))
        feed = []
        for entry in d['entries']:
            feed.append(Status(entry))

        cache.set('facebook', feed)

    return feed
     

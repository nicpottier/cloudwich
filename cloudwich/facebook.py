import feedparser
from datetime import datetime
from django.core.cache import cache
import re

class Status:
    def __init__(self, entry):
        self.status = entry['title']
        # Mon, 14 Dec 2009 14:05:47 -0800
        # Thu, 18 Mar 2010 15:08:34 -0700
        m = re.search('^(.*) -\d\d\d\d$', entry['updated'])
        if m:
            self.date = datetime.strptime(m.group(1), '%a, %d %b %Y %H:%M:%S')

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
     

import gdata.photos.service
import gdata.media
import gdata.geo

class Album:
    def __init__(self, entry, albumId=None):
        self.title = entry.title.text
        self.url = entry.GetHtmlLink()
        self.date = entry.timestamp.datetime
        if (albumId):
            self.id = albumId
            self.description = entry.subtitle.text
        else:
            self.id = entry.GetAlbumId()
            if (entry.media.thumbnail.count > 0):
                self.thumb = entry.media.thumbnail[0].url

class Photo:
    def __init__(self, entry=None):
        if not entry:
            return

        if (entry.media.thumbnail.count > 0):
            self.thumb = entry.media.thumbnail[0].url
            
        self.id = entry.gphoto_id.text


def get_picasa_feed(path):
    gd_client = gdata.photos.service.PhotosService()
    return gd_client.GetFeed(path)

def get_home_albums(user):
    feed = get_picasa_feed('/data/feed/api/user/%s?kind=album&thumbsize=160c' % user)
    albums = []
    for entry in feed.entry[:4]:
        albums.append(Album(entry))

    return albums

def get_albums(user):
    feed = get_picasa_feed('/data/feed/api/user/%s?kind=album&max-results=100&thumbsize=144c' % user)
    albums = []
    for entry in feed.entry:
        albums.append(Album(entry))

    return albums

def get_album(user, albumId):
    feed = get_picasa_feed('/data/feed/api/user/%s/albumid/%s?kind=photo&thumbsize=104c' %
                           (user, albumId));
    album = Album(feed, albumId)
    album.thumb = feed.icon.text
    photos = []
    for entry in feed.entry:
        photos.append(Photo(entry))

    album.photos = photos
    return album

def get_photo(user, albumId, photoId):
    feed = get_picasa_feed('/data/feed/api/user/%s/albumid/%s/photoid/%s?imgmax=576' %
                              (user, albumId, photoId));

    photo = Photo()
    photo.url = feed.media.content[0].url;
    photo.id = feed.gphoto_id
    photo.caption = feed.subtitle.text

    photo.album = get_album(user, albumId)

    return photo

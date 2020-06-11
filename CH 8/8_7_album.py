# Thus block of code calls a function using a default
# an f-string is used.
print()
def make_album(name, album_title, tracks =''):
    """Return a dictionary with the album information"""
    album_info = {'artist_name' : name.title(), 'album' : album_title.title()}
    if tracks:
        album_info['tracks'] = tracks
    return album_info

album = make_album('slave', 'slide', tracks=10)
print(album)
album = make_album('incognito', 'tribes, vibes, and scribes')
print(album)
album = make_album('ray obiedo', 'zulaya')
print(album)
print()

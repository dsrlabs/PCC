print()
def make_album(artist_name, album_title):
    """Return a dictionary with the album information"""
    album_info = {'artist_name' : artist_name.title(), 'album' : album_title.title()}
    return album_info

print("\nPlease enter the artist name:")
print("Please enter the album title:")

print("[enter 'q' at any time to quit]")
print()
while True:
    artist_name = input("Artist Name: ")
    if artist_name == 'q':
        break
    
    album_title = input("Album Title: ")
    if album_title == 'q':
        break

    album_data = make_album(artist_name, album_title)
    print(album_data)
    print()

def tracklist(**kwargs):
    for artist, album in kwargs.items():
        print(artist)
        for key, value in album.items():
            print(f'ALBUM: {key} TRACK: {value}')

# C8-08 p.146 see page for project

def make_album(artist, title, tracks=''):

    created_album = {}

    if tracks:

        created_album['Artist'] = artist
        created_album['Title'] = title
        created_album['Tracks'] = tracks

    else:
        created_album['Artist'] = artist
        created_album['Title'] = title

    for k, v in created_album.items():
        if k == 'Artist':
            print(f'The {k.lower()} who created the album is {v}.')

        elif k == 'Title':
            print(f'The {k.lower()} of the album was {v.title()}.')

        else:
            print(f'The album featured {v} {k.lower()}.')

active = True

tracks = ''

while active:

    artist = input('Enter the name of one of your favorite musicians. (press "q" at any time to quit)\n')
    if artist == 'q':
        break

    album = input (f'Enter the name of an album by {artist}.\n')
    if album == 'q':
        break

    know_tracks = input('Do you know how many tracks were on that album? (y/n)\n')

    if know_tracks == 'q':
        break

    elif know_tracks.lower() == 'y':

        tracks = input('How many tracks were on the album?\n')

    elif know_tracks.lower() == 'n':

        print('That is all right!')

    if tracks:

        make_album(artist, album, tracks)

    else:
        make_album(artist, album)

    contloop = input('again?(y/n): ')

    if contloop == 'n':
        active = False

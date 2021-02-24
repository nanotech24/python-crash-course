# C8-07 p.146 See page for instruction

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


make_album('ASG', 'Win Us Over', '13')

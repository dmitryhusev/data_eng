import pandas as pd
from extract import extract


def transform():
    raw_tracks = extract()
    tracks =[]
    for track in raw_tracks:
        records = {}
        if track.get('@attr'):
            continue
        records['artist'] = track['artist']['#text']
        records['song'] = track['name']
        records['date'] = track.get('date').get('#text')
        records['unix_date'] = track.get('date').get('uts')
        tracks.append(records)
    return tracks

pd_data = pd.DataFrame(transform())

print(pd_data)

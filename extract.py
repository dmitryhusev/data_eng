import os
import requests


def extract():
    api_key = os.getenv('LASTFM_API_KEY')
    url = f'http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=leverkun&api_key={api_key}&format=json'
    tracks = requests.get(url).json()['recenttracks']['track']
    return tracks

import os
import sys
import spotipy
import spotipy.util as util
import time
import collections

os.environ['SPOTIPY_CLIENT_ID'] = '###'
os.environ['SPOTIPY_CLIENT_SECRET'] = '###'

scope = 'playlist-modify-public'
username = '###'
token = util.prompt_for_user_token(username, scope, redirect_uri = 'https://example.com/callback/')
sp = spotipy.Spotify(auth=token)
playlists = sp.user_playlists(username)
playlist_id = playlists['items'][0]['id']
songList = []

# Obtain all songs from my playlist
for i in range(0, 30):
	tracks = sp.user_playlist_tracks(username, playlist_id=playlist_id, limit=100, offset=i*100)
	items = tracks['items']

	for item in items:
		track = item['track']
		artist = track['artists'][0]['name']
		song = track['name']
		track_id = track['id']
		songList.append([artist + ' ' + song, track_id])
	time.sleep(0.2)

# Check duplicate songs
seenBefore = []
songsToRemove = []

for song in songList:
	if song[0] in seenBefore:
		songsToRemove.append(song[1])
	seenBefore.append(song[0])

amountRemoved = len(songsToRemove)
print(str(amountRemoved) + ' duplicate songs have been removed from your playlist.')

# Remove duplicate songs
sp.user_playlist_remove_all_occurrences_of_tracks(username, playlist_id, songsToRemove)

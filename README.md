### Spotify Playlist Deduplicator

Sometimes, in a Spotify playlist, duplicate songs can occur.
Spotify should be able to automatically detect those duplicates. However, sometimes it misses a duplicate, because there are multiple editions of a single song,
eg. an album version and a single version. These editions are often identical, meaning it has no value to have both versions in a single playlist.
Therefore I decided to automate the process of deduplicating a playlist myself.
A Spotify developer account is needed to make it work. This is really easy to obtain: https://developer.spotify.com/dashboard/

Simply fill in the credentials in the Python script and run:

```bash
python3 spotifyDeduplicate.py
```

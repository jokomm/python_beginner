import os
from googleapiclient.discovery import build

api_key = "AIzaSyCdsEz59KmuCGP9Hc5zfyOq6xRXRU23GZM"

youtube = build('youtube', 'v3', developerKey=api_key)

playlist_id = 'PLbpi6ZahtOH6T-6wzWaw5e-zAkYSzSvpN'


request = youtube.playlistItems().list(
    part='snippet',
    playlistId=playlist_id,
    maxResults=50,
)

playlist_items = []
while request is not None:
    response = request.execute()
    playlist_items += response["items"]
    request = youtube.playlistItems().list_next(request, response)


print([f'https://www.youtube.com/watch?v={t["snippet"]["resourceId"]["videoId"]}&list={playlist_id}&t=0s' for t in playlist_items])
print(f"total: {len(playlist_items)}")
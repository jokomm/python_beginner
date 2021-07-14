"""Google API."""

from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
range_name = 'A1:E2'


def get_links_from_spreadsheet(id: str, token: str) -> list:
    """Should get a list of strings from the first column of a Google Spreadsheet with the given ID."""
    """Shows basic usage of the Sheets API.
        Prints values from a sample spreadsheet.
        """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=id,
                                range=range_name).execute()
    values = result.get('values', [])

    return [value[0] for value in values]


def get_links_from_playlist(link: str, developer_key: str) -> list:
    """Should get a list of links to songs in the Youtube playlist with the given address."""
    playlist_id = link.replace("https://www.youtube.com/playlist?list=", "")
    youtube = build('youtube', 'v3', developerKey=developer_key)

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

    return [f'https://www.youtube.com/watch?v={t["snippet"]["resourceId"]["videoId"]}&list={playlist_id}&t=0s' for t in playlist_items]


# https://stackoverflow.com/questions/62345198/extract-individual-links-from-a-single-youtube-playlist-link-using-python
# https://www.youtube.com/watch?v=IK5UUrPglTM
# https://www.youtube.com/watch?v=1KO_HZtHOWI
# https://stackoverflow.com/questions/30653208/retrieve-video-ids-contained-in-a-playlist-youtube-api-v3
# https://stackoverflow.com/questions/62347194/youtube-api-get-all-playlist-id-from-a-channel-python

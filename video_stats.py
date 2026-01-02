import requests
import json
import os

from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")
API_KEY = os.getenv('API_KEY')
CHANNEL_HANDLE = "MrBeast"

def get_playlist_id():
    try: 

        URL = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}"

        response = requests.get(URL)

        response.raise_for_status()

        data = response.json()

        channel_playlistId = data['items'][0]['contentDetails']['relatedPlaylists']['uploads']

        # print(channel_playlistId)

        return channel_playlistId
    
    except requests.exceptions.RequestException as e:
        raise e

def get_video_ids(playlist_id):
    
    video_ids = []
    base_url = f"https://youtube.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults=50&playlistId={playlist_id}&key={API_KEY}"    
    page_token = None

    try :
        while True:
            url = base_url

            if page_token:
                url += f"&pageToken={page_token}" 
                
            response = requests.get(url)
            
            response.raise_for_status()
            
            data = response.json()

            for item in data.get('items', []) :
                video_id = item["contentDetails"]["videoId"]
                video_ids.append(video_id)
            
            page_token = data.get('nextPageToken')

            if not page_token:
                break
        
        return video_ids

    except requests.exceptions.RequestException as e:
        raise e
    
if __name__ == '__main__' : 
    print('get_playlist_id will be executed')
    
    playlist_id = get_playlist_id()
    
    video_ids = get_video_ids(playlist_id)

else :
    print("get_playlist_id won't be executed")



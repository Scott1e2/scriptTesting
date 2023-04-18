#watch a show when live
import requests
import webbrowser

# Replace YOUR_API_KEY with your actual Twitch API key
headers = {'Client-ID': 'YOUR_API_KEY'}

# Replace STREAMER_NAME with the name of the streamer you want to watch
url = 'https://api.twitch.tv/helix/streams?user_login=STREAMER_NAME'

while True:
    response = requests.get(url, headers=headers).json()
    if response['data']:
        # Stream is live, open it in a web browser
        stream_url = 'https://www.twitch.tv/' + response['data'][0]['user_name']
        webbrowser.open(stream_url)
        break


#working on this
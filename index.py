import base64
import requests
from dotenv import load_dotenv
import os

load_dotenv('.env')
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET =os.getenv('CLIENT_SECRET')


# Create Token in Spotify
def access_token():
    try:
        credentials = f"{CLIENT_ID}:{CLIENT_SECRET}"
        encoded_credentials = base64.b64encode(credentials.encode()).decode()

        response = requests.post(
            'https://accounts.spotify.com/api/token',
            headers={"Authorization": f"Basic {encoded_credentials}"},
            data={'grant_type': 'client_credentials'}
        )

        print("Token Generated Successfully...")
        return response.json()['access_token']

    except Exception as e:
        print("Error in Token Generation..", e)


# Latest release in Spotify
def get_new_release():
    try:
        token = access_token()

        header = {'Authorization': f'Bearer {token}'}
        Param = {'limit': 50}

        response = requests.get(
            'https://api.spotify.com/v1/browse/new-releases',
            headers=header,
            params=Param
        )

        if response.status_code == 200:
            data = response.json()

            albums = data['albums']['items']   # corrected indexing

            for i in albums:
                a = {
                    'album_name': i['name'],
                    'release_date': i['release_date']
                }
                print(a)

        else:
            print("Error:", response.text)

    except Exception as e:
        print("Error in latest release data fetching..", e)




# Call function
get_new_release()

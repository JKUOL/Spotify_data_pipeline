import json
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import boto3
from datetime import datetime

# Lambda function handler
def lambda_handler(event, context):
    # Get Spotify API credentials from environment variables
    client_id = os.environ.get('client_id')
    client_secret = os.environ.get('client_secret')

    # Set up Spotipy (Spotify API client) with client credentials flow
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

    # Define playlist link and extract the playlist URI (identifier)
    playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbNG2KDcFcKOF"
    playlist_URI = playlist_link.split("/")[-1]

    # Fetch playlist data from Spotify API
    spotify_data = sp.playlist_tracks(playlist_URI)

    # Set up boto3 (AWS SDK for Python) client for S3
    client = boto3.client('s3')

    # Define the filename for storing the data on S3
    filename = "spotify_raw_" + str(datetime.now()) + ".json"

    # Put Spotify data to S3 bucket in JSON format
    client.put_object(
        Bucket="spotify-etl-project-jk",
        Key="raw_data/to-process/" + filename,
        Body=json.dumps(spotify_data)
        )
# -*- coding: utf-8 -*-

# Sample Python code for youtube.playlistItems.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os

import googleapiclient.discovery
from dotenv import load_dotenv

load_dotenv()

API_SERVICE_NAME = "youtube"
API_VERSION = "v3"
DEVELOPER_KEY = os.getenv('YT_API_KEY')

if DEVELOPER_KEY is None:
    raise Exception("Please provide a Youtube API key")

youtube = googleapiclient.discovery.build(
    API_SERVICE_NAME, API_VERSION, developerKey=DEVELOPER_KEY)


def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    request = youtube.playlistItems().list(  # type: ignore
        part="contentDetails",
        maxResults=50,
        pageToken="",
        playlistId="UUkss6NzmCBzo8TyvB3I0qaA"
    )
    response = request.execute()

    print(response)


if __name__ == "__main__":
    main()

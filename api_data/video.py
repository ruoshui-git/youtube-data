import json
from typing import Any, Optional

from .youtube import youtube
from .utils import chunks

DAMI_UPLOADS_ID = 'UUkss6NzmCBzo8TyvB3I0qaA'


def get_all_video_id():

    video_ids: list[str] = []

    page_token = ''

    total: Optional[int] = None

    while True:
        req = youtube.playlistItems().list( # type: ignore
            part='snippet,contentDetails',
            maxResults=50,
            pageToken=page_token,
            playlistId=DAMI_UPLOADS_ID
        )

        res: dict[str, Any] = req.execute()

        if total is None:
            total = res['pageInfo']['totalResults']

        video_ids.extend((item['contentDetails']['videoId']
                          for item in res['items']))

        if 'nextPageToken' in res:
            page_token = res['nextPageToken']
        else:
            break

    assert total == len(video_ids)

    return video_ids

def get_video_info(parts: list[str] = ['snippet', 'statistics']) -> list[Any]:
    all = []
    videos = get_all_video_id()
    for chunk in chunks(videos, 50):
        res = youtube.videos().list( # type: ignore
            part=','.join(parts),
            id=','.join(chunk)
        ).execute()
        all.extend(res['items'])

    return all
from youtube_data.models import ChannelInfo, VideoInfo
from pathlib import Path
from typing import List
from collections import defaultdict


from itertools import islice
from collections import deque
def sliding_window_iter(iterable, size):
    """..."""
    iterable = iter(iterable)
    window = deque(islice(iterable, size), maxlen=size)
    for item in iterable:
        yield tuple(window)
        window.append(item)
    if window:  
        # needed because if iterable was already empty before the `for`,
        # then the window would be yielded twice.
        yield tuple(window)


if __name__ == '__main__':
    data_dir = Path("results/")
    data: List[ChannelInfo] = []
    for file in data_dir.iterdir():
        try:
            data.append(ChannelInfo.from_json(file.read_text(encoding='utf-8')))
        except AttributeError as e:
            print(f'error occurred while reading {file}: {e}')

    videos = defaultdict(list)
    for channel in data:
        for video in channel.playlist:
            videos[video.link.lstrip('https://www.youtube.com/watch?').split('&')[0]].append(video.view_count)

    video_counts = dict()
    for key, views in videos.items():
        diffs = []
        if len(views) == 0:
            print(f'key {key} has no views')
        else:    
            try:
                for val in sliding_window_iter(views, 2):
                    if len(val) == 2:
                        diffs.append(val[1] - val[0])
                    else:
                        # when there's only 1 stat available (first day video uploaded)
                        diffs.append(val[0])
                video_counts[key] = views[0] + sum((max(d, 0) for d in diffs))
            except ValueError as e:
                print(f"Error: {e}")

    print("total:", sum(video_counts.values()))
    
import json
from datetime import datetime
from dataclasses import dataclass
from typing import Any, List, Optional, Set
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class CommentInfo:
    author: str
    text: str

    # def __init__(self, author: str, text: str) -> None:
    #     self.author = author
    #     self.text = text


@dataclass_json
@dataclass
class VideoInfo:
    name: str
    link: str
    view_count: int
    likes: int
    dislikes: int
    comment_count: int
    comments: Optional[List[CommentInfo]]

#     def __repr__(self) -> str:
#         return (
#             f'''video:              {self.name}
#     link:               {self.link}
#     view:               {self.view_count}
#     likes:              {self.likes}
#     dislikes:           {self.dislikes}
#     comment_count:      {self.comment_count}
# '''
#         )

#     def __init__(self, name: str, link: str, view_count: int, likes: int, dislikes: int, comment_count: int, comments: List[CommentInfo]) -> None:
#         # ...
#         self.name = name
#         self.link = link
#         self.comments = comments
#         self.view_count = view_count
#         self.likes = likes
#         self.dislikes = dislikes
#         self.comment_count = comment_count


@dataclass_json
@dataclass
class ChannelInfo:
    playlist: List[VideoInfo]
    recorded_time: datetime
    total_likes: int
    total_dislikes: int
    total_views: int
    total_comments: int
    total_commenters: Optional[int]

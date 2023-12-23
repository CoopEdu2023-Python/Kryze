import json


class Account:
    def __init__(self):
        self.name = str()
        self.following = int()
        self.fans = int()
        self.likes = int()
        self.video = int()
        self.article = int()
        self.coins = int()
        self.uid = str()
        self.level = int()
        self.private_data = json

    def __str__(self):
        return (f"账号名: {self.name}   账号id: {self.uid}    {self.level}级      硬币数: {self.coins}\n粉丝数: {self.fans}"
                f"     关注账号数: {self.following}\n"
                f"投稿视频数: {self.video}   投稿文章数: {self.article}       获赞数: {self.likes}")


class Video_data:
    def __init__(self):
        self.aid = str()
        self.bvid = str()
        self.title = str()
        self.comments_num = int()
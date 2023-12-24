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
                f"视频播放量: {self.video}   文章浏览量: {self.article}       获赞数: {self.likes}\n\n")


class Video_data:
    def __init__(self):
        self.aid = str()
        self.bvid = str()
        self.title = str()
        self.comments_num = int()
        self.reply_data = []

    def __str__(self):
        res = json.dumps(self.reply_data, indent=2, ensure_ascii=False)
        final = '\n'.join(line for line in res.splitlines())
        return (f"标题: {self.title}   评论数量: {self.comments_num}\n"
                f"评论数据\n{final}\n")
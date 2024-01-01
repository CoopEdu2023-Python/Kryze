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
        self.json_output = dict()

    def generate_json(self):
        self.json_output['name'] = self.name
        self.json_output['uid'] = self.uid
        self.json_output['level'] = self.level
        self.json_output['following_num'] = self.following
        self.json_output['fans'] = self.fans
        self.json_output['likes'] = self.likes
        self.json_output['video_views'] = self.video
        self.json_output['article_views'] = self.article
        self.json_output['coins'] = self.coins
        self.json_output['video_list'] = list()

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
        self.play_num = int()
        self.coins = int()
        self.share = int()
        self.like = int()
        self.json_output = dict()

    def generate_json(self):
        self.json_output['aid'] = self.aid
        self.json_output['bvid'] = self.bvid
        self.json_output['title'] = self.title
        self.json_output['comments_num'] = self.comments_num
        self.json_output['coins'] = self.coins
        self.json_output['likes'] = self.like
        self.json_output['share'] = self.share
        self.json_output['play_num'] = self.play_num
        self.json_output['comments_data'] = self.reply_data

    def __str__(self):
        res = json.dumps(self.reply_data, indent=2, ensure_ascii=False)
        final = '\n'.join(line for line in res.splitlines())
        return (f"标题: {self.title}\n评论数量: {self.comments_num}      "
                f"点赞数: {self.like}      投币数: {self.coins}       转发数: {self.share}      浏览数量: {self.play_num}\n"
                f"评论数据\n{final}\n")
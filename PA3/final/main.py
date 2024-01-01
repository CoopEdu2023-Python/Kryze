import re
import requests
import json
from bs4 import BeautifulSoup
import time
import dec
import spider
import data_struct
import setup
import subprocess
import data_process
import random

# 初始化
print("开始初始化爬虫")
web_spider = spider.Spider()
user = data_struct.Account()
print("done!")

# 获取指定账户名称的uid
print("获取账户uid")
params = setup.Params_get_user
params['keyword'] = setup.Keywords
user.name = setup.Keywords
web_spider.headers = setup.Headers
web_spider.params = params
web_spider.target_url = setup.Search_api
search_page = web_spider.get_page().text
with open("cache/search_result.html", "w", encoding="utf-8") as file:
    file.write(search_page)

soup = BeautifulSoup(search_page, "html.parser")
user.uid = re.findall("//space.bilibili.com/([0-9]+)", soup.select_one("a", class_='mr_md').get("href"))[0]
print(user.uid)
print("done!")
# 获取粉丝和关注数量
print("获取账户信息")
params = setup.Params_follow_state
params['vmid'] = user.uid
web_spider.params = params
web_spider.target_url = setup.Following_state_api
follow_data = web_spider.get_page().json()
user.following = follow_data['data']['following']
user.fans = follow_data['data']['follower']

# 获取浏览数和点赞数
params = setup.Params_like_state
params['mid'] = user.uid
web_spider.params = params
web_spider.target_url = setup.Like_state_api
like_data = web_spider.get_page().json()
user.video = like_data['data']['archive']['view']
user.article = like_data['data']['article']['view']
user.likes = like_data['data']['likes']

# 获取账号数据
params = setup.Params_data_state
params['mid'] = user.uid
passwd = dec.web_rid(params)
params['w_rid'] = passwd[0]
params['wts'] = passwd[1]
web_spider.params = params
web_spider.target_url = setup.Account_data_api
account_data = web_spider.get_page()
with open("cache/account_data.json", "w", encoding="utf-8") as file:
    file.write(account_data.text)
user.private_data = account_data.json()
user.coins = user.private_data['data']['coins']
user.level = user.private_data['data']['level']
user.generate_json()
print("done!")

# 获取账号下所有的视频
print("获取账号下的视频")
scan_all = False
i = 1
bvids = []
aids = []
comments = []
titles = []
play = []
count_all = 0
current_sum = 0
while not scan_all:
    python_script_path = "magic.py"
    arg = [user.uid, str(i)]
    out = subprocess.run([f"{setup.Python_path}", python_script_path] + arg, capture_output=True, text=True, encoding="utf-8").stdout
    if len(out) == 0:
        break
    bvids.extend(re.findall("bvid: ([0-9a-zA-Z]+)", out))
    aids.extend(re.findall("aid: ([0-9a-zA-Z]+)", out))
    titles.extend(re.findall("title: (.+)", out))
    comments.extend(re.findall("comments: ([0-9a-zA-Z]+)", out))
    play.extend(re.findall("play: ([0-9a-zA-Z]+)", out))
    i += 1
    print(i)
    time.sleep(0.3)

proc = 0
videos = []
for i in range(0, len(bvids)):
    current = data_struct.Video_data()
    print(f"{proc} / {len(bvids)}")
    # 获取视频状态数据
    params = setup.Params_video_state
    params['bvid'] = bvids[i]
    web_spider.params = params
    web_spider.target_url = setup.Video_state_api
    state = web_spider.get_page().json()
    current.coins = state['data']['stat']['coin']
    current.like = state['data']['stat']['like']
    current.share = state['data']['stat']['share']
    proc += 1

    # 上传状态
    current.title = titles[i]
    current.bvid = bvids[i]
    current.aid = aids[i]
    current.play_num = play[i]
    current.comments_num = comments[i]
    videos.append(current)
print("done!")


print("获取评论区数据")
process = 0
for video in videos:
    print(f"{process} / {len(videos)}")
    params = setup.Params_reply
    params['oid'] = video.aid
    web_spider.target_url = setup.reply_api
    web_spider.params = params
    finish_tag = False
    current_sum = 0
    pre_sum = -1
    page = 1
    while (not finish_tag) and (pre_sum != current_sum):
        web_spider.params['pn'] = page
        pre_sum = current_sum
        comment_list = web_spider.get_page().json()
        sum = int(comment_list['data']['page']['count'])
        for comment in comment_list['data']['replies']:
            _ = dict()
            _['message'] = comment['content']['message']
            current_sum += 1
            _['replies'] = []
            for reply in comment['replies']:
                _['replies'].append(reply['content']['message'])
                current_sum += 1
            video.reply_data.append(_)
            if current_sum >= sum:
                finish_tag = True
                break
        page += 1
        time.sleep(0.3)
    process += 1
    video.generate_json()
print("done")

print("正在生成报告")
with open(f"output/report_{user.name}.txt", "w", encoding="utf-8") as report:
    report.write(user.__str__())

with open(f"output/report_{user.name}.txt", "a", encoding="utf-8") as report:
    for video in videos:
        report.write(video.__str__())
print("done")

print("正在生成数据文件")
user.json_output['video_list'] = bvids
data_process.generate_xlsx(user.json_output, videos)
print("done")



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
import random

# 初始化
web_spider = spider.Spider()
user = data_struct.Account()

# 获取指定账户名称的uid
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

# 获取粉丝和关注数量
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

# 获取账号下所有的视频
scan_all = False
i = 1
bvids = []
aids = []
comments = []
titles = []
while not scan_all:
    python_script_path = "magic.py"
    arg = [user.uid, str(i)]
    out = subprocess.run(["python", python_script_path] + arg, capture_output=True, text=True, encoding="utf-8")
    time.sleep(0.5)
    raw_data = str(out.stdout)
    count_all = int(re.findall("'count': ([0-9]+),", raw_data)[0])
    if i * 30 >= count_all:
        scan_all = True
    bvids.extend(re.findall("'bvid': '([0-9a-zA-Z]+)',", raw_data))
    aids.extend(re.findall("'aid': ([0-9]+),", raw_data))
    comments.extend(re.findall("'comment': ([0-9]+),", raw_data))
    titles.extend(re.findall(r"'title': '(.*?)'", raw_data))
    i += 1
    time.sleep(0.5)

videos = []
for i in range(0, ):
    current = data_struct.Video_data()
    current.title = titles[i]
    current.bvid = bvids[i]
    current.aid = aids[i]
    current.comments_num = comments[i]

print(user)

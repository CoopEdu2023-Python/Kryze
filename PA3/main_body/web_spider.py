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
import csv
import csv_generate
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
contents = list
with open(f'output/{setup.Keywords}/user_data.csv', 'w', newline='', encoding='utf-8') as file:
    pass  # 不做任何写入操作
with open(f'output/{setup.Keywords}/video_data.csv', 'w', newline='', encoding='utf-8') as file:
    pass  # 不做任何写入操作
with open(f'output/{setup.Keywords}/reply_data.csv', 'w', newline='', encoding='utf-8') as file:
    pass  # 不做任何写入操作
for video in videos:
    print(f"视频进度: {process} / {len(videos)}")
    finish = False
    i = 1
    num = 0
    while not finish and count_all >= num:
        python_script_path = "get_comment.py"
        arg = [video.aid, str(i)]
        out = subprocess.run([f"{setup.Python_path}", python_script_path] + arg, capture_output=True, text=True,
                             encoding="utf-8").stdout
        count_all = int(re.findall("count: ([0-9a-zA-Z]+)", out)[0])
        print(f"评论进度: {num} / {count_all}")
        lines = out.strip().split('\n')
        # 解析数据
        data = []
        temp_dict = {}
        current_key = None
        for line in lines:
            if line.startswith('content: '):  # 开始一个新的字典
                if temp_dict:
                    data.append(temp_dict)
                    temp_dict = {}
                current_key = 'content'
                temp_dict[current_key] = line[len('content: '):].strip()
            elif any(line.startswith(key + ': ') for key in
                     ["like", "cid", "ctime", "mid", "uname", "is_up_like", "ip"]):
                current_key = line.split(':', 1)[0]
                temp_dict[current_key] = line.split(':', 1)[1].strip()
            elif current_key == 'content':  # content字段中的换行
                temp_dict[current_key] += ' ' + line.strip()
            elif line.strip() == '...':  # 数据块的分隔
                continue
        # 添加最后一个字典
        if temp_dict:
            data.append(temp_dict)
        num += len(re.findall("content", out))

        # CSV文件的头部（列名）
        headers = ["content", "like", "cid", "ctime", "mid", "uname", "is_up_like", "ip", "up_name", "aid", "up_name"]

        # 写入数据到CSV
        with open(f'output/{setup.Keywords}/reply_data.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            # 如果文件是新的，写入头部
            if file.tell() == 0:
                writer.writeheader()
            for row in data:
                # 转换布尔值和整数
                row['like'] = int(row['like'])
                row['cid'] = int(row['cid'])
                row['ctime'] = int(row['ctime'])
                row['mid'] = int(row['mid'])
                row['is_up_like'] = row['is_up_like'] == 'True'
                row['aid'] = video.aid
                row['up_name'] = setup.Keywords
                writer.writerow(row)
        i += 1
    video.generate_json()
    process += 1
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
csv_generate.to_csv(setup.Keywords)
print("done")
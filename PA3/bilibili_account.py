import re
import requests
import json
from bs4 import BeautifulSoup
import time
import hashlib
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()


def web_rid(param):
    """js解密"""
    n = "9cd4224d4fe74c7e9d6963e2ef891688" + "263655ae2cad4cce95c9c401981b044a"
    c = ''.join([n[i] for i in
                 [46, 47, 18, 2, 53, 8, 23, 32, 15, 50, 10, 31, 58, 3, 45, 35, 27, 43, 5, 49, 33, 9, 42, 19, 29, 28, 14,
                  39, 12, 38, 41, 13, 37, 48, 7, 16, 24, 55, 40, 61, 26, 17, 0, 1, 60, 51, 30, 4, 22, 25, 54, 21, 56,
                  59, 6, 63, 57, 62, 11, 36, 20, 34, 44, 52]][:32])
    s = int(time.time())
    param["wts"] = s
    param = "&".join([f"{i[0]}={i[1]}" for i in sorted(param.items(), key=lambda x: x[0])])
    return hashlib.md5((param + c).encode(encoding='utf-8')).hexdigest(), s


class Account:
    def __init__(self, username, space_addr):
        self.username = username
        self.space_addr = space_addr
        self.uid = str()
        self.fans = int()
        self.following = int()
        self.views = int()
        self.likes = int()
        self.article_views = int()
        self.video_num = int()
        self.audio_num = int()
        self.article_num = int()

    def __str__(self):
        return (f"{self.username}: uid: {self.uid} \nfans: {self.fans} likes: {self.likes} "
                f"following: {self.following} views: {self.views} article_views: {self.article_views}")


class Video_data:
    def __init__(self, bvid):
        self.bvid = bvid
        self.aid = str()
        self.review_data = json

def print_user_list(user_list: list):
    for ele in user_list:
        print(ele)


search_api = 'https://search.bilibili.com/upuser?'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'cookie': 'buvid3=DB63C40D-0344-B088-B882-D3C7E046A72F91393infoc; b_nut=1698498791; CURRENT_FNVAL=4048; _uuid=7107AC658-108310-4110F-3BAC-6A1026B6A1091E72946infoc; buvid4=BB284D28-43F3-8557-6108-FEB1891A42A193574-023102821-paGIybps7qw3HWSFfsEs8w%3D%3D; rpdid=|(u~)YJ|)))u0J\'uYm)Rm)~mR; enable_web_push=DISABLE; header_theme_version=CLOSE; DedeUserID=1567113694; DedeUserID__ckMd5=f415c329ce53457e; CURRENT_QUALITY=80; buvid_fp_plain=undefined; LIVE_BUVID=AUTO3017020964209180; home_feed_column=5; browser_resolution=1707-838; fingerprint=fdc0d21e0476a2aa928e27445cff466a; buvid_fp=fdc0d21e0476a2aa928e27445cff466a; SESSDATA=6f89a7e5%2C1718709764%2C418a7%2Ac2CjC5q6cy8i-UoTpuw2hr3osCOxiciNSt-Co05QkIs6XqYxDBoIlHQ800M-QdsCqG_iASVmczYUR5VDVTZ3YxdjFFZWg1R3dzQl9lX3dtM1dkNFBVTU1nT2RGUlBjMEpuZ1YxdG9ZZVpxUC1vaUhJTWFPQXByM2pVSC1MUzEzSmVERWlGaU1oQ1dBIIEC; bili_jct=fc84243d362748651761f3a2c2978254; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDM1MDAwMTIsImlhdCI6MTcwMzI0MDc1MiwicGx0IjotMX0.IRB-YogVwbeUYOLA8Jr5SHxXBvEqPKWhCNHgEShHsy4; bili_ticket_expires=1703499952; sid=5x0gww39; bp_video_offset_1567113694=877915122312413209; b_lsid=8B910621B_18C91A8F164; PVID=4'
}

params = {
    'keyword': 'HIKARI-FIELD',
}

user_list = requests.get(url=search_api, headers=headers, params=params)

with open("raw/search_result.html", "w", encoding="utf-8") as file:
    file.write(user_list.text)

search_result = BeautifulSoup(user_list.text, 'html.parser')
space_list = search_result.select("a")
users = []
for user in space_list:
    if user.get("title") != None:
        users.append(Account(user.get("title"), 'https:' + user.get("href")))

users[0].uid = re.findall("https://space.bilibili.com/([0-9]+)",users[0].space_addr)


follow_state_api = 'https://api.bilibili.com/x/relation/stat?'
params = {
    'vmid': users[0].uid
}

follow_state = requests.get(url=follow_state_api, headers=headers, params=params).json()
users[0].fans = follow_state['data']['follower']
users[0].following = follow_state['data']['following']

likes_state_api = 'https://api.bilibili.com/x/space/upstat?'
params = {
    'mid': users[0].uid,
}

likes_state = requests.get(url=likes_state_api, headers=headers, params=params).json()
users[0].views = likes_state['data']['archive']['view']
users[0].article_views = likes_state['data']['article']['view']
users[0].likes = likes_state['data']['likes']

content_api = 'https://api.bilibili.com/x/space/navnum?'
params = {
    'mid': users[0].uid
}
content_state = requests.get(url=content_api, headers=headers, params=params).json()
users[0].video_num = content_state['data']['video']
users[0].article_num = content_state['data']['opus']
users[0].audio_num = content_state['data']['audio']




user_id = ''
for i in users[0].uid:
    if '0' <= i <= '9':
        user_id += i
num = 1
finish = False
pages = users[0].video_num // 30 + 1
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)
video_list = []
for num in range(1, pages + 1):
    video_url_current = f'https://space.bilibili.com/{user_id}/video?pn={str(num)}'
    get_state = False
    while not get_state:
        driver.get(video_url_current)
        time.sleep(3)
        source = driver.page_source
        soup = BeautifulSoup(source, "html.parser")
        li_ele = soup.find_all('li', class_='fakeDanmu-item')
        get_state = not (li_ele == [])
    for video in li_ele:
        video_list.append(video['data-aid'])
    # with open(f"raw/bili_pages/page{str(num)}_{user_id}.html", "w", encoding="utf-8") as file:
    #     file.write(source)

video_data_list = []
for video in video_list:
    current_ = Video_data(video)
    current_video_url = f'https://www.bilibili.com/video/{video}'
    page = requests.get(url=current_video_url, headers=headers).text


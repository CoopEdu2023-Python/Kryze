import json
import jieba
import jieba.analyse
import matplotlib
import re
from wordcloud import WordCloud
import requests


def words_split(raw: list):
    words = list()
    for comment in raw:
        comment = re.sub(r'\[.*?\]', '', comment)
        comment = re.sub(r'@.*?', '', comment)
        words += jieba.cut(comment)
    return words


def get_comments(data_name: str):
    videos_stat = list()
    video_title = list()
    comments_all = 0
    proc = 0
    with open(f"output/{data_name}/user_data.json", "r", encoding='utf-8') as user_data:
        user_stat = json.loads(user_data.read())
    print(f"共检测到{len(user_stat['video_list'])}条视频数据")

    for video in user_stat['video_list']:
        print(f'视频进度: {proc + 1} / {len(user_stat["video_list"])}')
        with open(f"output/{data_name}/videos/{video}.json", "r", encoding='utf-8') as video_data:
            try:
                json_data = json.load(video_data)
                videos_stat.append(json_data)
                video_title.append(json_data['title'])
            except json.decoder.JSONDecodeError as e:
                print(f"JSON 解码错误：{e}")
        proc += 1

    video_state_scores = list()
    video_reply_scores = list()
    proc = 1

    print("正在估测评论总数")
    reply_list = list()
    stat_list = list()
    for data in videos_stat:
        s = 0
        for sub_data in data['comments_data']:
            reply_list.append(sub_data['message'])
            reply_list.extend(sub_data['replies'])
        current = data
        stat_list.append(current)

    comments_all = len(reply_list)
    print(comments_all, 'done')
    return reply_list, video_title


def generate_wordcloud(folder_name: str):
    data_name = folder_name
    data = get_comments(data_name)
    reply_list = data[0]
    title_list = data[1]
    reply_list_words = words_split(reply_list)
    title_list_words = words_split(title_list)
    wordcloud = WordCloud(
        font_path='/System/Library/Fonts/msyh.ttc',
        width=1920, height=1080,
        max_words=40
    )
    stopwords_url = 'https://raw.githubusercontent.com/goto456/stopwords/master/hit_stopwords.txt'
    stopwords = requests.get(stopwords_url).text.split('\n')
    stopwords.extend(['不', '不是', '好', '都', '回复', '说', '耶', '是', '没有', '没', '人', '更', '会', '作者', '喜欢', '想',
                      '快', '很', '真的', '不会', '好好', '还', '现在', '知道', '感觉'])
    words = [word for word in reply_list_words if word not in stopwords]
    # Generate wordcloud
    wordcloud.generate(' '.join(words))
    # Save as png
    wordcloud.to_file(f'output/{data_name}/wordcloud.png')
    print('done')


import jieba
import jieba.analyse
import re
from wordcloud import WordCloud
import requests
import pandas


def words_split(raw: list):
    words = list()
    for comment in raw:
        comment = re.sub(r'\[.*?\]', '', comment)
        comment = re.sub(r'@.*?', '', comment)
        words += jieba.cut(comment)
    return words


def get_comments(data_name: str):
    reply_data = pandas.read_csv(f"output/{data_name}/reply_data.csv", encoding='utf-8')
    reply_list = reply_data['content']
    title_data = pandas.read_csv(f"output/{data_name}/video_data.csv", encoding='utf-8')
    title_list = title_data['title']
    return reply_list, title_list


def generate_wordcloud(folder_name: str, mode: str):
    data_name = folder_name
    data = get_comments(data_name)
    reply_list = data[0]
    title_list = data[1]
    reply_list_words = words_split(reply_list)
    title_list_words = words_split(title_list)
    target = reply_list_words if mode == 'reply' else title_list_words
    wordcloud = WordCloud(
        font_path='/System/Library/Fonts/msyh.ttc',
        width=2560, height=1440,
        background_color='white'
    )
    stopwords_url = 'https://raw.githubusercontent.com/goto456/stopwords/master/hit_stopwords.txt'
    stopwords = requests.get(stopwords_url).text.split('\n')
    stopwords.extend(['不', '不是', '好', '都', '回复', '说', '耶', '是', '没有', '没', '人', '更', '会', '作者', '喜欢', '想',
                      '快', '很', '真的', '不会', '好好', '还', '现在', '知道', '感觉', '觉得', '直接', '最', '看', '看到', '真是',
                      '上', '复制', '简介', '赢', '应该', '真是', '哈', '男', '女', '鬼', '', ' '])
    words = [word for word in target if word not in stopwords]
    # Generate wordcloud
    wordcloud.generate(' '.join(words))
    # Save as png
    wordcloud.to_file(f'output/{data_name}/wordcloud_{mode}.png')
    print('done')
    return words


if __name__ == "__main__":
    generate_wordcloud("iMoore", 'reply')
import os
import json
import pandas as pd
from cemotion import *
import torch
import warnings
import setup
import matplotlib.pyplot as plt
import numpy as np
import time
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor


warnings.filterwarnings("ignore", category=UserWarning)
# 初始化评估模型
print("初始化评估模型")
predictor = Cemotion()
comments_all = 0
proc = 0
print('done')


class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.floating):
            return float(obj)
        return super(NumpyEncoder, self).default(obj)


def struct_data(data: dict):
    res = json.dumps(data, indent=2, ensure_ascii=False, cls=NumpyEncoder)
    final = '\n'.join(line for line in res.splitlines())
    return res


def predict_process(words_list: list):
    global proc, comments_all
    res = list()
    for reply in words_list:
        res.append(predictor.predict(reply))
        proc += 1
        print(f"{proc} / {comments_all}")
    return res

def avg(data):
    max_length = max(len(row) for row in data)
    padded_data = []
    for row in data:
        padding_size = max_length - len(row)
        if padding_size > 0:
            # 使用均值填充
            padding_value = np.mean(row)
            padded_row = np.pad(row, (0, padding_size), constant_values=padding_value)
        else:
            padded_row = row.copy()
        padded_data.append(padded_row)
    padded_tensor = torch.tensor(padded_data)
    return padded_tensor


# 评估账号基本数据
def user_state_score(data: json):
    return ((data['fans'] / 100)
            * (data['likes'] / 1000)
            * ((data['video_views'] + data['article_views']) / 10000))


def split_list_into_segments(input_list, num_segments):
    avg_length = len(input_list) // num_segments
    segments = [input_list[i:i + avg_length] for i in range(0, len(input_list), avg_length)]
    return segments


# 评估视频评论区和视频数据
def video_state_score(data_video: list, data_stat: list):
    sum = 1
    res = []
    val_list = []
    num_threads = setup.Thread_max
    stat_score = list()
    # 评估视频基本数据
    for data in data_stat:
        stat_score.append((float(data['play_num']) / 10000) * ((data['likes'] + data['share'] + data['coins']) / 1000))

    val_rep = list()
    if num_threads > len(data_video):
        num_threads = len(data_video)
    segments = split_list_into_segments(data_video, num_threads)
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        val_list.extend(list(executor.map(predict_process, segments)))
    val_rep = [element for row in val_list for element in row]
    return (stat_score, val_rep)


# 读取档案
data_name = input("请输入档案名称: ")
videos_stat = list()

with open(f"output/{data_name}/user_data.json", "r", encoding='utf-8') as user_data:
    user_stat = json.loads(user_data.read())
print(f"共检测到{len(user_stat['video_list'])}条视频数据")


for video in user_stat['video_list']:
    print(f'视频进度: {proc + 1} / {len(user_stat["video_list"])}')
    with open(f"output/{data_name}/videos/{video}.json", "r", encoding='utf-8') as video_data:
        try:
            json_data = json.load(video_data)
            videos_stat.append(json_data)
        except json.decoder.JSONDecodeError as e:
            print(f"JSON 解码错误：{e}")
    proc += 1

# print(videos_stat)

user_score = user_state_score(user_stat)
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

start_time = time.time()
res = video_state_score(reply_list, stat_list)
video_state_scores.append(res[0])
video_reply_scores.append(res[1])
end_time = time.time()
print(end_time - start_time)
# 导出数据
weight_data = dict()
weight_data['user_stat_score'] = user_score
weight_data['video_stat_score'] = video_state_scores
weight_data['video_reply_score'] = video_reply_scores
with open(f"output/{data_name}/weights.json", "w", encoding='utf-8') as weight:
    weight.write(struct_data(weight_data))








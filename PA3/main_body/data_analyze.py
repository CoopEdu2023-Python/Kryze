import numpy
import numpy as np
import torch
import json
import matplotlib.pyplot as plt


def get_data(data_index: str):
    with open(f"output/{data_index}/weights.json", "r", encoding='utf-8') as weights_data:
        json_data = json.loads(weights_data.read())
        return json_data["video_stat_score"], json_data["video_reply_score"]


name = input('输入档案名称: ')

try:
    res = get_data(name)
except:
    print("未找到档案")
    exit()

stat = res[0]
reply = res[1]
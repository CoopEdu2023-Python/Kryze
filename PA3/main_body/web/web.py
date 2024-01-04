import matplotlib.pyplot as plt
import matplotlib
import streamlit as st
import pandas as pd
import json
import seaborn as sns
import numpy as np
import os
import sys
import subprocess


current_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(current_dir, '..', 'output')
folders = [f for f in os.listdir(output_dir) if os.path.isdir(os.path.join(output_dir, f))]

# 设置 Matplotlib 字体
matplotlib.rcParams['font.family'] = 'Microsoft YaHei'  # 或其他支持中文的字体


def show_user_info(selected_folder):
    user_info = get_user_info(selected_folder)
    translations = {
        "name": "用户名",
        "uid": "用户ID",
        "level": "等级",
        "following_num": "关注数",
        "fans": "粉丝数",
        "sign": "签名",
        "likes": "点赞数",
        "video_views": "视频观看数",
        "article_views": "文章观看数"
        # "coins" 已被排除
    }
    st.title('用户信息')
    st.write(f"显示 {selected_folder} 的信息")
    for key, value in user_info.items():
        if key not in ['video_list', 'coins']:  # 排除 video_list 和 coins
            chinese_key = translations.get(key, key)
            st.write(f"{chinese_key}: {value}")


def show_data_analysis(selected_folder):
    st.title('数据可视化')
    st.write(f"您选择的文件夹是： {selected_folder}")
    weight_data = get_weight(selected_folder)
    data_stat = weight_data[0]
    data_reply = weight_data[1]

    # 用户选择数据集的下拉菜单
    dataset_name = st.selectbox('选择数据', ('视频评分数据', '评论情感倾向'))

    # 显示选定的数据集
    if dataset_name == '视频评分数据':
        st.markdown("""
                **视频评分计算公式：**  
                `评分 = (粉丝数 / 100) * (点赞数 / 1000) * ((视频观看次数 + 文章观看次数) / 10000)`
                """)
        selected_data = data_stat
    else:
        selected_data = data_reply

    # 绘制图表
    fig = plot_data(selected_data, dataset_name)
    st.pyplot(fig)


def show_cloud(selected_folder):
    # 构建wordcloud.png文件的完整路径
    file_path = os.path.join('main_body', 'output', selected_folder, 'wordcloud.png')
    if os.path.exists(file_path):
        st.header('词云分析')

        st.image(file_path)
    else:
        st.warning('wordcloud.png not found in the selected folder.')


def get_weight(folder: str):
    with open(f"main_body/output/{folder}/weights.json", "r", encoding='utf-8') as file:
        data = file.read()
        raw = json.loads(data)
    return raw['video_stat_score'], raw['video_reply_score']


def get_user_info(folder: str):
    with open(f"main_body/output/{folder}/user_data.json", "r", encoding='utf-8') as file:
        data = json.load(file)
    return data


# 绘制折线图并隐藏 X 轴下标
def plot_data(selected_data, dataset_name):
    fig, ax = plt.subplots()
    ax.hist(selected_data, bins=30, alpha=0.7, color='blue')
    ax.set_title(dataset_name)
    ax.set_xlabel('Score')
    ax.set_ylabel('Frequency')
    return fig


def main_frame():
    st.sidebar.title("选择用户")
    selected_folder = st.sidebar.selectbox('选择用户', folders)
    st.sidebar.title("导航")
    page = st.sidebar.radio("选择页面：", ["用户信息", "数据分析", "词云展示"])

    if page == "用户信息":
        show_user_info(selected_folder)
    elif page == "数据分析":
        show_data_analysis(selected_folder)
    elif page == '词云展示':
        show_cloud(selected_folder)


if __name__ == '__main__':
    pass

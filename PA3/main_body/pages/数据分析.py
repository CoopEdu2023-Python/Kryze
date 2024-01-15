import re
import requests
import pandas
import streamlit as st
import pandas as pd
import json
import wordcloud_generate
import setup
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import os


def get_folders_name():
    folder_path = 'output/'
    folders = [f.name for f in os.scandir(folder_path) if f.is_dir()]
    return folders


def get_weights(folder_name):
    with open(f"output/{folder_name}/weights.json", 'r', encoding='utf-8') as file:
        json_file = json.loads(file.read())
    return json_file


def show_user_chooser():
    folders = get_folders_name()
    if folders:
        selected_folder = st.sidebar.selectbox('选择用户档案', folders)
    else:
        st.write('output/ 文件夹下没有任何文件夹。')
    return selected_folder


def show_data_analyze(folder_name):
    modes = {"评论数据": display_emotion_data, '评论ip分布数据': display_map_data, '视频发布数据': display_video_publish_data}
    mode = st.selectbox("数据类型", modes.keys())
    modes[mode](folder_name)


def display_video_publish_data(folder_name):
    # 发布时间相关
    st.subheader('发布数据')
    csv_path = f'output/{folder_name}/video_data.csv'
    raw_data = pd.read_csv(csv_path)
    raw_data = raw_data.sort_values(by='pubdate')
    pub_time = raw_data['pubdate']
    standard_time = pd.to_datetime(pub_time, unit='s')
    standard_time = standard_time.dt.tz_localize('UTC').dt.tz_convert('Asia/Shanghai')
    st.write(f"视频总数: {len(standard_time)}")
    date_range = standard_time.max() - standard_time.min()
    frequency = len(standard_time) / (date_range.days / 30)
    st.write(f"每月平均发布: {frequency:.2f} 个视频")
    standard_time = standard_time.dt.to_period('M')
    monthly_counts = standard_time.value_counts().sort_index()
    monthly_counts.index = monthly_counts.index.astype(str)
    fig_pub = px.line(monthly_counts, labels={'index': 'Month', 'value': 'Number of Videos'},
                 title='Monthly Video Publish Count')
    st.plotly_chart(fig_pub, use_container_width=True)

    st.subheader('点赞数据')
    # 视频具体数据
    comments_num = raw_data['comments_num']
    video_id = raw_data['title']
    likes_num = raw_data['likes']
    st.write(f'平均每个视频有: {likes_num.mean()} 个点赞')
    st.write(f"最小点赞数: {likes_num.min()}")
    st.write(f"最大点赞数: {likes_num.max()}")
    st.write(f"中位数: {likes_num.median()}")
    fig_like = px.line(likes_num, labels={'index': 'video', 'value': 'Number of likes'}, title='视频点赞数据',
                       x=video_id, y=likes_num)
    fig_like.update_layout(
        xaxis=dict(
            showticklabels=False,  # 隐藏刻度标签
        )
    )
    st.plotly_chart(fig_like, use_container_width=True)
    # 标题数据
    st.subheader("标题数据")
    keywords = wordcloud_generate.generate_wordcloud(folder_name, 'title')
    st.markdown("标题关键词")
    st.write(set(keywords[0:15:]))
    st.write(f"{'......(仅显示前15个)' if len(keywords) > 15 else ''}")
    st.markdown("标题词云")
    st.image(f"output/{folder_name}/wordcloud_title.png")


def display_comments_data(folder_name):
    st.subheader('评论数量数据')
    csv_path = f'output/{folder_name}/video_data.csv'
    raw_data = pd.read_csv(csv_path)
    raw_data = raw_data.sort_values(by='pubdate')
    c_num = raw_data['comments_num']
    video_id = raw_data['title']
    st.write(f'平均评论数: {c_num.mean()}')
    st.write(f'最大评论数: {c_num.max()}')
    st.write(f'最小评论数: {c_num.min()}')
    st.write(f'中位数: {c_num.median()}')
    fig_num = px.line(c_num, labels={'index': 'Video', 'value': 'Number of comments'},
                      title='Video comments Count', x=video_id, y=c_num)
    fig_num.update_layout(
        xaxis=dict(
            showticklabels=False,  # 隐藏刻度标签
        )
    )
    st.plotly_chart(fig_num, use_container_width=True)
    st.subheader("情感倾向数据")
    display_emotion_data(folder_name)
    st.subheader("内容分析")
    keywords = wordcloud_generate.generate_wordcloud(folder_name, 'reply')
    st.markdown("内容关键词")
    st.write(set(keywords[0:15:]))
    st.write(f"{'......(仅显示前15个)' if len(keywords) > 15 else ''}")
    st.markdown("内容词云")
    st.image(f"output/{folder_name}/wordcloud_reply.png")


def display_emotion_data(folder_name):
    data_weight = get_weights(folder_name)
    reply_emotion = pd.DataFrame(data_weight["video_reply_score"][0], columns=['weight'])
    st.write(f"平均值: {reply_emotion.mean()}")
    st.write(f'最小值: {reply_emotion.min()}')
    st.write(f"最大值: {reply_emotion.max()}")
    st.write(f"中位数: {reply_emotion.median()}")
    fig = px.histogram(reply_emotion, nbins=50, range_x=[0, 1])
    fig.update_layout(
        title='情感倾向分布',
        xaxis_title='情感倾向',
        yaxis_title='数量',
        bargap=0.1
    )
    st.plotly_chart(fig, use_container_width=True)


def display_map_data(folder_name):
    locations = dict()
    csv_path = f'output/{folder_name}/reply_data.csv'
    ip_data = pandas.read_csv(csv_path, encoding='utf-8')['ip']
    ip_set = list(ip_data)
    location_data = []
    locations['lon'] = []
    locations['lat'] = []
    cache = dict()
    try:
        with open("cache/locations_data.json", 'r', encoding='utf-8') as cache_data:
            cache = json.loads(cache_data.read())
    except:
        pass
    for ip in ip_data:
        if ip == 'unknown':
            continue
        ip_current = re.findall("IP属地：(.+)", ip)[0]
        if ip_current and ip_current != '未知':
            try:
                locations['lon'].append(cache[ip_current]['lon'])
                locations['lat'].append(cache[ip_current]['lat'])
            except:
                print(f"未找到地址  {ip_current}  的坐标")
                params = setup.Params_geodata
                params['ds']['keyWord'] = ip_current
                raw = requests.get(url=f'https://api.tianditu.gov.cn/geocoder?ds={{"keyWord":"{ip_current}"}}&tk=9aea2f'
                                       f'41881a8de0c50280d9c8d81619').json()
                locations['lon'].append(raw['location']['lon'])
                locations['lat'].append(raw['location']['lat'])
                cache[ip_current] = dict()
                cache[ip_current]["lon"] = raw['location']['lon']
                cache[ip_current]["lat"] = raw['location']['lat']
    jitter = 0.8  # 调整系数
    data = pd.DataFrame(locations)
    color = []
    for i in range(len(data)):
        color.append((data['lon'][i] * 100 % 1.0, data['lat'][i] * 100 % 1.0, (data['lon'][i] + data['lat'][i]) * 100 % 1.0))
    data['lat'] = data['lat'] + np.random.randn(len(data)) * jitter
    data['lon'] = data['lon'] + np.random.randn(len(data)) * jitter
    data['color'] = color
    with open("cache/locations_data.json", 'w', encoding='utf-8') as cache_data:
        cache_data.write(str(cache).replace("'", '\"'))
    st.map(data, color='color', use_container_width=False)
    display_location_data(folder_name)


def display_location_data(folder_name):
    csv_path = f'output/{folder_name}/reply_data.csv'
    ip_data = pd.read_csv(csv_path, encoding='utf-8')['ip']
    location_counts = {}
    total_count = 0
    for ip in ip_data:
        if ip == 'unknown':
            continue
        ip_current = re.findall("IP属地：(.+)", ip)[0]
        if ip_current and ip_current != '未知':
            location_counts[ip_current] = location_counts.get(ip_current, 0) + 1
            total_count += 1
    others_count = 0
    threshold = 0.025 * total_count
    for location, count in list(location_counts.items()):
        if count < threshold:
            others_count += count
            del location_counts[location]
    if others_count > 0:
        location_counts['其他'] = others_count
    data = pd.DataFrame(list(location_counts.items()), columns=['Location', 'Count'])
    fig = go.Figure(data=[go.Pie(labels=data['Location'], values=data['Count'], hole=0.3)])
    fig.update_traces(textinfo='percent+label', pull=0.05)
    fig.update_layout(title_text='3D Pie Chart Style: Number of People per Location')
    st.plotly_chart(fig)


def main():
    folder = show_user_chooser()
    map, comment, pub = st.tabs(["ip位置数据", '评论数据', '发布数据'])
    with map:
        display_map_data(folder)
    with comment:
        display_comments_data(folder)
    with pub:
        display_video_publish_data(folder)


if __name__ == '__main__':
    main()
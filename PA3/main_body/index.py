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


def main():
    video_file = open('pages/videos/introduction.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)


if __name__ == '__main__':
    main()

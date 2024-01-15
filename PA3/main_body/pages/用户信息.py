import streamlit as st
import os
import pandas as pd
import setup


def get_folders_name():
    folder_path = 'output/'
    folders = [f.name for f in os.scandir(folder_path) if f.is_dir()]
    return folders


def show_user_chooser():
    folders = get_folders_name()
    if folders:
        selected_folder = st.sidebar.selectbox('选择用户档案', folders)
    else:
        st.write('output/ 文件夹下没有任何文件夹。')
    return selected_folder


def display_user_data(folder_name):
    st.markdown('<span style="color: blue;">账户基本信息</span>', unsafe_allow_html=True)
    try:
        file_path = os.path.join('output', folder_name, 'user_data.csv')
        df = pd.read_csv(file_path)
        columns_order = ['姓名', '用户ID', '等级', '签名', '粉丝数', '关注数', '点赞数', '视频观看数', '文章浏览数', '硬币数']
        columns_mapping = {
            'name': '姓名',
            'uid': '用户ID',
            'level': '等级',
            'following_num': '关注数',
            'fans': '粉丝数',
            'sign': '签名',
            'likes': '点赞数',
            'video_views': '视频观看数',
            'article_views': '文章浏览数',
            'coins': '硬币数'
        }
        df.rename(columns=columns_mapping, inplace=True)
        df = df[columns_order]
        for index, row in df.iterrows():
            for col in df.columns:
                st.text(f"{col}: {row[col]}")
            st.markdown("---")  # 添加分隔线
    except FileNotFoundError:
        st.error(f'在文件夹 {folder_name} 中找不到 user_data.csv 文件。')
    except Exception as e:
        st.error(f'读取文件时发生错误：{e}')


def display_video_data(folder):
    st.markdown('<span style="color: blue;">账户下视频信息</span>', unsafe_allow_html=True)
    try:
        file_path = os.path.join('output', folder, 'video_data.csv')
        df = pd.read_csv(file_path)
        df = df.drop(columns=['author', 'uid', 'aid'])
        df['pubdate'] = df['pubdate'].astype(str)
        date_format = st.radio("选择 'pubdate' 的显示格式", ('时间戳', '日期'))
        filter_flag = st.multiselect('筛选项', ['R-18', '全年龄'])
        if date_format == '日期':
            df['pubdate'] = pd.to_datetime(df['pubdate'], unit='s').dt.strftime('%Y-%m-%d')
        else:
            df['pubdate'] = df['pubdate'].astype(str)
        pattern = '|'.join(setup.filter_words)
        filter_df = None
        if len(filter_flag) % 2 == 0:
            st.dataframe(df)
        elif filter_flag[0] == '全年龄':
            filtered_df = df[~df['title'].str.contains(pattern, na=False)]
            st.dataframe(filtered_df)
        elif filter_flag[0] == 'R-18':
            filtered_df = df[df['title'].str.contains(pattern, na=False)]
            st.dataframe(filtered_df)
    except FileNotFoundError:
        st.error(f'在文件夹 {folder} 中找不到 video_data.csv 文件。')
    except Exception as e:
        st.error(f'读取文件时发生错误：{e}')


def show_user_data(folder_name):
    st.subheader("用户信息")
    display_user_data(folder_name)
    display_video_data(folder_name)


folder = show_user_chooser()
show_user_data(folder)



import streamlit as st
import os
import matplotlib
import matplotlib.pyplot as plt
import json
import wordcloud_generate, Account_val
import web.web


output_dir = os.path.join('', 'output')
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


def show_spider_setting():
    proc_list = [web_spider.init_spider, web_spider.get_uid, web_spider.get_follow, web_spider.get_like,
                 web_spider.get_stat, web_spider.get_videos]
    proc_name = ['爬虫初始化', "uid获取", "获取关注状态", '获取总点赞和播放量', '获取账号其他状态数据', '获取视频数据']
    st.title("爬虫基本设置")
    user_name = st.text_input('用户名')
    max_retries = st.text_input('最大重试次数')
    if max_retries != '':
        try:
            max_retries = int(max_retries)
        except:
            st.error('请输入数字')
    status_placeholders = [st.empty() for _ in proc_list]
    for name, placeholder in zip(proc_name, status_placeholders):
        placeholder.markdown(f"<span style='color: gray;'>**{name}**: 未执行</span>", unsafe_allow_html=True)
    if st.button("开始爬取") and (max_retries is not None and user_name is not None):
        res = []
        stat = 'success'
        for proc_current, placeholder in zip(range(len(proc_list)), status_placeholders):
            placeholder.markdown(f"<span style='color: orange;'>**{proc_name[proc_current]}**: 执行中...</span>",
                                 unsafe_allow_html=True)
            res = proc_list[proc_current](user_name, max_retries, res)
            if type(res) == str:
                placeholder.markdown(f"<span style='color: red;'>**{proc_name[proc_current]}**: 执行失败</span>",
                                     unsafe_allow_html=True)
                stat = 'error'
                break
            else:
                placeholder.markdown(f"<span style='color: green;'>**{proc_name[proc_current]}**: 执行成功</span>",
                                     unsafe_allow_html=True)

        if stat == 'error':
            st.error('执行失败\n建议刷新后重试')
        else:
            st.success('执行成功')
        for name, placeholder in zip(proc_name, status_placeholders):
            placeholder.markdown(f"<span style='color: gray;'>**{name}**: 未执行</span>", unsafe_allow_html=True)


def show_data_analysis(selected_folder):
    st.title('数据可视化')
    st.write(f"您选择的文件夹是： {selected_folder}")
    if st.button('重新分析数据'):
        st.session_state.progress_bar = st.progress(0)
        Account_val.generate_weight(selected_folder)
        st.success('生成完成！')
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
    st.header('词云分析')
    if st.button('重新生成词云'):
        wordcloud_generate.generate_wordcloud(selected_folder)  # 重新生成词云
        st.rerun()
    file_path = os.path.join('output', selected_folder, 'wordcloud.png')
    if os.path.exists(file_path):
        st.image(file_path)
    else:
        st.write('未找到词云图片，请点击上面的按钮生成词云。')


def get_weight(folder: str):
    with open(f"output/{folder}/weights.json", "r", encoding='utf-8') as file:
        data = file.read()
        raw = json.loads(data)
    return raw['video_stat_score'], raw['video_reply_score']


def get_user_info(folder: str):
    with open(f"output/{folder}/user_data.json", "r", encoding='utf-8') as file:
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


def main():
    st.sidebar.title("选择用户")
    selected_folder = st.sidebar.selectbox('选择用户', folders + ['+'])
    if selected_folder != '+':
        st.sidebar.title("导航")
        page = st.sidebar.radio("选择页面：", ["用户信息", "数据分析", "词云展示"])
        if page == "用户信息":
            show_user_info(selected_folder)
        elif page == "数据分析":
            show_data_analysis(selected_folder)
        elif page == '词云展示':
            show_cloud(selected_folder)
    else:
        st.sidebar.title("基础设置")
        show_spider_setting()


if __name__ == '__main__':
    main()

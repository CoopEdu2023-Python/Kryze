import requests
import re
import json

url = 'https://www.douyin.com/user/MS4wLjABAAAAw6_Jq4rDqlUKujFUvw0mjwTE8Y4uYuqJoKIQWO43oBYTd5_FlhU3qZ-PbOS7MP35'

# Request headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'cookie': 'ttwid=1%7CZTHR8pWKsKjkItdpJdkIr_bp4kyLnu7MBfNsBkLNuY0%7C1699774704%7C69e14bcb296c63ffbfb255915332da39541a4df529c7c53f8fae4b772171ba85; passport_csrf_token=aa7b6cb15d5f6e0f0af939205002e6c7; passport_csrf_token_default=aa7b6cb15d5f6e0f0af939205002e6c7; s_v_web_id=verify_lov5z1vj_IzWWw5yI_oWaV_44Sx_9o8P_EkZih0xcTAts; dy_swidth=1707; dy_sheight=960; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; strategyABtestKey=%221703121248.363%22; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.5%7D; bd_ticket_guard_client_web_domain=2; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1707%2C%5C%22screen_height%5C%22%3A960%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A16%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; __ac_nonce=06583efb60096e7922daf; __ac_signature=_02B4Z6wo00f0134v3VgAAIDC4rRulye1vMd-D5HAALoTiffKQdBpQEHpX6YH5O-1.CWd4vc-Ec0.NUzOH.ktoV8s.3IDiX5XzYA4wgY59bByjKw6T21YBgZoqIhic9uKRCWUtGQPqwjci9FF93; csrf_session_id=029fc7504efca21b72b143c72f5630ff; home_can_add_dy_2_desktop=%221%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCTDRKbUJJUy9DT0taczJDTGZGTVllMnMyR0FuVVJzemxDRVNZMHZtRThuR01ycXpKTjZYM1hiam9rUHBseFJ2cEg1L1NKbjVWbFU4RFlOeVhZaHVQZTA9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; msToken=3SVKhMT4ywGhNd4bU1E_RqB18uzFSarKSHbq9WAh_qzsoVwd7GwoU2YDSDATV4BnYfF7VjLsHYBWl9Bn-Dj1JFCMrvfihIqwEGuyH82C0yTl087E-OUR77SUl2xI; msToken=0u5k-IKr7orBdWF0eYQ3XfrMsHN3GUxYVPjMma8fl-_RcSH9cV0DeITfJvr9RS3ywNXH2uUpkXpBKYh_5b-Yv7KQSj0XgYHjzrHr6p2OUZ8MRbJSGDCIFUughNbN; tt_scid=H-n1QonM61KS9cH9mnDFcWl5riT3zkLE85V0enaA9F4jkuXPcA6HvtGxEkYIawGPd9dc; download_guide=%223%2F20231221%2F0%22; pwa2=%220%7C0%7C3%7C0%22; IsDouyinActive=true'
}

# Get response and save
response = requests.get(url=url, headers=headers, timeout=5)

with open('raw/genshin.html', 'w', encoding='utf-8') as f:
    f.write(response.text)

# Assume required data is in RENDER_DATA
data = re.search(r'<script id="RENDER_DATA" type="application/json">(.*?)</script>', response.text).group(1)
data = requests.utils.unquote(data)

with open('raw/genshin_render_data.json', 'w', encoding='utf-8') as f:
    f.write(data)

# Extract information needed and save
data = re.search(r'\{(.*)\}', re.findall(r'self.__pace_f.push\((.*?)\)', response.text)[-1]).group(0).replace('\\', '')

with open('raw/genshin_target_data.json', 'w', encoding='utf-8') as f:
    f.write(data)

# To json
data_json = json.loads(data)

# Get name
real_name = data_json['user']['user']['realName']
print(real_name)
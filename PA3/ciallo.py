import re
import requests
from bs4 import BeautifulSoup
import json
import hashlib
import time

url = 'https://api.bilibili.com/x/space/wbi/arc/search?'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'cookie': 'buvid3=DB63C40D-0344-B088-B882-D3C7E046A72F91393infoc; b_nut=1698498791; CURRENT_FNVAL=4048; _uuid=7107AC658-108310-4110F-3BAC-6A1026B6A1091E72946infoc; buvid4=BB284D28-43F3-8557-6108-FEB1891A42A193574-023102821-paGIybps7qw3HWSFfsEs8w%3D%3D; rpdid=|(u~)YJ|)))u0J\'uYm)Rm)~mR; enable_web_push=DISABLE; header_theme_version=CLOSE; DedeUserID=1567113694; DedeUserID__ckMd5=f415c329ce53457e; CURRENT_QUALITY=80; PVID=1; buvid_fp_plain=undefined; LIVE_BUVID=AUTO3017020964209180; home_feed_column=5; browser_resolution=1707-838; fingerprint=fdc0d21e0476a2aa928e27445cff466a; buvid_fp=fdc0d21e0476a2aa928e27445cff466a; bp_video_offset_1567113694=875351503595896851; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDMyNTE4NTYsImlhdCI6MTcwMjk5MjU5NiwicGx0IjotMX0.G3Sn-hnVkOxA3_6010sy1rvpGVPpOxGoZcrqM3_R9Sg; bili_ticket_expires=1703251796; SESSDATA=6f89a7e5%2C1718709764%2C418a7%2Ac2CjC5q6cy8i-UoTpuw2hr3osCOxiciNSt-Co05QkIs6XqYxDBoIlHQ800M-QdsCqG_iASVmczYUR5VDVTZ3YxdjFFZWg1R3dzQl9lX3dtM1dkNFBVTU1nT2RGUlBjMEpuZ1YxdG9ZZVpxUC1vaUhJTWFPQXByM2pVSC1MUzEzSmVERWlGaU1oQ1dBIIEC; bili_jct=fc84243d362748651761f3a2c2978254; b_lsid=7A14D4C2_18C906F3A4B; sid=oosfgir5'
}
params = {
        'mid': '41883712',
        'pn' : '1',
        'ps': '30',
        'keyword': "",
        'order': "pubdate"
}

def web_rid(param):
    """js解密"""
    n = "7cd084941338484aae1ad9425b84077c" + "4932caff0ff746eab6f01bf08b70ac45"
    c = ''.join([n[i] for i in
                 [46, 47, 18, 2, 53, 8, 23, 32, 15, 50, 10, 31, 58, 3, 45, 35, 27, 43, 5, 49, 33, 9, 42, 19, 29, 28, 14,
                  39, 12, 38, 41, 13, 37, 48, 7, 16, 24, 55, 40, 61, 26, 17, 0, 1, 60, 51, 30, 4, 22, 25, 54, 21, 56,
                  59, 6, 63, 57, 62, 11, 36, 20, 34, 44, 52]][:32])
    s = int(time.time())
    param["wts"] = s
    param = "&".join([f"{i[0]}={i[1]}" for i in sorted(param.items(), key=lambda x: x[0])])
    return hashlib.md5((param + c).encode(encoding='utf-8')).hexdigest(), s

passwd = web_rid(params)
params['w_rid'] = passwd[0]
params['wts'] = passwd[1]
print(requests.get(url=url, params=params, headers=headers).text)
# response = requests.get(url=url, headers=headers).text
# with open("raw/demo.html", "w", encoding="utf-8") as file:
#     file.write(response)

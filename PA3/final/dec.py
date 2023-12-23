import hashlib
import time
import requests
import setup


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

url = 'https://api.bilibili.com/x/web-interface/nav'
raw = requests.get(url=url, headers=setup.Headers).json()
print(raw)
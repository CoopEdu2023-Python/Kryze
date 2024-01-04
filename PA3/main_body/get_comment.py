import time

import spider
import setup
import dec
import json
import sys


def analize_data(comment: json):
    _ = dict()
    print("content:", comment['content']['message'])
    print("like:", comment['like'])
    print('cid:', comment['rpid'])
    print('ctime: ', comment['ctime'])
    print('mid:', comment['member']['mid'])
    print('uname:', comment['member']['uname'])
    print("is_up_like:", comment['up_action']['like'])
    try:
        ip = comment['reply_control']['location']
    except:
        ip = 'unknown'
    print('ip:', ip)


arguments = sys.argv[1:]
oid = arguments[0]
page = arguments[1]
web_spider = spider.Spider()
web_spider.target_url = setup.reply_api
web_spider.headers = setup.Headers
params = setup.Params_reply
params['oid'] = oid
params['pn'] = page
passwd = dec.web_rid(params)
params['w_rid'] = passwd[0]
params['wts'] = passwd[1]
web_spider.params = params
reply_raw = web_spider.get_page().json()
for reply in reply_raw['data']['replies']:
    analize_data(reply)
    for sub in reply['replies']:
        analize_data(sub)
print(f'is_end: {reply_raw["data"]["cursor"]["is_end"]}')
print(f'count: {reply_raw["data"]["cursor"]["all_count"]}')
time.sleep(0.2)
import spider
import setup
import dec
import sys


arguments = sys.argv[1:]
uid = arguments[0]
page = arguments[1]
web_spider = spider.Spider()
web_spider.target_url = setup.Video_all_api
web_spider.headers = setup.Headers
params = setup.Params_find_video
params['mid'] = uid
params['pn'] = page
passwd = dec.web_rid(params)
params['w_rid'] = passwd[0]
params['wts'] = passwd[1]
web_spider.params = params
video_raw = web_spider.get_page().json()
print(video_raw)
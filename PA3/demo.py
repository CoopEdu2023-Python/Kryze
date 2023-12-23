import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# 设置 Chrome 选项
chrome_options = Options()
# chrome_options.add_argument("--headless")  # 无头模式，不打开浏览器界面

# 创建 WebDriver
driver = webdriver.Chrome(options=chrome_options)

# 打开网页
url = "https://www.bilibili.com/video/BV15v4y1u7VJ"  # 替换为你要爬取的网页地址
driver.get(url)
time.sleep(2)

# 获取页面源代码
page_source = driver.page_source

with open("raw/current_video_page.html", "w", encoding="utf-8") as file:
    file.write(page_source)

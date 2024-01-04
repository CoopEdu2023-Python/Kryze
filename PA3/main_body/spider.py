import requests
from bs4 import BeautifulSoup
import json


class Spider:
    def __init__(self):
        self.target_url = str()
        self.params = json
        self.headers = json

    def get_page(self):
        return requests.get(url=self.target_url, headers=self.headers, params=self.params)

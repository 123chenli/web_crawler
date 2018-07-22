import sys
import time
import urllib
import requests
from imp import reload
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf8')

url = 'https://book.douban.com/tag/?view=type'
wb_data = requests.get(url) # 请求网址
soup = BeautifulSoup(wb_data.text, 'lxml')
tags = soup.select('#content > div > div.article > div > div > tabl')
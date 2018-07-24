# # python爬去豆瓣网站图书
# # 1、GUI---展示数据
# # 2、采集图书信息
# from tkinter import *
# from tkinter import scrolledtext # 文本滚动条
# import urllib
# import re
#
# root = Tk() # 创建一个窗口
# root.title('豆瓣书库数据分析')
# root.geometry('800x800+100+200')
# # root.geometry('500*300') # 窗口大小
# text = scrolledtext.ScrolledText(root, font=('微软雅黑', 10)) # 增加滚动条
# text.grid() # 布局的方法
# button = Button(root, text='开始分析', font=('微软雅黑', 10))
# button.grid() # 实现布局
# varl = StringVar() # 设置变量，文字会发生改变,通过tk绑定一个变量
# label = Label(root, font=('微软雅黑', 10), fg='red', textvariable=varl) # Label是一个可以些文字的文本框，fg表示文字的颜色
# label.grid() # 实现布局，将文本框增加到root窗口中
# varl.set('准备中...')
# root.mainloop() # 进入消息循环，发送命令
# encoding: utf-8

import re
import requests
from bs4 import BeautifulSoup


def book(target_url):
    books = []
    book = requests.get(target_url)  # 使用request返回网页的整体结构
    soup = BeautifulSoup(book.text, 'lxml')  # 使用lxml作为解析器，返回一个Beautifulsoup对象
    table = soup.findAll('table', {'width': '100%'})  # 找到其中width=100%的标签，相当于找到所有的书
    for item in table:
        name = item.div.a.text.strip()
        r_name = name.replace('\n', '').replace(' ', '')
        tmp2 = item.div.span  # 判断书籍是否有别名，例如三体：地球往事”三部曲之一
        if tmp2:
            name2 = tmp2.text.strip().replace(':', '')
        else:
            name2 = r_name
        url = item.div.a['href']  # 获取书籍的链接
        info = item.find('p', {"class": "pl"}).text  # 获取书的信息
        score = item.find('span', {'class': 'rating_nums'}).text.strip()  # 获取书籍得分
        nums = item.find('span', {'class': 'pl'}).text.strip()  # 获取评价人数
        num = re.findall('(\d+)人评价', nums)[0]  # 通过正则取具体的数字
        if item.find('span', {'class': 'inq'}):  # 判断是否存在描述
            desc = item.find('span', {'class': 'inq'}).text.strip()
        else:
            desc = 'no description'
        books.append((r_name, name2, url, info, score, num, desc))  # 以元组的形式存入列表
    return books  # 返回一页的书籍


for n in range(10):
    url1 = 'https://book.douban.com/top250?start=' + str(n * 25)
    tmp = book(url1)
    with open('file/booktop250.xls', 'a', encoding='utf-8') as d:  # 新建一个booktop250的文件，在后面追加的形式（a）
        for i in tmp:
            print(i[0]+"\t"+i[1]+"\t"+i[2]+"\t"+i[3]+"\t"+i[4]+"\t"+i[5]+"\t"+i[6], file=d)
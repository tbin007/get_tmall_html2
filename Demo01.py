#!/usr/bin/env python
# 对比selenium 与 chrome请求和使用自定义有请求头的不同

from selenium import webdriver
from lxml import etree

import urllib

url = "http://192.168.18.20"


def get_html_selenium(u):
    option = webdriver.ChromeOptions()     # 定制chrome启动的属性
    option.add_argument("headless")

    browser = webdriver.Chrome(chrome_options=option)

    browser.get(u)
    html = browser.page_source
    browser.quit()
    selector = etree.HTML(html)
    img_urls = selector.xpath('//html/head/title/text()')
    for i in img_urls:
        print(i)


def get_html_add_header(u):   # 获取HTML
    try:
        header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/67.0.3396.62 Safari/537.36'}
        req = urllib.request.Request(u, headers=header)     # 将请求实例化为对象
        html = urllib.request.urlopen(req)                  # 使用定义好的对象来发送请求获取HTML代码
        html = html.read()
        return html                                    # 返回获取到的HTML代码
    except Exception as e:
        error = "获取页面失败"
        print(error + e)


get_html_selenium(url)
get_html_add_header(url)


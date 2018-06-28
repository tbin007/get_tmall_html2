#!/usr/bin/env python
# 爬取天猫网站指定位置的图片 v 2.0
# 通过selenium 与 chrome实现获取
# auth: TBin007

import urllib.request
import os
import csv
import datetime
import time
from lxml import etree
from selenium import webdriver


file_name = ".\\source\\id.csv"   # 指定数据源
mk_path = ".\\picture\\"    # 定义要创建的目录


def get_html(u):
    # 引入chrome_driver.exe
    try:
        option = webdriver.ChromeOptions()
        option.add_argument("headless")     # 设定为不打开浏览器
        browser = webdriver.Chrome(chrome_options=option)       # executable_path= 参数默认不填为当前目录
        browser.get(u)
        page_source = browser.page_source
        browser.quit()
        return page_source
    except Exception as e:
        print(e)


def get_img(h, n):      # 筛选出需要的内容
    selector = etree.HTML(h)
    img_urls = selector.xpath('//*[@id="J_ImgBooth"]/@src')  # 通过Xpath获取到需要的内容
    if img_urls:
        for i in img_urls:
            imgurl = "http:" + i
            urllib.request.urlretrieve(imgurl, '.\\picture\\%s.jpg' % n)   # 通过urlretrieve 方法存储需要的图片，并指定名称
            print("保存图片" + n + "成功")
            result = "保存图片" + n + "成功" + " " + imgurl
            return result
    else:
        print("未获取到指定的内容")
        result = "未获取到指定的内容"
        return result


def mk_dir(path):
    is_exists = os.path.exists(path)    # 判断是否存在
    if not is_exists:                   # 如果不存在就创建目录
        os.makedirs(path)               # 创建目录
        print(path + "创建目录成功")
        result = path + "创建目录成功"
        return result
    else:
        print(path + "目录已存在")  # 如果目录存在则不创建，并提示目录已存在
        now_time = datetime.datetime.now()
        result = path + "目录已存在" + str(now_time) + "\n"
        return result


if __name__ == '__main__':
    star_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(star_time + " " + "开始执行")
    file = open(".\\log\\log.txt", "a")  # 以可写打开存储日志的文件,如果没有就生成一个新的文件
    file.write(star_time + " " + "\n")
    log = mk_dir(mk_path)       # 创建用于保存图片的目录
    file.write(str(log) + "\n")      # 写入新建目录的记录
    with open(file_name, 'r') as f:
        reader = csv.reader(f)  # 读取文件
        for row in reader:
            if reader.line_num > 1:     # 由于数据源第一行是标题所以>1 才执行
                id = row[0].strip()     # 需要的id在数据源的第二列，所以获取下表为1 的值
                skuid = row[5].strip()
                goods_code = row[6].strip()
                url = ("https://detail.tmall.hk/hk/item.htm?id=%s&skuId=%s" % (id, skuid))
                html = get_html(url)
                img_log = get_img(html, goods_code)
                file.write(str(img_log) + "\n")      # 写入保存图片记录
                time.sleep(5)
    end_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    file.write(end_time + "\n")
    file.close()

    print(end_time + " " + "完成")

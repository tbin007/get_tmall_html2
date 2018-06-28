#!/usr/bin/env python
# 爬取天猫网站指定位置的图片 v 1.0
# auth: TBin007

import urllib.request
import os
import csv
import datetime
import time
from lxml import etree


file_name = ".\\source\\id.csv"   # 指定数据源
mk_path = ".\\picture\\"    # 定义要创建的目录


def get_html(u):   # 获取HTML
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


def get_img(h, n):   # 筛选出需要的内容
    selector = etree.HTML(h)
    img_urls = selector.xpath('//*[@id="J_ImgBooth"]/@src')  #通过Xpath获取到需要的内容
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


def mkdir(path):
    is_exists = os.path.exists(path) # 判断是否存在
    if not is_exists:    # 如果不存在就创建目录
        os.makedirs(path)   # 创建目录
        print(path + "创建目录成功")
        result = path + "创建目录成功"
        return result
    else:
        print(path + "目录已存在")  # 如果目录存在则不创建，并提示目录已存在
        now_time = datetime.datetime.now()
        result = path + "目录已存在" + str(now_time) + "\n"
        return result


if __name__ == '__main__':
    log = mkdir(mk_path)       # 创建用于保存图片的目录
    file = open(".\\log\\log.txt", "a")  # 以可写打开目标文件,如果没有就生成一个新的文件
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
                time.sleep(2)
    file.close()


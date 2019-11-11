#!/usr/bin/python3

import requests

# 5.将获取到的图片下载本地
import urllib


class PicOutputer(object):
    # 初始化集合
    def __init__(self):
        # 计数
        self.count = 0

    def out_picture(self, new_urls, keyword):
        print('已爬到关键词图片，现在开始下载到本地...')
        #print(len(new_urls),'==============',new_urls)

        print('正在保存' + keyword + '的第' + str(self.count+1) + '张图片，图片地址:' + str(new_urls))
        try:
            # 下载
            urllib.request.urlretrieve(new_urls,'./pic/%s.jpg' %(keyword + "_" + str(self.count)))
            self.count += 1
        except requests.exceptions.ConnectionError:
            print('【错误】当前图片无法下载--状态码：', new_urls.status_code)
            return


#!/usr/bin/python3

from spider_baidutup import url_manager, html_downloader, html_parser, pic_outputer
import requests

# 整个框架调度器
class SpiderMain(object):
    def __init__(self):
        # 文件名.类名
        self.urls = url_manager.UrlManager()  # url管理器
        self.downloader = html_downloader.HtmlDownloader()  # html下载器
        self.parser = html_parser.HtmlParser()  # html解析器
        self.outputer = pic_outputer.PicOutputer()  # 文件输出

    def spider(self,spider_url,keyword):
        print('正在查找 "' + keyword + '" 对应的图片，请稍后...')
        #print("搜索图片的链接： ", spider_url)

        # 下载 html源码
        result = self.downloader.download(spider_url)
        # print("网页源码：", result)

        # 解析源码中图片链接-得到很多url
        new_urls = self.parser.parse(result)

        # 将批量的图片链接全放到url管理器中
        self.urls.add_new_urls(new_urls)

        # 遍历下载数据
        while self.urls.has_new_url():  # 判断是否存在未爬取url？
            try:
                self.outputer.out_picture(self.urls.get_new_url(), keyword)
                print("总爬取量：", self.urls.get_urls_size(), "已爬取量：", self.urls.get_oldurl_size())

                if self.urls.get_urls_size() == self.urls.get_oldurl_size():
                    print("图片下载完成。请查看")
            except Exception as e:
                print('爬取失败--', e)

if __name__ == '__main__':
    # 获取关键字
    keyword = input("请输入想要搜索的图片关键字：")
    # 拼接形成链接url
    spider_url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + keyword + '&ct=201326592&v=flip'
    obj_spider = SpiderMain()
    obj_spider.spider(spider_url,keyword)



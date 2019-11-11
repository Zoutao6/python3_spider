import requests

# 2.下载器
class HtmlDownloader(object):

    # 最简单的下载做法
    def download(self, spider_url):
       try:
            response = requests.get(spider_url,timeout=10)
            # response = requests.post(spider_url, data=post_data, headers=headers)
            #print(response.apparent_encoding)  # 用来获得爬取的网站的编码，然后，在data字典的键值中指定编码：'张三'.encode('GB2312')
            if response.status_code == 200:     # 判断是否请求成功?
                # print(response.text)
                return response.text   # 返回源码内容
            else:
                print('请求失败，',response.status_code)  # 如果403-则添加headers
                return None
       except requests.RequestExceptione:
            print('url请求失败。')
            return None



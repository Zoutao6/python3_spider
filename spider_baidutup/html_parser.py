
import re
# 3.解析器
class HtmlParser(object):

    def __init__(self):
        self.urls = set()

    # 获取集合
    def _get_new_urls(self):
        return self.urls

    # 通过网页源码爬取url--这里更改过！
    def parse(self, html_cont):
        if html_cont is None:  # 判空
            return None
        # 这个地方把爬取URL地址都提出来，然后重新组合到了一个set当中去。去重！
        for addr in re.findall('"objURL":"(.*?)"', html_cont, re.S):  # 查找URL
            #print('正在爬取URL地址：' + str(addr))
            self.urls.add(addr)
        return self.urls



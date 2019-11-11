
# 4.URL管理器：管理器里面有两个集合。
class UrlManager (object):

    def __init__(self):
        self.new_urls = set()  # 两个集合记录要爬和已爬 url
        self.old_urls = set()

    # 添加填入的单个url
    # 判断链接不能为空，判断不能存在新链接和老链接
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls or self.old_urls:
            self.new_urls.add(url)   # 全新的url

    # 判断集合中是否存在未爬取url？
    def has_new_url(self):
        return len(self.new_urls)!=0

    # 添加批量urls
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    # 获取待爬取数量
    def get_newurl_size(self):
        return len(self.new_urls)

    # 获取已经爬取数量
    def get_oldurl_size(self):
        return len(self.old_urls)

    # 获取爬取的总数量
    def get_urls_size(self):
        return len(self.new_urls) + len(self.old_urls)

    # 获取新的url
    def add_new_urls(self, new_urls):
        if new_urls is None or len(new_urls) == 0:
            return
        for url in new_urls:
            # 调用子程序
            self.add_new_url(url)
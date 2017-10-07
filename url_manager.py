"""
URL管理器
"""
class UrlManager():

    def __init__(self):
        self.new_urls = set() #
        self.old_urls = set() #

    def add_new_url(self, url):
        '''
        向URL管理器中添加单个URL
        '''
        if url is None: #URL为空，不添加进URL管理器
            return
        if url not in self.new_urls and url not in self.old_urls: #如果URL即不存在于待抓取的URL集合中，也不存在于已抓取的URL集合中，则将其添加进待抓取的URL集合中
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        '''
        向URL管理器中批量添加URL
        '''
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        '''
        检查URL管理器中是否有待爬取的URL
        '''
        return len(self.new_urls) != 0

    def get_new_url(self):
        '''
        从URL管理器获取一个新的待爬取的URL
        '''
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

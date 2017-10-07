@author
"""
爬虫总调度
"""
import url_manager, html_downloader, html_parser, html_outputer

class SpiderMain():
    def __init__(self):
        """
        初始化所需要的各对象
        """
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()


    def craw(self, root_url):
        """
        爬虫调度程序
        """
        count = 1 #count用来记录当前爬取的URL的序数
        self.urls.add_new_url(root_url) #讲root_url添加进URL管理器
        while self.urls.has_new_url(): #循环获取待爬取的URL
            try:
                new_url = self.urls.get_new_url()
                print('craw %d : %s' % (count, new_url)) #打印当前爬取的URL序数以及具体URL地址
                html_cont = self.downloader.download(new_url) #下载new_url的页面
                new_urls, new_data = self.parser.parse(new_url, html_cont)#解析器解析新页面数据
                self.urls.add_new_urls(new_urls) #将获取到的新的URL添加进URL管理器
                self.outputer.collect_data(new_data) #将解析完的数据进行收集

                if count == 100: #设定限定条件，只爬取100个URL数据
                    break

                count = count + 1
            except: #异常（没有可用的数据或URL失效）处理
                print('---ERROR!\n---craw failed.')

        self.outputer.output_html()



if __name__=="__main__":
    root_url = "http://baike.baidu.com/item/Python" #将Python词条的URL作为爬虫的入口URL
    obj_spider = SpiderMain() #对象实例化
    obj_spider.craw(root_url) #启动爬虫

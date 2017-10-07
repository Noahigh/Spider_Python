"""
网页下载器
"""
from urllib import request

class HtmlDownloader():


    def download(self, url):
        if url is None:
            return

        response = request.urlopen(url)

        if response.getcode() != 200: #判断请求是否成功
            return None #请求失败，返回None

        return response.read() #返回下载好的内容

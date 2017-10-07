"""
网页解析器
"""
from bs4 import BeautifulSoup
import re
import urllib.parse

class HtmlParser():


    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"/item/\w"))
        for link in links:
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {} #用字典来存放数据

        # 记录URL
        res_data['url'] = page_url

        # <dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title_node = soup.find('dd', class_ = 'lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()
        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_ = 'lemma-summary')
        '''
        因为遇到多义词（URL地址标记为[?force=1]），会无法找到[lemma-summary]类，
        而且还不能确定哪一个关联度最大，以下几个解决方案：
        1/异常情况下直接赋值‘NULL’
        2/全部抓取，遇到上述情况就直接全部抓取，后期分析筛查数据，会造成无关数据过多的情况，对存储造成压力
        3/利用正则表达式将带[?force=1]标记的URL地址过滤掉，此方法同一方法一样，会对抓取数据的完整性造成伤害
        '''
        try:
            res_data['summary'] = summary_node.get_text()
        except:
            res_data['summary'] = 'NULL'

        return res_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None: #如果待解析的网址或者网页内容为空，则跳出当前函数
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

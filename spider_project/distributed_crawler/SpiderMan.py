from DATAOutPut import DataOutput
from HTMLDownloader import HtmlDownloader
from HTMLParser import HtmlParser
from URLManager import UrlManager

class SpiderMan(object):
    def __init__(self):
        self.manager=UrlManager()
        self.downloader=HtmlDownloader()
        self.parser=HtmlParser()
        self.output=DataOutput()

    def crawl(self,root_url):
        #添加入口url
        self.manager.add_new_url(root_url)
        #判断url管理器中是否有新的url，同时判断抓取了多少个url
        while(self.manager.has_new_url() and self.manager.old_url_size()<100):
            try:
                #从url管理器中获取新的url
                new_url=self.manager.get_new_url()
                #HTMl下载器下载网页
                html=self.downloader.download(new_url)
                #html解析器抽取网页数据
                new_urls,data=self.parser.parser(new_url,html)
                #将抽取的url添加到url管理器中
                self.manager.add_new_urls(new_urls)
                #数据存储器存储文件
                self.output.store_data(data)
                print('已经抓取了{}个链接'.format(self.manager.old_url_size()))
            except Exception as e:
                print('crawl failed',e)

        self.output.output_html()


if __name__=='__main__':
    spider_main=SpiderMan()
    spider_main.crawl("http://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB")

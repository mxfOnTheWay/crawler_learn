import pickle
import hashlib

class UrlManager(object):
    def __init__(self):
        self.new_urls=self.load_progress('new_urls.txt')#未爬取url集合
        self.old_urls=self.load_progress('old_urls.txt')#已爬取url集合

    def has_new_url(self):
        #判断是否有未爬取的url
        return self.new_url_size()!=0

    def get_new_url(self):
        #获取一个未爬取的url
        new_url=self.new_urls.pop()
        m=hashlib.md5()
        m.update(new_url.encode('utf-8'))
        self.old_urls.add(m.hexdigest()[8:-8])
        return new_url

    def add_new_url(self,url):
        #将新的单个url添加到未爬取的url集合中
        if url is None:
            return
        m=hashlib.md5()
        m.update(url.encode('utf-8'))
        url_md5=m.hexdigest()[8:-8]
        if url not in self.new_urls and url_md5 not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self,urls):
        #将新的批量url添加到未爬取的url集合中
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.add_new_url(url)

    def new_url_size(self):
        #获取未爬取的集合大小
        return len(self.new_urls)

    def old_url_size(self):
        #获取已爬取的集合大小
        return len(self.old_urls)

    def save_progress(self,path,data):
        '''保存进度，path为文件路径，data为数据'''
        with open(path,'wb') as f:
            pickle.dump(data,f)

    def load_progress(self,path):
        '''从本地加载进度，path为文件路径,返回set集合'''
        print('[+] 从文件加载进度：{}'.format(path))
        try:
            with open(path,'rb') as f:
                tmp=pickle.load(f)
                return tmp

        except:
            print('[!]无进度文件，创建：{}'.format(path))

        return set()

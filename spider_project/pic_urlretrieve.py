import urllib.request
import requests
from lxml import etree

def Schedule(blocknum,blocksize,totalsize):
    per=100.0*blocknum*blocksize/totalsize
    if per>100:
        per=100
    print('当前下载进度{}%'.format(per))

user_agent='User-Agent,Mozilla/5.0'
headers={'user-agent':user_agent}
url='http://www.ivsky.com/tupian/ziranfengguang/'
r=requests.get(url,headers=headers)
html=etree.HTML(r.text)
img_urls=html.xpath('.// img/@src')
i=0
for img_url in img_urls:
    urllib.request.urlretrieve(img_url,'/Users/sun-dream/'+'img'+str(i)+'.jpg',Schedule)
    i+=1
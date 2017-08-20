import requests
from bs4 import BeautifulSoup
import re

user_agent='User-Agent,Mozilla/5.0'
headers={'user-agent':user_agent}
url='http://www.ivsky.com/tupian/ziranfengguang/'
r=requests.get(url,headers=headers)
html=BeautifulSoup(r.text,"lxml")

pic_tag=html.find_all('img')



i=0
for img_url in pic_tag:
    print(img_url.get('src'))
    with open('/Users/sun-dream/'+'img'+str(i)+'.jpg','wb') as f:
        print('/Users/sun-dream/'+'img'+str(i)+'.jpg')
        r1=requests.get(img_url.get('src'))
        f.write(r1.content)
        i+=1

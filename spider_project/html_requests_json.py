import requests
from bs4 import BeautifulSoup
import json

user_agent='User-Agent,Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'

headers={'user-gent':user_agent}

def url_text():
    try:
        url='http://seputu.com/'
        r=requests.get(url,headers=headers)
        r.raise_for_status()
        r.encoding=r.apparent_encoding


    except Exception as e:
        print(e)
    return r.text

def find_data(text):

    soup=BeautifulSoup(text,'html.parser')
    content=[]
    for mulu in soup.find_all(class_="mulu"):
        h2=mulu.find('h2')
        if h2!=None:
            h2_title=h2.string
            list=[]
            for a in mulu.find(class_='box').find_all('a'):
                href=a.get('href')
                box_title=a.get('title')
                list.append({'href':href,'box_title':box_title})
            content.append({'title':h2_title,'content':list})
    with open('daomubiji.json','w') as f:
        json.dump(content,f)


text=url_text()
find_data(text)
with open('daomubiji.json', 'r') as f:
    data=json.loads(f.read())
    print(data)





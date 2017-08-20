import requests,json
from bs4 import BeautifulSoup

def getHtmlText(url):
    user_agent='User-Agent,Mozilla/5.0'
    headers={'User-Agent':user_agent}
    try:
        response=requests.get(url,headers=headers)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(e)


def getContent(text):
    try:
        soup =BeautifulSoup(text,"html.parser")
        content=[]
        for mulu in soup.find_all(class_='mulu'):
            h2 = mulu.find('h2')
            if h2!=None:
                h2_title=h2.string
                list=[]
                for a in mulu.find(class_='box').find_all('a'):
                    href=a.get('href')
                    box_title=a.get('title')
                    list.append({'href':href,'box_title':box_title})
                content.append({'title':h2_title,'content':list})
        with open('meng.text','w') as f:
            f.write(json.dumps(content))
    except Exception as e:
        print(e)

if __name__=='__main__':
    url='http://www.rulianshi.org/'
    text=getHtmlText(url)
    getContent(text)
    with open('meng.text','r') as f:
        data=json.loads(f.read())
        print(data)

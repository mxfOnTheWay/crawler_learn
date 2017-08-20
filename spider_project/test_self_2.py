import requests,re
from bs4 import BeautifulSoup
from urllib import parse
url="http://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB"

user_agent = 'User-Agent,Mozilla/5.0'
headers = {'user-agent': user_agent}
r = requests.get(url, headers=headers)
r.raise_for_status()
r.encoding = r.apparent_encoding
soup=BeautifulSoup(r.text,'html.parser',from_encoding='utf-8')
#links=soup.find_all('a',href="/item/%E5%BC%80%E6%94%BE%E6%BA%90%E4%BB%A3%E7%A0%81")
links=soup.find_all('a',href=re.compile('/item/.*'))

#links=soup.find_all('a',href=re.compile(r'/item/（.*？）'))
print(links)
for link in links:

    new_url=link['href']
    print(new_url)
    # page_url='http://baike.baidu.com'
    # new_full_url = parse.urljoin(page_url, new_url)
    # print(new_full_url)
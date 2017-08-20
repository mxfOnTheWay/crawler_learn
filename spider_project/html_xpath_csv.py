import requests,re,csv
from lxml import etree

def getHTMLurl(url):
    user_agent='User-Agent,Mozilla/5.0'
    headers={'user-agent':user_agent}
    try:
        r=requests.get(url,headers=headers)
        r.raise_for_status()
        return r.text
    except Exception as e:
        print(e)


def csv_write(text):

    try:
        html=etree.HTML(text)
        div_mulus=html.xpath('.//*[@class="mulu"]')
        rows = []
        for div_mulu in div_mulus:
            div_h2=div_mulu.xpath('./div[@class="mulu-title"]/center/h2/text()')

            if len(div_h2)>0:
                h2_title=div_h2[0]

                a_s=div_mulu.xpath('./div[@class="box"]/ul/li/a')
                for a in a_s:
                    href=a.xpath('./@href')[0]
                    box_title=a.xpath('./@title')[0]
                    pattern=re.compile(r'\s*\[(.*)\]\s+(.*)')
                    match=pattern.search(box_title)
                    if match!=None:
                        date=match.group(1)
                        real_title=match.group(2)
                        content=(h2_title,real_title,href,date)
                        #print(content)
                        rows.append(content)
        headers=['title','real_title','href','date']
        with open('daomubiji.csv','w') as f:
            f_csv=csv.writer(f)
            f_csv.writerow(headers)
            f_csv.writerows(rows)

    except Exception as e:
        print('2',e)




url='http://seputu.com/'
text=getHTMLurl(url)
csv_write(text)
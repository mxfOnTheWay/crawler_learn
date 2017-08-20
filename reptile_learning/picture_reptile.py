import urllib.request,re

keyname="短裙"
key=urllib.request.quote(keyname)
headers=("user-agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:49.0) Gecko/20100101 Firefox/49.0")
opener=urllib.request.build_opener()
opener.add_handlers=[headers]
urllib.request.install_opener(opener)

for i in range(0,1):
    url="https://s.taobao.com/list?spm=a21bo.50862.201867-links-0.6.5dcec6f7PBATBQ&q="+key+"&cat=16&style=grid&seller_type=taobao&bcoffset=12&s="+str(i*60)
    data =urllib.request.urlopen(url).read().decode("utf-8","ignore")
    print(len(data))
    pat='pic_url":"//(.*?)"'
    imageurllist=re.compile(pat).findall(data)
    for j in range(0,len(imageurllist)):
        this_image = imageurllist[j]
        this_image_url ="http://"+this_image
        file="/Users/sun-dream/sinanews/"+str(i)+str(j)+".jpg"
        urllib.request.urlretrieve(this_image_url,filename=file)

import urllib.request,re

url="http://blog.csdn.net"
headers=("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
#data=opener.open(url).read().decode("utf-8","ignore")
data=urllib.request.urlopen(url).read().decode("utf-8","ignore")
print(len(data))

data_decode=data.decode("utf-8","ignore")
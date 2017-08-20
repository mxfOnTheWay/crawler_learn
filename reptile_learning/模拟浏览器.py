import urllib.request
url="https://mail.qq.com/cgi-bin/frame_html?sid=YycNBUvJ2rXqd0wV&r=b4e03ae4cb94b20b9fbeba94b77cf3fe"
headers=("user-agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
opener=urllib.request.build_opener()
opener.add_handlers=[headers]
data=opener.open(url).read()
fh=open("/Users/sun-dream/test1.html","wb")
fh.write(data)
fh.close()

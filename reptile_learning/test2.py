import urllib.request,urllib.error
try:
    data=urllib.request.urlopen("http://udn.com/news/index").read()
except urllib.error.URLError as e:
    if hasattr(e,"code"):
        print(e.code)
    if hasattr(e,"reason"):
        print(e.reason)
except Exception as e:
    print(e)
else:
    print(data.decode())
    print(len(data))
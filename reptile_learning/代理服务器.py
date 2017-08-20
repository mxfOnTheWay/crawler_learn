import urllib.request

#建立代理服务器函数
def use_proxy(url,proxy_addr):
    proxy=urllib.request.ProxyHandler({"http":proxy_addr})
    opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data=urllib.request.urlopen(url).read().decode("utf-8","ignore")
    #data=opener.open(url).read().decode("utf-8","ignore")
    return data


proxy_addr="222.194.14.130:808"
url="http://www.baidu.com"
data=use_proxy(url,proxy_addr)
#print(data)
print(len(data))
import urllib.request,re,urllib.error


data=urllib.request.urlopen("http://news.sina.com.cn/").read()
data_decode=data.decode("utf-8","ignore")

pat='href="(http://news.sina.com.cn/.*?)>"'
allurl = re.compile(pat).findall(data_decode)
print(len(allurl))
for i in range(0,len(allurl)):
    try:
        print("第"+str(i)+"次爬取")
        thisurl=allurl[i]

        file ="/Users/sun-dream/sinanews/"+str(i)+".html"

        urllib.request.urlretrieve(thisurl,file)
        print("---成功----")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    except Exception as e:
        print(e)
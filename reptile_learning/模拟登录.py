import  urllib.request,urllib.parse

url="https://passport.cnblogs.com/user/signin?"
mydata=urllib.parse.urlencode({
    "input1":"孟向锋在路上",
    "input2":"mxf_160505"
}).encode("utf-8")

rep=urllib.request.Request(url,mydata)

data=urllib.request.urlopen(rep).read()
fh=open("/Users/sun-dream/test.html","wb")
fh.write(data)
fh.close()

#import  urllib

# from urllib.request import urlopen
# data1=urlopen("http://www.baidu.com").read()
# print(data1.decode())
# file = open("test_reptile_data_baidu","w")
# file.write(data1.decode('utf-8'))
# file.close()
# print(len(data1))

from urllib  import request


data3 =request.urlopen("http://jd.com").read()
print(len(data3))
print(data3.decode())
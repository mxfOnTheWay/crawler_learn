import  time
a=time.time() #获取时间戳
time.sleep(1)#睡几秒
time.gmtime()#将时间戳转换成utc区的时间元组
print(time.gmtime(3748484484))
print(a)
time.localtime()#到本地时间元组

print(a/60/60/24/365)

print(time.localtime())

print(time.timezone/3600)
print(time.daylight)
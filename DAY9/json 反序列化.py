
import json

f = open("test.text","r")

#data =eval(f.read() )#eval 不是通用的办法

data = json.loads(f.read())
print(data)
print(data['age'])
f.close()
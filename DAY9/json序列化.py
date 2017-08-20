
import  json


def sayhi(name):
    print("hello,",name)

info ={
    'name':'alex',
    'age':22,
    'func':sayhi
}

f = open("test.text","w")

#print(json.dumps(info))
f.write(json.dumps(info))

f.close()
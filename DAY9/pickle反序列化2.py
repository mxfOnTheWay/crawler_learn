#coding: utf-8
import pickle

def sayhi(name):
    print("hello,",name)

f = open("test.text","rb")

#data =eval(f.read() )#eval 不是通用的办法

#data = pickle.loads(f.read())

data = pickle.load(f)
print(data)
print(data['age'])
f.close()
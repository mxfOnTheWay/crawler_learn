import time
#1、无参数
# def  decorate(func):#定义一个装饰器函数，其参数为一个函数（这里会传入原函数）
#     def inner():
#         print("在原函数前增加的功能")
#         func()
#         print("在原函数后增加的功能")
#     return inner
#
# @decorate  #相当于original=decorate(original)
# def original():
#     print("我是原函数")
#
# original()

#2、有参数
# import time
# def  decorate(func):#定义一个装饰器函数，其参数为一个函数（这里会传入原函数）
#     def inner(*args,**kwargs):
#         print("在原函数前增加的功能")
#         func(*args,**kwargs)
#         print("在原函数后增加的功能")
#     return inner
#
# @decorate  #相当于original=decorate(original)
# def original(name):
#     print("我是原函数，%s"%name)
#
# original("meng")


#3、有返回参数
# import time
# def  decorate(func):#定义一个装饰器函数，其参数为一个函数（这里会传入原函数）
#     def inner(*args,**kwargs):
#         print("在原函数前增加的功能")
#         res =func(*args,**kwargs)
#         print("在原函数后增加的功能")
#         return res
#     return inner
#
# @decorate  #相当于original=decorate(original)
# def original(name):
#     print("我是原函数，%s"%name)
#     return "python"
#
# print(original("meng"))


#4、装饰器本身带参数
import time
def  decorate(decorate_type):#定义一个装饰器函数，其参数为一个函数（这里会传入原函数）
    def outer(func):
        def inner(*args,**kwargs):
            if decorate_type=="1":

                print("在原函数前增加的功能")
                res =func(*args,**kwargs)
                print("在原函数后增加的功能")
                return res
            elif decorate_type =="2":

                print("强制结束")
        return inner
    return outer

@decorate(decorate_type="1")  #相当于original=decorate(original)
def original(name):
    print("我是原函数，%s"%name)
    return "python"

@decorate(decorate_type="2")
def original2(name):
    print("我是原函数，%s"%name)
    return "python"

print(original("meng"))
print(original2("li"))

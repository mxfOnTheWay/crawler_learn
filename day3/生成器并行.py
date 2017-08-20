import time

def consumer(name):
    print("%s 准备吃包子了"%name)
    while True:
        baozi = yield

        print ("包子[%s]来了，被[%s]吃了"%(baozi,name))

# c=consumer("meng")
# c.__next__()
# c.__next__()
# c.__next__()
# c.send("韭菜馅")
# c.__next__()
def producter(*args):
    c = consumer(args[0])
    c2= consumer(args[1])
    c.__next__()
    c2.__next__()
    print("准备做包子了")
    for i in range(10):
        time.sleep(1)
        print("做了一个包子")
        if i%2==0:
            c.send(i+1)
        else:
            c2.send(i+1)


producter("meng","li")
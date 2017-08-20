import time


def consumers(name):
    print("%s 吃包子了"%name)
    while True:
        baozi =yield

        print("baozi %s 来了，被%s吃了"%(baozi,name))


def producter(name):
    c=consumers("A")
    c2=consumers("B")
    c.__next__()
    c2.__next__()

    print("准备做包子了")
    for i in range(10):
        time.sleep(1)
        print("做了一个包子")
        c.send(i)
        c2.send(i)

producter("lili")


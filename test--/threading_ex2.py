import threading,time

# def run(n):
#     print("task",n)
#     time.sleep(3)
#
#
# t1=threading.Thread(target=run,args=("t1",))
# t2=threading.Thread(target=run,args=("t2",))
# t1.start()
# t2.start()

class MyThread(threading.Thread):
    def __init__(self,n):
        super(MyThread,self).__init__()
        self.n=n

    def run(self):
        print("runnint task",self.n)
        time.sleep(2)

t1=MyThread("t1")
t2=MyThread("t2")

t1.start()

t2.start()
t1.join()
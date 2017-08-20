import threading,time

def run(n):
    print("task",n)
    time.sleep(2)
    print("task done",n)

start_time=time.time()
for i in range(50):
    t=threading.Thread(target=run,args=("t-%s"%i,))

    t.start()

print("---- all threads had fineshed")
print("cost:",time.time()-start_time)


import socket
import os
server = socket.socket()
server.bind(("localhost",6969))#绑定要监听的对象
server.listen(0) #监听

print("I am waiting the phone")
while True:
    conn,addr =server.accept()

    print(conn,addr)

    print("the phone comming")
    while True:
        data=conn.recv(1024)

        print("recv:",data.decode())

        if not data:
            print("client has lost")
            break
        res = os.popen(data).read()
       # conn.send(data.upper())
        conn.send(res)  #conn.sendall(res

server.close()
import socket
import os
server = socket.socket()
server.bind(("localhost",9999))

server.listen(5)

while True:
    conn,addr=server.accept()
    print("new conn:",addr)

    while True:
        data = conn.recv(1024)
        if not data:
            print("clint not on line")
            break

        print("执行指令：",data)
        cmd_res=os.popen(data.decode()).read()# 接收字符串，执行结果也是字符串
        print("before send",len(cmd_res))
        if len(cmd_res)==0:
            cmd_res="cmd has no output..."
        conn.send(str(len(cmd_res)).encode("uft-8"))
        conn.send(cmd_res.encode("utf-8"))
        print("send done`")

server.close()
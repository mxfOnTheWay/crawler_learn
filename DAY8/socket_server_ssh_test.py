import socket,os,time

server =socket.socket()#建立socket对象

server.bind(("localhost",9999))#建立服务器端的监听对象

server.listen(5)#监听 并设立最大监听数

while True:
    print("等待新指令")
    conn,addr=server.accept()  #阻塞
    print("conn:",addr)
    while True:
        data = conn.recv(1024)  #接收数据
        if not data:
            print("客户端已断开")
            break
        print("执行指令：",data)
        cmd_res =os.popen(data.decode()).read()#接收字符串，执行结果也是字符串
        print("before send",len(cmd_res))
        if len(cmd_res)==0:
            cmd_res="cmd has no output..."

        conn.send(str(len(cmd_res.encode())).encode("utf-8"))
       # time.sleep(5)
        client_ack =conn.recv(1024)#等待确认，不收到就不向下执行
        print("收到结果为：",client_ack.decode("utf-8"))
        conn.send(cmd_res.encode("utf-8"))
        print("send done")

server.close()

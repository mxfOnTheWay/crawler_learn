import socket

client = socket.socket()  #建立socket对象

client.connect(("localhost",9999))#建立连接
while True:
    cmd=input(">>:").strip()#输入接收的内容
    if len(cmd) ==0:continue
    client.send(cmd.encode("utf-8"))#发送到服务器，注意转码
    cmd_res_size = client.recv(1024) #接收命令结果的长度
    print("命令结果大小：",cmd_res_size.decode())

    client.send("准备好接收了，可以发了".encode("utf-8"))
    received_size = 0
  #  received_data=b''
    while received_size < int(cmd_res_size.decode()):
        data = client.recv(1024)
        received_size += len(data) #每次收到的有可能小于1024，所以用len判断
     #   cmd_res=client.recv(1024)#接收返回的结果
        print(data.decode())
        print(received_size)
    else:
        print("cmd res receive done...",received_size)

client.close()#客户端关闭

import  socket

client = socket.socket()

client.connect(('localhost',9999))

while True:
    cmd = input(">>:").strip()
    if len(cmd)==0:continue
    client.send(cmd.encode("utf-8"))
    cmd_res_size = client.recv(1024)##接收命令结果的长度
    print("命令结果大小：",cmd_res_size)


    cmd_res =client.recv(1024)

    print(cmd_res)


client.close()
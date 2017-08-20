import socket

client = socket.socket()

client.connect(("localhost",8081))

client.send(b"hey")

client.close()

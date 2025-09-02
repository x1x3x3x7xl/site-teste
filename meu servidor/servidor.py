import socket

host = "177.52.51.71"  
port = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

while True:
    msg = input("Digite algo: ")
    client.send(msg.encode())
    data = client.recv(1024).decode()
    print("Resposta do servidor:", data)

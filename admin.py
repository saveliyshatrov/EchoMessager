import socket
import json

host = '0.0.0.0'
port = 5000
size = 1024
message = ''

client = {
    'username': 'Admin',
    'host': '0.0.0.0',
    'port': '5000',
    'message': '',
    'to': 'Server'
}

while message != 'quit':

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    CommandList = "1. Users in network"
    print(CommandList)

    client['message'] = input("Enter number command: ")

    s.connect((host,port)) 
    s.send(str(client).encode())
    data = s.recv(size)
    Info = (data.decode()).replace("'", '"')
    #print(Info)
    info = json.loads(Info)
    s.close()
    print(info)
import socket

host = '0.0.0.0'
port = 5000
size = 1024
message = ''

client = {
    'username': 'time_bitch',
    'host': '0.0.0.0',
    'port': '5000',
    'message': '',
    'to': ''
}

while message != 'quit':

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client['to'] = input("Enter username: ")
    client['message'] = input("Enter message: ")

    s.connect((host,port)) 
    s.send(str(client).encode())
    data = s.recv(size)
    array = (data.decode())
    print(array)

print('Quit')
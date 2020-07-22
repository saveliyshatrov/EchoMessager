import socket
import json

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

host = '0.0.0.0'
port = 5000
size = 1024
x = 1

dictOfUsers = {}

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host,port))
s.listen(1)

while x == 1:
    client, address = s.accept()
    ADDRESS = json.dumps(address)
    print('address: {}'.format(address))
    Client = client.recv(size).decode().replace("'", '"')
    Client = json.loads(Client)
    print('{} connected and messege: {}'.format(Colors.OKBLUE + Colors.BOLD + Client['username'] + Colors.ENDC, Colors.OKGREEN + Client['message'] + Colors.ENDC))
    dictOfUsers[Client['username']] = {
        "ip": str(address[0]),
        "port": str(address[1])
    }
    if Client['username'] == 'Admin':
        if Client['to'] == 'Server':
            if Client['message'] == '1':
                client.send((str(dictOfUsers)).encode())
    
    #elif Client:
    elif Client:
        #s.accept() = client, tuple(str(dictOfUsers[Client['to']]['ip']), int(dictOfUsers[Client['to']]['port']))
        s.sendto('sdhfbds', (str(dictOfUsers[Client['to']]['ip']), int(dictOfUsers[Client['to']]['port'])))
        client.send(('recieved').encode())
    client.close()

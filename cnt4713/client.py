# William Valido
# 3354913
# Professor: Alex Afanasyev
# Class: CNT4713 RVC 1208

import socket, sys, os

class Client:
    def __init__(self, sock=None, timeout=10):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     
            self.sock.settimeout(timeout)
        else:
            self.sock = sock

    def connect(self, host, port):
        if(port in range(0, 65535)):
            serverAddress = (host, port)
        else:
            sys.stderr.write("ERROR: (port must be 0-65535.)")
            exit(1)
        
        try:
            self.sock.connect(serverAddress)
        except socket.error:
            sys.stderr.write("ERROR: (Error: connection could not be stablished.)")
            exit(1)

    def receiveMessage(self, size):
        try:
            return self.sock.recv(size).decode('utf-8')
        except socket.timeout:
            sys.stderr.write("ERROR: (Error: timed out)")
            exit(1)

    def sendMessage(self, msg):
        self.sock.sendall(msg)
        
args = sys.argv[1:]

hostname = args[0]
port = int(args[1])
filename = args[2]

file = open(filename,  'rb')
contents = file.read(os.path.getsize(filename))

client = Client()
client.connect(hostname, port)
    
recv = client.receiveMessage(16)

if (recv == 'accio\r\n'):
    client.sendMessage(contents)

client.sock.close()
exit(0)
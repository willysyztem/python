import socket
import sys

global host
global port
global s


def socketCreate():
    global host
    global port
    global s

    host = "0.0.0.0"
    port = int(sys.argv[1])

    # checks to see if the port is within allowed range
    if port not in range(0, 65535):
        sys.stderr.write("Error: (port number not in range)")
        sys.exit(1)
    s = socket.socket()


def socketBind():
    global host
    global port
    global s

    s.bind((host, port))
    s.listen(10)


def socketAccept():
    connection, address = s.accept()
    connection.settimeout(10.0)

    socketSend(connection)
    socketRecv(connection)
    connection.close()


def socketSend(connection):
    # only accio\r\n is send
    connection.send(str.encode("accio\r\n"))


def socketRecv(connection):
    totalData = 0
    while True:
        data = len(connection.recv(1024))
        if not data:
            break
        totalData += data
    print(totalData)


def main():
    socketCreate()
    socketBind()

    allowedConnections = 10
    totalConnected = 0

    while totalConnected < allowedConnections:
        try:
            socketAccept()
        except socket.timeout:
            sys.stderr.write("Error\n")
        totalConnected += 1


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main()
    else:
        sys.stderr.write("Run with arguments >> python server-s.py <PORT>")
        sys.exit(1)

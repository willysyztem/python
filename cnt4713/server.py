import socket
import sys
import os

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


def socketAccept(connID):
    conn, address = s.accept()
    conn.settimeout(10.0)

    # print(f"Connected to {address[0]} on port {address[1]}")
    socketSend(conn)
    socketRecv(conn, connID)
    conn.close()


def socketSend(conn):
    # only accio\r\n is send
    conn.send(str.encode("accio\r\n"))


def socketRecv(conn, connID):
    totalData = ""
    while True:
        data = conn.recv(2048).decode("utf-8")
        if not data:
            break
        totalData += data
    writeToFile(totalData, connID)


def writeToFile(totalData, connID):
    path = sys.argv[2][1:]
    try:
        os.mkdir(path)
    except OSError:
        pass  # not handling if path created already exist.

    path = f"{path}/{connID}"
    filename = open(path, "w")
    filename.write(totalData)
    filename.close()


def main():
    socketCreate()
    socketBind()

    allowedConnections = 10
    connection = 0

    while connection <= allowedConnections:
        connection += 1
        try:
            # print(f"Waiting for connection: {connection}")
            socketAccept(connection)
        except socket.timeout:
            sys.stderr.write("Error\n")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main()
    else:
        sys.stderr.write("Run with arguments >> python server-s.py <PORT>")
        sys.exit(1)

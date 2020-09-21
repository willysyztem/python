import socket
import sys

global host
global port
global connection


def socketCreate():
    global host
    global port
    global connection

    host = sys.argv[1]
    port = int(sys.argv[2])

    # checks to see if the port is within allowed range
    if port not in range(0, 65535):
        sys.stderr.write("Error: (port number not in range)")
        sys.exit(1)
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.settimeout(10.0)
    connection.connect((host, port))


def socketReceive():
    global connection
    response = ""
    while "accio\r\n" not in response:
        chunk = connection.recv(1).decode("utf-8")
        if not chunk:
            break
        response += chunk


def socketSend():
    global connection
    filename = sys.argv[3]
    f = open(filename, "rb")
    while True:
        data = f.read(2048)
        if not data:
            break
        connection.sendall(data)


def main():
    try:
        socketCreate()
        socketReceive()
        socketSend()
    except socket.gaierror:
        sys.stderr.write("Error: (connection could not be established.)")
        sys.exit(1)
    except socket.timeout:
        sys.stderr.write("Error:(connection has timed out")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main()
    else:
        sys.stderr.write("Run with arguments >> python client.py <IP ADDRESS> <PORT> <FILENAME>")
        sys.exit(1)


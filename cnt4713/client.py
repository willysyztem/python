# William Valido
# 3354913
# Professor: Alex Afanasyev
# Class: CNT4713 RVC 1208

import socket, sys, os
        
def main():
    args = sys.argv[1:]

    hostname = args[0]
    port = int(args[1])
    filename = args[2]

    file = open(filename, "rb")
    data = file.read(os.path.getsize(filename))

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        if(port in range(0, 65535)):
            s.connect((hostname, port))
            s.settimeout(10)
        else:
            sys.stderr.write("ERROR: (port must be 0-65535.)")
            exit(1)
        
        recv = s.recv(16)
        if (recv == "accio\r\n"):
            s.sendall(data)

    except socket.error:
        sys.stderr.write("ERROR: (Error: connection could not be stablished.)")
        exit(1)
    except socket.timeout:
        sys.stderr.write("ERROR: (Error: timed out)")
        exit(1)
    finally:
        file.close()
        s.close()

if __name__ == "__main__":
    main()
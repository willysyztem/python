# William Valido
# 3354913
# Professor: Alex Afanasyev
# Class: CNT4713 RVC 1208

import socket, sys, os, time
        
def main():
    args = sys.argv[1:]

    hostname = args[0]
    port = int((args[1]))
    filename = args[2]
    
    file = open(filename, 'rb')
    timeout = 10.0

    try:
        if(port not in range(0, 65535)):
            sys.stderr.write("ERROR: (port must be 0-65535.)")
            exit(1)
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        s.connect((hostname, port))
        reply = s.recv(16)
        
        if(reply == "accio\r\n"):
            while True:
                data = file.read(1024)
                if not data:
                    break
                s.sendall(data)
    
    except socket.timeout:
        sys.stderr.write("ERROR: (Error: timed out)")
        exit(1)
    except socket.error:
        sys.stderr.write("ERROR: (Error: connection could not be stablished.)")
        exit(1)
    finally:
        file.close()
        s.shutdown(socket.SHUT_RDWR)
        s.close()

if __name__ == "__main__":
    main()
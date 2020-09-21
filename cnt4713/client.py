# William Valido
# 3354913
# Professor: Alex Afanasyev
# Class: CNT4713 RVC 1208
# Accio Client

import socket, sys
        
def main():
    args = sys.argv[1:]

    hostname = args[0]
    port = int((args[1]))
    filename = args[2]
    
    if(port not in range(0, 65535)):
        sys.stderr.write("ERROR: (port must be 0-65535.)")
        sys.exit(1)

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 2048)
        s.settimeout(10)
        s.connect((hostname, port))

        response = ""
        while "accio\r\n" not in response:
            chunk = s.recv(1).decode("utf-8")
            response += chunk
            
        #print("Message from server: \n {}".format(reply))
        if(response == "accio\r\n"):
            with open(filename, "rb") as file:
                data = file.read(2048)
                while data:
                    s.send(data)
                    data = file.read(2048)
    except socket.timeout:
        sys.stderr.write("ERROR: (Error: timed out)")
        sys.exit(1)
    except socket.gaierror:
        sys.stderr.write("ERROR: (Error: connection could not be stablished.)")
        sys.exit(1)
    
    s.close()
    sys.exit(0)

if __name__ == "__main__":
    main()
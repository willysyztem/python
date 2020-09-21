# William Valido
# 3354913
# Professor: Alex Afanasyev
# Class: CNT4713 RVC 1208
# Accio Simplified Server

import socket, sys, time

def main():

    port = int(sys.argv[1])
    allowedConnections = 10
    totalConnected = 0

    if(port not in range(0, 65535)):
        sys.stderr.write("ERROR: (port must be 0-65535.)")
        exit(1)
    
    s = socket.socket()
    s.bind(("0.0.0.0", port))
    s.listen(10)
    
    while totalConnected < allowedConnections:
        #print("Waiting for connection...")
        try:
            totalData = 0
            connection, address = s.accept()
            #print("Connected to {} on port {}".format(address[0], address[1]))
            connection.settimeout(10)

            connection.send(str.encode("accio\r\n"))
            
            while True:
                data = len(connection.recv(1024))
                if not data:
                    break
                totalData += data

            print(totalData)
            connection.close()
        except socket.timeout:
            sys.stderr.write("ERROR")
        totalConnected += 1
        

if __name__ == '__main__':
    main()
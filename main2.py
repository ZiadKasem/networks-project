import socket

import sys
if len(sys.argv) <= 1:
    print ('Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server')
    #sys.exit(2)
# Create a server socket, bind it to a port and start listening

tcpSerSock = socket(AF_INET,SOCK_STREAM)
#server_address
tcpSerSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
tcpSerSock.bind(('localhost',8888))
tcpSerSock.listen(5)
# Fill in start.
# Fill in end.
while 1:
    # Start receiving data from the client
    print ('\n\nReady to serve...')
    tcpCliSock, addr = tcpSerSock.accept() #return address and tcp client socket
    print ('Received a connection from:', addr)
    message = tcpCliSock.recv(4096)
    print (message)
    # Extract the filename from the given message
    print(message.split()[1])
    #filename = message.split()[1].partition("/")[2]

    file = message.decode().split()[1]
    print(file)
    filename = file.split('/')[1]
    print (filename)
    fileExist = "false"
    filetouse = "/" + filename
    print(filetouse)
#/////////////////////////////////////
    flag = -1
    urlfile = open("URL_BLOCKED.txt")
    for i in urlfile:
        if message == i:
            flag = 0
            break
    urlfile.close()
    print( flag )
    Blockedfile = open("Blocked.txt")
    if flag == 0:
        tcpCliSock.send("HTTP/1.0 403 Forbidden\r\n".encode())  # mod
        tcpCliSock.send("Content-Type:text/html\r\n".encode())  # mod
        tcpCliSock.send(Blockedfile.read().encode())
        continue

    Blockedfile.close()
#/////////////////////////////
    try:
        # Check wether the file exist in the cache
        f = open(filetouse[1:], "rb")#mod
        outputdata = f.read() #was readlines-> in order to be not tuple
        fileExist = "true"
        # ProxyServer finds a cache hit and generates a response message
        tcpCliSock.send("HTTP/1.0 200 OK\r\n".encode())  #mod
        tcpCliSock.send("Content-Type:text/html\r\n".encode())  # mod
        tcpCliSock.send(outputdata)
        f.close()
        print ('Read from cache')
        #return outputdata
        # Error handling for file not found in cache
    except IOError:
        if fileExist == "false":
            # Create a socket on the proxyserver
             c = socket(AF_INET, SOCK_STREAM)
             hostn = filename.replace("www.","",1)
             print(hostn)
             try:
                fileobj = c.makefile('rwb',0)
                # Connect to the socket to port 80
                port=80
                socket.gethostbyname(hostn) #expect error if not found
                c.connect((hostn, 80))

                fileobj.write(b'GET / HTTP/1.0\r\n\r\n') #sent to browser server
                print("checkpoint1")
                # check if it needs to be encoded
                responseBuffer = fileobj.read()

                #responseBuffer = c.recv(2048)
                print ("responseBuffer print")
                print(responseBuffer)
                print(8888)
                # Create a new file in the cache for the requested file.
                # Also send the response in the buffer to client socket and the corresponding file in the cache
                tmpFile = open("./" + filename,"wb")
                for i in range(0, len(responseBuffer)):
                    tmpFile.write(responseBuffer[i])
                print(222222)
                tcpCliSock.send(responseBuffer)
                tmpFile.close()
                # Fill in start.
                # Fill in end.
             except Exception as e:
                 print ("Illegal request")
                 print (e)
        else:
             print("error 404")
             ERRORFile = open("Error.txt")
             tcpCliSock.send("HTTP/1.0 404 page not found\r\n".encode())  # mod
             tcpCliSock.send("Content-Type:text/html\r\n".encode())  # mod
             tcpCliSock.send(ERRORFile.read().encode())


        tcpCliSock.close()
 # Fill in start.
tcpSerSock.flush()
tcpSerSock.close()
 # Fill in end.
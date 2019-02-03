import bluetooth


serverSock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
print('here')

def connect(port):
    return bluetooth.BluetoothSocket(bluetooth.RFCOMM)

def listen_for_messages():
    socket_server = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    port=port
    socket_server.bind(("", port))
    socket_server.listen(port)
    
    client_sock,address = socket_server.accept()
    
    data = client_sock.recv(1024)
    client_sock.close()
    socket_server.close()
        
def send_message(address, msg):
    port=1
    sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((address, port))
    sock.send(msg)
    sock.close()

def get_devices():
    devices = bluetooth.discover_devices()
    for addr in devices:
        name = str(bluetooth.lookup_name(addr))
        print(name + " [" + str(addr) + "]")

port = 1
serverSock.bind(("", port))
serverSock.listen(1)

while True:
    f = open("/home/pi/messages.txt", 'r+')          
    try:
        get_devices()
        clientSock,address = serverSock.accept()
        print("Accepted connection from ", address)
        serverSock.getpeername()
        
        str = f.readline()
        print("read line")
        if(str.startswith('TCCC1')):
            print("passed if")
            serverSock.connect(("94:65:2D:DB:FB:11", port))
            print("connected")
            serverSock.send(str)
            print("sent")
            serverSock.close()
            print("closed")
            break
    except IOError as e:
        print(e)
        pass
    try:
        data = clientSock.recv(1024)
        if len(data) == 0: break
        print("received [%s]" % data)
        str = "".join(map(chr, data))
        f.write(str+"\n")
        


    except IOError:
        pass

    except KeyboardInterrupt:

        print("disconnected")
    



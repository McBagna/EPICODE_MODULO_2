import socket

# In questa parte scegliamo la porta e catturiamo l'ip della macchina dove eseguiamo il software
port = 4000
catchIPSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
catchIPSocket.connect(("8.8.8.8", 80))
localIP = str(catchIPSocket.getsockname()[0])
catchIPSocket.close()

# Qui creiamo il ns socket
mySockServer1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mySockServerAdress = (localIP,port)
mySockServer1.bind(mySockServerAdress)

print(f"UDP Server is listening at address {localIP} on port {port}...")

while True:
    data, client_address = mySockServer1.recvfrom(1024)
    print(f"Received message from {client_address}: {data.decode('utf-8')}")
    
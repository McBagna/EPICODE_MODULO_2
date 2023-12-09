import socket
import os

print(
    """
    Se non lo si e' gia' fatto lanciare da terminale il programma W7D4_Pratica_1_Server.py...............
    Li saranno indicati l'indirizzo ip ed il numero di porta sul quale il server e' in ascolto...........
    """
)
ip = input("Inserisci l'ip del server che e' stato indicato \n")
porta = int(input("Inserisci la porta indicata per una comunicazione efficace \n"))
packs = int(input("Inserisci il numero di pacchetti che vuoi mandare \n"))

# Create a UDP socket
mySockClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address and port
server_address = (ip, porta)

# Send a message to the server
for i in range(packs):
    message = str(os.urandom(1024))
    mySockClient.sendto(message.encode('utf-8'), server_address)
    

# Close the socket
mySockClient.close()


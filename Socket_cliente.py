import socket
SERVER = "Direccion Server"
PORT = 8080
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER,PORT))
client.sendall(bytes("Yo soy el cliente",'UTF-8'))
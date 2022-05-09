import socket
import threading

class HiloCliente(threading.Thread):
    def _init_(self,ipCliente,clienteSocket):
       threading.Thread._init_(self)
       self.csocket = clienteSocket
       print("Nueva conexion",ipCliente)
    def run(self):
        print ("Conexion desde: ",ipCliente) 
        #self.socket.send (bytes ("hola esto se envia desde el server", 'utf-8'))
        msg=''
        while True:
            #data = self.csocket.recv(2048)
            if msg == 'bye':
                break
            print ("del cliente",msg)
            #self.socket.send(bytes(msg,'UTF-8'))
        print ("El cliente",ipCliente,"desconectado")
host = 'localhost'
PORT = 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
server.bind ((host,PORT))
print ("Server Iniciado")
print ("Esperando Cliente")
server.listen(1)
while True: 
    clienteSock,ipCliente = server.accept()
    newthread = HiloCliente(target = ipCliente)
    newthread.start()
    
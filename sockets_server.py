import socket
import threading

class HiloCliente(threading.Thread):
    def _init_(self,ipCliente,clienteSocket):
       threading.Thread._init_(self)
       self.csocket = clienteSocket
       print("Nueva conexion",ipCliente)
    def run(self):
        print ("Conexion desde: ",ipCliente) 
        self.socket.send (bytes ("hola esto se envia desde el server", 'utf-8'))
        msg=''
        while True:
            data = self.csocket.recv(2048)
            if msg = 'bye':
                break
            print ("del cliente",msg)
            
import socket
import threading

class HiloCliente(threading.Thread):
    def _init_(self,ipCliente,clienteSocket):
       threading.Thread._init_(self)
       self.csocket = clienteSocket
       print("Nueva conexion",ipCliente)
    def run(self):
        print ("Conexion desde: ",ipCliente) 
        
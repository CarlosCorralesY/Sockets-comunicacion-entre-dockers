import socket
import threading

class HiloCliente(threading.Thread):
    def _init_(self,ipCliente,clienteSocket):
        
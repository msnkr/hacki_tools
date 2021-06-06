import socket
from IPy import IP
from termcolor import colored

class PortScan():
    def __init__(self, h, port_num):
        self.h = h
        self.port_num = port_num
        self.banner = banner

    def port_scan(self):
        for port in range(1, int(port_num)):
            try:
                s = socket.socket()
                s.connect((h, port))
                s.settimeout(1)
                banner = s.recv(1024).decode().strip('\n')
            except:
                pass


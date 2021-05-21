import socket
from IPy import IP
from termcolor import colored

host = input(colored('Hosts: ', 'red'))

def port_scan(host, port):
    try:
        s = socket.socket()
        s.settimeout(0.5)
        s.connect((host, port))
        print(colored(f'[+] Port {port} is open.', 'blue'))
        
    except:
        pass


for port in range(1, 100):
    port_scan(host, port)


import socket
from IPy import IP
from termcolor import colored

host = input(colored('Hosts: ', 'red'))
host_list = host.split(', ')

def port_scan(h):
    for port in range(1, 100):
        try:
            s = socket.socket()
            s.settimeout(0.5)
            s.connect((h, port))
            print(colored(f'[+] Port {port} is open.', 'blue'))        
        except:
            pass

for h in host_list:
    print(colored(f'[-_-] Scanning {h}: ', 'red'))
    port_scan(h)



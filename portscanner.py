import socket
from IPy import IP
from termcolor import colored

host = input(colored('Hosts: ', 'red'))
host_list = host.split(', ')
port_num = input(colored('Number of ports: ', 'red'))


def port_scan(h):
    for port in range(1, int(port_num)):
        try:
            s = socket.socket()
            s.settimeout(1)
            s.connect((h, port))
            try:
                banner = s.recv(1024).decode().strip('\n')
                print(colored(f'[0_0] {h}: {port}: {banner}', 'blue'))        
            except:
                print(colored(f'[0_0] {h}: {port}', 'blue'))        
        except:
            pass

for h in host_list:
    print(colored(f'[-_0] Scanning {h}: ', 'red'))
    port_scan(h)



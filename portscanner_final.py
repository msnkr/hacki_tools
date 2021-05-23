import socket
from IPy import IP
from termcolor import colored


def port_scan(h, port_num):
    for port in range(1, int(port_num)):
        try:
            s = socket.socket()
            s.connect((h, port))
            s.settimeout(1)
            banner = s.recv(1024).decode().strip('\n')
            print(colored(f'[0_0] {h}: {port}: {banner}', 'blue'))        
        except:
            pass


host = input(colored('Host/s: ', 'red'))
port_num = input(colored('Port/s: ', 'red'))
host_list = host.split(', ')
for h in host_list:
    print(colored(f'[-_0] Scanning {h}: ', 'red'))
    port_scan(h, port_num)

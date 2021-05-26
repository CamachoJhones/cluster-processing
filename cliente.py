import socket
import threading
import os
import sys
class Cliente:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.accept_connections()  
    def accept_connections(self):
        ip = "LocalHost"
        #port = 8000

        port = int(sys.argv[1])
        self.s.bind((ip,port))
        self.s.listen(100)
        print('Running on IP: '+ip)
        print('Running on port: '+str(port))
        while 1:
            c, addr = self.s.accept()
            print(c)           
            threading.Thread(target=self.handle_client,args=(c,addr,)).start()
    def handle_client(self,c,addr):
        data = c.recv(1024).decode()  
        print("IMRPIMIENDO DATA ------  " + data) 
        if not os.path.exists(data):
            c.send("file-doesn't-exist".encode())
        else:
            c.send("file-exists".encode())
            print('Sending',data)
            if data != '':
                file = open(data,'rb')
                data = file.read(1024)
                while data:
                    c.send(data)
                    data = file.read(1024)
                c.shutdown(socket.SHUT_RDWR)
                c.close()
cliente =Cliente()

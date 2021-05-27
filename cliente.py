import socket
import threading
import os
import sys
import time
class Cliente:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.accept_connections()  
    def accept_connections(self):
        ip = "LocalHost"
        #port = 8000

        port = int(sys.argv[1])
        print("Antes del BIND <<<<<<<<<<<<<<---------------  ")
        time.sleep(3)
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
        print("Cosas que trai el data " + data) 
        caracter,arch = data.split('-')
        print("Caracter>> " + caracter )
        print("Caracter>> " + arch )
        if(caracter == "/x11"):
            print("Es un video")
        elif(caracter == "/x12"):
            print("Es un frame")
            os.chdir(r"C:\Users\Alonso\OneDrive\Desktop\ProyectoFinalASD\Emily\Simple-Python-File-Transfer-Server-master\serverFrames")
            # change dir a /serverFrames
            
        else:
            print("Ni es video ni es frame")

        if not os.path.exists(arch):
            c.send("file-doesn't-exist".encode())
        else:
            c.send("file-exists".encode())
            print('Sending ',arch)
            if arch != '':
                file = open(arch,'rb')
                arch = file.read(1024)
                while arch:
                    c.send(arch)
                    arch = file.read(1024)
                c.shutdown(socket.SHUT_RDWR)
                c.close()
cliente =Cliente()

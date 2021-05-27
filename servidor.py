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
        print("Antes del BIND <<<<<<<<<<<<<<---------------  ")
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
        file_name=arch
        print("Caracter>> " + caracter )
        print("Caracter>> " + arch )
        if(caracter == "/x11"):
            print("Es un video")
            banderaFrame=False

        elif(caracter == "/x12"):
            print("Es el frame")
            os.chdir(r"C:\Users\Alonso\OneDrive\Desktop\ProyectoFinalASD\Emily\Simple-Python-File-Transfer-Server-master\serverFrames")
            # change dir a /serverFrames
            banderaFrame=True

        elif(caracter=="/x13"):
            print("Es el frame que viene desde Cluster ")
            os.chdir(r"C:\Users\Alonso\OneDrive\Desktop\ProyectoFinalASD\Emily\Simple-Python-File-Transfer-Server-master\clusterFilteredFrames")
            # change dir a /serverFrames
            banderaFrame=True
        else:
            print("Ni es video ni es frame ni sabemos de donde viene")
            banderaFrame=False

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
                file.close()

                

cliente =Cliente()

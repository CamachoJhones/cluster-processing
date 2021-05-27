

import socket
import os
import argparse
import sys
import threading
target_port = sys.argv[2]


def filtro(file_name, cluster_number):
    print("FILE NAME FILTRO " + file_name)
    os.chdir(r"C:\Users\Alonso\OneDrive\Desktop\ProyectoFinalASD\Emily\Simple-Python-File-Transfer-Server-master")
    print("python clusterFilter.py " + file_name + " " + cluster_number)
    os.system("python clusterFilter.py " + file_name + " " + cluster_number)


class Servidor:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.connect_to_server()
    def connect_to_server(self):
        self.target_ip = "LocalHost"
        #self.target_port = 8000
        self.s.connect((self.target_ip,int(target_port)))
        self.main()
    def reconnect(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.s.connect((self.target_ip,int(target_port)))
    def main(self):
        file_name = sys.argv[1]
        while 1:
            print("FAIL NEIM */*/*/*/ " + file_name)
            if target_port=="8000":
                #val=os.getcwd()
                #print("RUTA DIRECTORIO 1 -*/-*/-*/-*/-*/   " + val)
                write_name = 'from_server_'+file_name
                file_name = "/x11-" + file_name 
                print("Nombre File_name_" + file_name)

            elif(target_port=="8001"):
                write_name="./serverFrames/"+ file_name
                #os.chdir(r"C:\Users\Alonso\OneDrive\Desktop\ProyectoFinalASD\Emily\Simple-Python-File-Transfer-Server-master\serverFrames")
                #val=os.getcwd()
                #print ("Ruta actual " + val)
                print("RUTA DIRECTORIO 2 -*/-*/-*/-*/-*/   " + file_name)
                write_name = './clusterFrames/from_server_'+file_name
                file_name = "/x12-" + file_name 
                print("Nombre despues de File NAME 8001 " + file_name)

            elif(target_port=="8002"):
                write_name="./clusterFilteredFrames/"+ file_name
                #os.chdir(r"C:\Users\Alonso\OneDrive\Desktop\ProyectoFinalASD\Emily\Simple-Python-File-Transfer-Server-master\serverFrames")
                #val=os.getcwd()
                #print ("Ruta actual " + val)
                print("RUTA DIRECTORIO 3 -*/-*/-*/-*/-*/   " + file_name)
                write_name = './serverFilteredFrames/'+file_name #AQUI CAMBIO nombre FRAMES!!!!!!!!!!!!!
                file_name = "/x13-" + file_name 
                print("Nombre despues de File NAME 8002 " + file_name)
            self.s.send(file_name.encode())
            confirmation = self.s.recv(1024)
            if confirmation.decode() == "file-doesn't-exist":
                print("File doesn't exist on server.")
                self.s.shutdown(socket.SHUT_RDWR)
                self.s.close()
                self.reconnect()
            else:        
                if os.path.exists(write_name): os.remove(write_name)

                with open(write_name,'wb') as file:
                    while 1:
                        data = self.s.recv(1024)
                        if not data:
                            break
                        file.write(data)
                print(file_name,'successfully downloaded.')
                if(write_name.find("png")!= -1):
                    img_name = write_name[16:]
                    print("Imagen a FILTRAR "+img_name)
                    #subprocess.call('start /wait python cliente.py 8001', shell=True)
                    #print("python clusterFilter.py " + file_name)
                    
                    t=threading.Thread(target=filtro(img_name, "2"))
                    t.start()
                else:
                    pass

                self.s.shutdown(socket.SHUT_RDWR)
                self.s.close()
                #self.reconnect()  
                break

        exit()               
servidor = Servidor()


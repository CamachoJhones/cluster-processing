import subprocess
import sys
import os
import threading
import time

#subprocess.call(['./servidor.py', 'enviar.txt'])
#subprocess.call(['./cliente.py'])

def sendFrame(filename, puerto):
    print(filename + "**************************************")
    ruta= "python servidor.py " + str(filename) +" "+ puerto
    print("RUTA +++++++++++++++ "+ ruta)
    os.system(ruta)
def processFrames(carpetaProcess):
    t=threading.Thread(target=rutina)
    t.start()
    time.sleep(3)
    if(carpetaProcess=='./serverFrames'):
        puerto="8001"
    elif(carpetaProcess=='./clusterFilteredFrames'):
        puerto="8002"
        print("-*/-*/-*/-*/-*/-*/-*/-/*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/")
        print("-*/-*/-*/-*/-*/-*/-*/-/*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/")
        print("-*/-*/-*/-*/-*/-*/-*/-/*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/")

        

    for filename in os.listdir(carpetaProcess):
        sendFrame(filename, puerto)

def rutina():
    print("Entramos a RUTINA")
    #os.system("python cliente.py 8001")
    print("Iniciando CLUSTER 1 ")
    subprocess.call('start /wait python cliente.py 8001', shell=True) #Frames ida
    subprocess.call('start /wait python cliente.py 8002', shell=True) #Frames regreso


os.system("python servidor.py video.mp4 8000")
#subprocess.call('start /wait python servidor.py video.mp4 8000', shell=True)
os.system("python video2frames.py")
#subprocess.call('start /wait python servidor.py video2frames.py', shell=True)
processFrames('./serverFrames')
processFrames('./clusterFilteredFrames')
os.system("python frames2video.py")



#print(os.listdir('./serverFrames'))
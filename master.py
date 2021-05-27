import subprocess
import sys
import os
import threading
import time

#subprocess.call(['./servidor.py', 'enviar.txt'])
#subprocess.call(['./cliente.py'])

def sendFrame(filename):
    print(filename + "**************************************")
    ruta= "python servidor.py " + str(filename) +" 8001"
    print("RUTA +++++++++++++++ "+ ruta)
    os.system(ruta)
def processFrames():
    t=threading.Thread(target=rutina)
    t.start()
    for filename in os.listdir('./serverFrames'):
        sendFrame(filename)

def rutina():
    print("Entramos a RUTINA")
    #os.system("python cliente.py 8001")
    print("Iniciando CLUSTER 1 ")
    subprocess.call('start /wait python cliente.py 8001', shell=True)

os.system("python servidor.py video.mp4 8000")
#subprocess.call('start /wait python servidor.py video.mp4 8000', shell=True)
os.system("python video2frames.py")
#subprocess.call('start /wait python servidor.py video2frames.py', shell=True)
processFrames()
#print(os.listdir('./serverFrames'))
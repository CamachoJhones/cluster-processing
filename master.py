import subprocess
import sys
import os
import threading

#subprocess.call(['./servidor.py', 'enviar.txt'])
#subprocess.call(['./cliente.py'])

def sendFrame(filename):
    print(filename + "**************************************")
    ruta= "python servidor.py " + str(filename) +" 8001"
    print("RUTA +++++++++++++++ "+ ruta)
    os.system(ruta)
def processFrames():
    for filename in os.listdir('./serverFrames'):
        t=threading.Thread(target=rutina)
        t.start()
        sendFrame(filename)

def rutina():
    os.system("python cliente.py 8001")

os.system("python servidor.py video.mp4 8000")
os.system("python video2frames.py")
processFrames()
#print(os.listdir('./serverFrames'))

     



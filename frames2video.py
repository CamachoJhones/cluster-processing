import cv2
import numpy as np
import os

from os.path import isfile, join


def frames_to_video(pathIn,pathOut,fps):
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
    #Acomodar Frames
    files.sort(key = lambda x: int(x[5:-4]))
    for i in range(len(files)):
        filename=pathIn + files[i]
        #Leer Frames
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        print(filename)
        #Crear arreglo con las imagenes
        frame_array.append(img)
    #Guardar Video
    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
    for i in range(len(frame_array)):
        #Guardar matriz de frames
        out.write(frame_array[i])
    out.release()

def main():
    pathIn= './serverFilteredFrames/'
    pathOut = './clientFilteredVideo/videoFINAL.mp4'
    fps = 25.0
    frames_to_video(pathIn, pathOut, fps)

if __name__=="__main__":
    main()

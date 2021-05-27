import sys
import cv2 as cv
import os

cluster_number = sys.argv[2]
#frame_name = "frame22.png"
#frame_name = "from_server_frame22.png"
os.chdir(r"C:\Users\Alonso\OneDrive\Desktop\ProyectoFinalASD\Emily\Simple-Python-File-Transfer-Server-master\clusterFrames")
frame_name = sys.argv[1]
frame_number = str(frame_name[17:].replace('.png',''))
img = cv.imread(frame_name,cv.IMREAD_GRAYSCALE)
#cambio de directorio
renderFrame = "frame"+frame_number+"-"+"ok-"+cluster_number+".png"
os.chdir(r"C:\Users\Alonso\OneDrive\Desktop\ProyectoFinalASD\Emily\Simple-Python-File-Transfer-Server-master\clusterFilteredFrames")
cv.imwrite(renderFrame,img)
print(frame_name+" FILTERED")



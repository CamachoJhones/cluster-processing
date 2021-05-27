import sys
import cv2 as cv
cluster_number = str(1)
#frame_name = "frame22.png"
frame_name = "from_server_frame22.png"
frame_name = sys.argv[1]
frame_number = str(frame_name[17:].replace('.png',''))
img = cv.imread(frame_name,cv.IMREAD_GRAYSCALE)
#cambio de directorio
renderFrame = "frame"+frame_number+"-"+"ok-"+cluster_number+".png"
cv.imwrite(renderFrame,img)
print(renderFrame+" ready")



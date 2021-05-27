import cv2
import os

#video_path= open('from_server video.mp4')

cap = cv2.VideoCapture('from_server_video.mp4')
img_index = 0
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    os.chdir(r"C:\Users\Alonso\OneDrive\Desktop\ProyectoFinalASD\Emily\Simple-Python-File-Transfer-Server-master\serverFrames")
    cv2.imwrite('frame' + str(img_index) + '.png', frame)
    print('frame' + str(img_index) + '.png')
    img_index += 1

cap.release()
cv2.destroyAllWindows()
exit()

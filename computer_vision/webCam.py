import cv2
import numpy as np
import os
def load_video(camera_index):
    # if not os.path.exists(camera_index):       ---- optional code ----
    #     print(f"Camera does not exist \n {camera_index}")
    #     return None      
    video = cv2.VideoCapture(camera_index)
    while True:
        status,frame = video.read()
        if not status:
            print('no frame availble!')
            break
        cv2.imshow("camera",frame)
        if cv2.waitKey(10) == ord('q'):
            break
    #clear the memory
    video.release()
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    cam_indx = 0
    load_video(cam_indx)
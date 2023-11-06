import cv2
import numpy as np
import os
def load_video(path_of_video):
    if not os.path.exists(path_of_video):
        print(f"Video does not exist \n {path_of_video}")
        return None
    cv2.namedWindow('Video')
    cv2.createTrackbar('Ksize','Video',3,100,lambda x:None)
    video = cv2.VideoCapture(path_of_video)
    while True:
        status,frame = video.read()
        height, width , _= frame.shape
        print(f'{height} and {width}')
        if not status:
            print('no frame availble!')
            break
        ''' 
        operations
        1.resize
        2.convert to grayscale
        3.blur
        4.add text
        5.add graphics
        
        '''
        Frame = cv2.resize(frame,(None,None),fx=0.5,fy=0.5)
        Frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
       
        
        Ksize = cv2.getTrackbarPos('Ksize','Video')
        # sigmaY = cv2.getTrackbarPos('Y','Video')
        try: Frame = cv2.GaussianBlur(Frame,(Ksize,Ksize),0)
        except:print(Ksize)
        
        cv2.putText(frame,'Atoms',(width//2-50,height//2),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
        cv2.imshow("Video",frame)
        if cv2.waitKey(10) == ord('q'):
            break
    #clear the memory
    video.release()
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    videofile = r'C:\Users\ASHU\Downloads\atoms.mp4'
    load_video(videofile)
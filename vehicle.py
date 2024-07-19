import cv2
import numpy as np 

#Web Camera
cap=cv2.VideoCapture('video.mp4')

min_width_rectangle=80  #min width rectangle
min_height_rectangle=80  #min height rectangle

count_line_position=550
#Initialise Substractor 
algo= cv2.createBackgroundSubtractorMOG2()

def center_handle(x,y,w,h):
     x1=int(w/2)
     y1=int(h/2)
     cx=x+x1
     cy=y+y1
     return cx,cy
detect =[]
offset=10 #Allowable error between pixel
cnt=0

 
while True:
     ret,frame1=cap.read()

     grey=cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
     blur = cv2.GaussianBlur(grey,(3,3),5)
     #applying on each frame
     imageSub=algo.apply(blur)
     dilate =cv2.dilate(imageSub,np.ones((5,5)))
     kernel =cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
     dilatada=cv2.morphologyEx(dilate,cv2.MORPH_CLOSE,kernel)
     dilatada=cv2.morphologyEx(dilatada,cv2.MORPH_CLOSE,kernel)
     counter,h =cv2.findContours(dilatada,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

     cv2.line(frame1,(25,count_line_position),(1200,count_line_position),(255,127,0),3)

     for(i,c) in enumerate (counter):
          (x,y,w,h) =cv2.boundingRect(c)
          validate_counter=(w>=min_width_rectangle) and (h>=min_height_rectangle)
          if not validate_counter:
               continue
          cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
          cv2.putText(frame1,"VEHICLE COUNTER:"+str(cnt),(x, y-20),cv2.FONT_HERSHEY_TRIPLEX,1,(255,244,0),2)

          center= center_handle(x,y,w,h)
          detect.append(center)
          cv2.circle(frame1,center,4,(0,0,255),-1)

          for (x,y) in detect:
               if y<(count_line_position+offset) and y>(count_line_position-offset):
                  cnt+=1
                  cv2.line(frame1,(25,count_line_position),(1200,count_line_position),(0,170,255),3)   
                  detect.remove((x,y))
                  print("Vehicle Counter:"+str(cnt))

            
     cv2.putText(frame1,"VEHICLE COUNTER:"+str(cnt),(450,70),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),5)

     
     
     
     
     
     
     #cv2.imshow('Detectoe',dilatada) #to check what happens in the background



     cv2.imshow('Video Original',frame1)

     if(cv2.waitKey(1) ==13):
         break
cv2.destroyAllWindows()
cap.release()     
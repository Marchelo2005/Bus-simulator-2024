import cv2 
import pygame
import random
class detector(object):
    txtVideo=""
    def face():
     pygame.display.set_caption("Video Display")
     prototxt ="model/deploy.prototxt"
     model ="model/res10_300x300_ssd_iter_140000.caffemodel"
     net=cv2.dnn.readNetFromCaffe(prototxt,model)
     if detector.txtVideo=="exit":
      randomVideo=random.randint(1,2)
     elif detector.txtVideo=="person":
      randomVideo=random.randint(1,24)
     cap=cv2.VideoCapture("video/"+detector.txtVideo+repr(randomVideo)+".mp4")
     GREEN = (0, 255, 0)
     YELLOW = (0, 255, 255)
     screenVideo = pygame.display.set_mode((400, 800))
     while True:
       ret, frame= cap.read()
       if ret==False:
         break
       height, width, _ =frame.shape
       frame_resized =cv2.resize(frame, (300, 300))
       blob = cv2.dnn.blobFromImage(frame_resized, 1.0, (300,300),(104, 117, 123))
       net.setInput(blob)
       detections= net.forward()
       #print("detections.shape: ", detections.shape)
       for detection in detections[0][0]:
      #print("detection: ", detection)
        if detection[2]>0.5:
         box=detection[3:7]*[width, height, width, height]
         x_start, y_start, x_end, y_end=int(box[0]),int(box[1]),int(box[2]),int(box[3])
         cv2.rectangle(frame, (x_start, y_start), (x_end, y_end), (0,255,0),2)
         cv2.putText(frame, "Conf: {:2f}".format(detection[2] * 100),(x_start, y_start -5),1,1.2,(0,255,255),2 )
       frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
       frame = cv2.transpose(frame)
       frame_surface = pygame.surfarray.make_surface(frame)
    
       # Display frame in Pygame
       screenVideo.fill((0, 0, 0))  # Clear the screen
       screenVideo.blit(frame_surface, (0, 0))  # Adjust position as needed
       pygame.display.flip()  # Update the full display Surface to the screen
       if cv2.waitKey(1) & 0xFF==27:
        break
       
       cap.read()   
       cv2.destroyAllWindows()

    pass





import cv2
import pygame
import numpy as np

class Utils:
    """User friendly platform + other esential functions"""
    x,y=0,0
    rotation=0
    speed=0
    font = cv2.FONT_HERSHEY_SIMPLEX
    keys=["Q","H","R","W","A","S","D"]
    description=["Quit","Hide/Show HelpBar","Reccord","Move Forward","Move Left","Move Backward","Move Right"]
    def scale_image(img, factor):
        size = round(img.get_width() * factor), round(img.get_height() * factor)
        return pygame.transform.scale(img, size)


    def blit_rotate_center(win, image, top_left, angle):
        """rotate images relative to a point """
        rotated_image = pygame.transform.rotate(image, angle)
        #new_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
        win.blit(rotated_image, top_left)


    def blit_text_center(win, font, text):
        """ add text to pygame image object"""
        render = font.render(text, 1, (200, 200, 200))
        win.blit(render, (win.get_width()/2 - render.get_width() /
                      2, win.get_height()/2 - render.get_height()/2))
    def Display(frame):
        """opencv lookalike Display function with user friendly helpBar"""
        h,w,c=frame.shape
        image = np.ones((h, w//2, c), dtype=np.uint8)*255
        if HelpBar.show==1:
            cv2.putText(image, "HelpBar", (10, 20), Utils.font, 1, (9,0,0), 2)
            for i in range(len(Utils.keys)):
                cv2.rectangle(image,(10,30+i*40),(40,60+i*40),(255,0,0),3)
                cv2.putText(image,Utils.keys[i],(20,50+i*40),Utils.font,0.5,(0,0,255),2)
                cv2.putText(image,Utils.description[i],(50,50+i*40),Utils.font,0.5,(0,0,255),2)
            cv2.putText(image,"Car PROPERTIES",(10,380),Utils.font,1,(0,0,0),2)
            cv2.rectangle(image,(10,400),(310,700),(255,0,255),2)
            cv2.putText(image,"Position",(30,430),Utils.font,0.5,(255,0,0),2)
            cv2.putText(image,"X = "+str(Utils.x),(30,450),Utils.font,0.5,(0,0,0),2)
            cv2.putText(image,"Y = "+str(Utils.y),(130,450),Utils.font,0.5,(0,0,0),2)
            cv2.putText(image,"Angular Movement",(30,470),Utils.font,0.5,(255,0,0),2)
            cv2.putText(image,"angle = "+str(Utils.rotation),(30,490),Utils.font,0.5,(0,0,0),2)
            cv2.putText(image,"Linear Movement",(30,510),Utils.font,0.5,(255,0,0),2)
            
            cv2.putText(image,"speed = "+str(round(Utils.speed,2)),(30,530),Utils.font,0.5,(0,0,0),2)

            frame=cv2.hconcat([frame,image])
            
        
        cv2.imshow("FramexMap",frame)
class HelpBar():
    #image = np.ones((720, 100, 3), dtype=np.uint8)*255

    show=0
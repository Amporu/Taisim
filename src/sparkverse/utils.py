"""
info:This module contains a collection of non categorizable functions
autor: Tucudean Adrian-Ionut
date: 17.05.2023
email: Tucudean.Adrian.Ionut@outlook.com
license: MIT
"""

import time
import cv2
import pygame
import numpy as np
class Video:
    """class for reccording data"""
    start_time = 0
    end_time=0
    delta_time=0
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') #pylint: disable=E1101
    output_file = 'output_video.mp4'  # Specify the output file name
    fps = 30.0  # Specify the frames per second (FPS)
    #frame_size = (640, 480)  # Specify the frame size (width, height)
    video_writer = None#cv2.VideoWriter(output_file, fourcc, fps, frame_size)
    recorded=0
    reccording_flag=0
class Utils(Video):
    """a class where i dump yet non categorizable functions

    Parameters:
    rotation (int): car rotation
    speed (float): car speed
    x (int): car x position
    y (int): car y position
    description (string[]): HelpBar description
    keys (string[]): HelpBar keys
    """
    x,y=0,0
    rotation=0
    speed=0
    font = cv2.FONT_HERSHEY_SIMPLEX   #pylint: disable=E1101
    keys=["Q","H","R","W","A","S","D","T"]
    description=["Quit","Hide/Show",  #pylint: disable=C0301
                 "Reccord",
                 "Move Forward",
                 "Rotate Left",
                 "Move Backward",
                 "Rotate Right",
                 "Enable Trail"]
    @staticmethod
    def scale_image(img, factor):
        """
        function designated for scaling an image by a factor

        Parameters:
        img (Mat)    : source image 
        factor (int) : scale factor (where 1 is the original size)

        Returns: 
        Mat         : rescaled image
        """
        size = round(img.get_width() * factor), round(img.get_height() * factor)
        return pygame.transform.scale(img, size)

    @staticmethod
    def blit_rotate_center(win, image, point, angle):
        """
        rotate images relative to a point

        Parameters:
        win (pygameObj)    : pygame window object
        image (Mat)        : desired image
        point (tuple)      : point of rotation
        angle (int)        : the angle of rotation
        """
        rotated_image = pygame.transform.rotate(image, angle)
        win.blit(rotated_image, point)

    @staticmethod
    def blit_text_center(win, font, text):
        """
        add text to pygame image object

        Parameters: 
        win (pygameObj)    :  pygame window object
        font (int)         :  desired font 
        text (string)      :  text message
        
        """
        render = font.render(text, 1, (200, 200, 200))
        win.blit(render, (win.get_width()/2 - render.get_width() /
                      2, win.get_height()/2 - render.get_height()/2))
    @staticmethod
    def display(frame):
        """
        HelpBar display

        Parameters:
        frame (Mat): input frame
        """
        if Utils.recorded==1:
            Utils.start_time=time.time()
            Utils.video_writer = cv2.VideoWriter(Utils.output_file,Utils.fourcc, Utils.fps,(frame.shape[1],frame.shape[0]))
            Utils.recorded=-1
        if Utils.recorded==-1:
            Utils.video_writer.write(frame)
            Utils.end_time=time.time()
            Utils.delta_time=Utils.end_time-Utils.start_time
        height,width,channels=frame.shape
        help_image = np.ones((height, width//2, channels), dtype=np.uint8)*255
        sensor_image = np.ones((height, width//2, channels), dtype=np.uint8)*255
        if HelpBar.show==1 and SensorBar.show==0:
            frame=HelpBar.showpannel(frame,help_image)
        if HelpBar.show==1 and SensorBar.show==1:
            frame=HelpBar.showpannel(frame,help_image)
            frame=SensorBar.showpannel(frame,sensor_image)
        if HelpBar.show==0 and SensorBar.show==1:
            frame=SensorBar.showpannel(frame,sensor_image)
        cv2.imshow("FramexMap",frame)#pylint: disable=E1101
    @staticmethod
    def move_player(player_car):
        """key input for player car"""
        keys = pygame.key.get_pressed()
        moved = False
        if keys[pygame.K_q]:#pylint: disable=E1101
            HelpBar.last_key=0
            pygame.quit()#pylint: disable=E1101
        if keys[pygame.K_r]:#pylint: disable=E1101
            HelpBar.last_key=2
            time.sleep(0.5)
            Utils.reccording_flag=Utils.reccording_flag^1
        if keys[pygame.K_t]:#pylint: disable=E1101
            HelpBar.last_key=7
            HelpBar.trail_flag=HelpBar.trail_flag^1
            time.sleep(0.5)
        if keys[pygame.K_h]:#pylint: disable=E1101
            HelpBar.last_key=1
            HelpBar.show=HelpBar.show^1
            time.sleep(0.5)
        if keys[pygame.K_e]:#pylint: disable=E1101
            SensorBar.show=SensorBar.show^1
            time.sleep(0.5)
            #print(HelpBar.show)
        if keys[pygame.K_a]:#pylint: disable=E1101
            HelpBar.last_key=4
            player_car.rotate(left=True)
        if keys[pygame.K_d]:#pylint: disable=E1101
            HelpBar.last_key=6
            player_car.rotate(right=True)
        if keys[pygame.K_w]:#pylint: disable=E1101
            HelpBar.last_key=3
            moved = True
            player_car.move_forward()
        if keys[pygame.K_s]:#pylint: disable=E1101
            HelpBar.last_key=5
            moved = True
            player_car.move_backward()
        if Utils.reccording_flag==1 and Utils.recorded!=-1:
            Utils.recorded=1
        if Utils.reccording_flag==0 and Utils.recorded==-1:
            time.sleep(0.5)
            Utils.video_writer.release()
            Utils.recorded=0
            Utils.end_time=time.time()
            

            #video_writer = cv2.VideoWriter(output_file, fourcc, fps, frame_size)
        if not moved:
            player_car.reduce_speed()
class HelpBar:
    """class for controlling HelpBar menu"""
    show = 1
    last_key=-1
    trail_flag=0
    Trail=[]
    @staticmethod
    def enable_trail(player_car,mask):
        """function to enable trail feature"""
        if len(HelpBar.Trail)>=100:
            HelpBar.Trail.pop(0)
        else:
            if len(HelpBar.Trail)>0 and (HelpBar.Trail[-1][0]!=int(player_car.x_value)or (HelpBar.Trail[-1][0]<player_car.x_value+1 and HelpBar.Trail[-1][0]>player_car.x_value-1)) and (HelpBar.Trail[-1][1]!=int(player_car.y_value)or (HelpBar.Trail[-1][0]<player_car.y_value+1 and HelpBar.Trail[-1][0]>player_car.y_value-1)):
                HelpBar.Trail.append((int(player_car.x_value),int(player_car.y_value)))
            if len(HelpBar.Trail)==0:
                HelpBar.Trail.append((int(player_car.x_value),int(player_car.y_value)))
        for i in range(0,len(HelpBar.Trail),1):
            cv2.circle(img=mask,center=HelpBar.Trail[i],radius=3,color=(0,255,0),thickness=1) 
    @staticmethod
    def showpannel(frame,image):
        """
        Help Bar GUI

        Parameters:
        frame (Mat): simulator frame
        image (Mat): blank HelpBar frame
        """
        
        cv2.putText(img=image,text="HelpBar",org=(12, 20),fontFace=Utils.font,fontScale=0.8,color=(9,0,0),thickness=2)#pylint: disable=E1101
        for i in range(len(Utils.keys)):# pylint: disable=C0200
            if (HelpBar.last_key==i):
                if (i!=2):
                    cv2.rectangle(img=image,pt1=(10,30+i*40),pt2=(40,60+i*40),color=(0,255,0),thickness=3)#pylint: disable=E1101
                    cv2.putText(img=image,text=Utils.keys[i],org=(20,50+i*40),fontFace=Utils.font,fontScale=0.5,color=(0,255,0),thickness=2)#pylint: disable=E1101
                    cv2.putText(img=image,text=Utils.description[i],org=(50,50+i*40),fontFace=Utils.font,fontScale=0.5,color=(0,255,0),thickness=2)#pylint: disable=E1101
            else:
                if i!=2 or Utils.recorded!=-1 or Utils.recorded==0:
                    cv2.rectangle(img=image,pt1=(10,30+i*40),pt2=(40,60+i*40),color=(255,0,0),thickness=3)#pylint: disable=E1101
                    cv2.putText(img=image,text=Utils.keys[i],org=(20,50+i*40),fontFace=Utils.font,fontScale=0.5,color=(0,0,255),thickness=2)#pylint: disable=E1101
                    cv2.putText(img=image,text=Utils.description[i],org=(50,50+i*40),fontFace=Utils.font,fontScale=0.5,color=(0,0,255),thickness=2)#pylint: disable=E1101
            if HelpBar.trail_flag==1 and i==7:
                cv2.rectangle(img=image,pt1=(40,60+i*40),pt2=(230,30+i*40),color=(0,0,0),thickness=-1)#pylint: disable=E1101
                cv2.putText(img=image,text=Utils.description[i],org=(50,50+i*40),fontFace=Utils.font,fontScale=0.5,color=(0,255,0),thickness=2)#pylint: disable=E1101
            if Utils.recorded==-1:
                    minutes = int(Utils.delta_time // 60)
                    seconds = int(Utils.delta_time % 60)
                    cv2.putText(img=image,text=str(minutes)+"' "+str(seconds)+"''",org=(50,50+80),fontFace=Utils.font,fontScale=0.5,color=(0,0,255),thickness=2)#pylint: disable=E1101
                    cv2.circle(img=image,center=(25,125),radius=10,color=(0,0,255),thickness=-1)#pylint: disable=E1101
                    cv2.rectangle(img=image,pt1=(10,30+80),pt2=(40,60+80),color=(0,0,255),thickness=3)
        cv2.putText(img=image,text="Car PROPERTIES",org=(10,380),fontFace=Utils.font,fontScale=1,color=(0,0,0),thickness=2)#pylint: disable=E1101
        cv2.rectangle(img=image,pt1=(10,400),pt2=(310,700),color=(255,0,255),thickness=2)#pylint: disable=E1101
        cv2.putText(img=image,text="Position",org=(30,430),fontFace=Utils.font,fontScale=0.5,color=(255,0,0),thickness=2)#pylint: disable=E1101
        cv2.putText(img=image,text="X = "+str(Utils.x),org=(30,450),fontFace=Utils.font,fontScale=0.5,color=(0,0,0),thickness=2)#pylint: disable=E1101
        cv2.putText(img=image,text="Y = "+str(Utils.y),org=(130,450),fontFace=Utils.font,fontScale=0.5,color=(0,0,0),thickness=2)#pylint: disable=E1101
        cv2.putText(img=image,text="Angular Movement",org=(30,470),fontFace=Utils.font,fontScale=0.5,color=(255,0,0),thickness=2)#pylint: disable=E1101
        cv2.putText(img=image,text="angle = "+str(Utils.rotation),org=(30,490),fontFace=Utils.font,fontScale=0.5,color=(0,0,0),thickness=2)#pylint: disable=E1101
        cv2.putText(img=image,text="Linear Movement",org=(30,510),fontFace=Utils.font,fontScale=0.5,color=(255,0,0),thickness=2) #pylint: disable=E1101          
        cv2.putText(img=image,text="speed = "+str(round(Utils.speed,2)),org=(30,530),fontFace=Utils.font,fontScale=0.5,color=(0,0,0),thickness=2)#pylint: disable=E1101
        frame=cv2.hconcat([frame,image])#pylint: disable=E1101
        return frame
        
class SensorBar:
    """class to manage sensors"""
    show=1
    last_key=-1
    trail_flag=0
    
    @staticmethod
    def showpannel(frame,image):
        """
        SensorBar Bar GUI

        Parameters:
        frame (Mat): simulator frame
        image (Mat): blank HelpBar frame
        """
        
        cv2.putText(img=image,text="SensorBar",org=(10, 20),fontFace=Utils.font,fontScale=1,color=(9,0,0),thickness=2)#pylint: disable= E1101
        frame=cv2.hconcat([image,frame])#pylint: disable=E1101
        return frame
    
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
#pylint: disable=E1101
from sparkverse.gui.help_bar import HelpBar
from sparkverse.components.video import Video
class Utils():
    """a class where i dump yet non categorizable functions

    Parameters:
    rotation (int): car rotation
    speed (float): car speed
    x (int): car x position
    y (int): car y position
    description (string[]): HelpBar description
    keys (string[]): HelpBar keys
    """
    mask=np.array([])
    x,y=0,0
    rotation=0
    speed=0
    font = cv2.FONT_HERSHEY_SIMPLEX   #pylint: disable=E1101
    
    @staticmethod
    def draw(win, player_car,background):
        """function to draw character and background"""
        win.blit(background,(0,0))
        player_car.draw(win)
        pygame.display.update()

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
    def display(frame=None):
        """Special Display for our sensors"""
        mask=Utils.mask.copy()
        #if (not frame.any()):
            #frame=np.ones((mask.shape[0], mask.shape[1], mask.shape[2]), dtype=np.uint8)*255
            #cv2.putText(img=frame,text="No Sensor Input",org=(50,frame.shape[0]//2),fontFace=Utils.font,fontScale=2,color=(0,0,255),thickness=4)#pylint: disable=E1101
        concatenated=cv2.vconcat([frame,mask])
        """
        HelpBar display

        Parameters:
        frame (Mat): input frame
        """
        if Video.recorded==1:
            Video.start_time=time.time()
            Video.video_writer = cv2.VideoWriter(Video.output_file,Video.fourcc, Video.fps,(frame.shape[1],frame.shape[0]))
            Video.recorded=-1
        if Video.recorded==-1:
            Video.video_writer.write(frame)
            Video.end_time=time.time()
            Video.delta_time=Video.end_time-Video.start_time
        height,width,channels=concatenated.shape
        help_image = np.ones((height, width//2, channels), dtype=np.uint8)*255
        sensor_image = np.ones((height, width//2, channels), dtype=np.uint8)*255
        if HelpBar.show==1 and SensorBar.show==0:
            concatenated=HelpBar.showpannel(concatenated,help_image,Utils.x,Utils.y,Utils.rotation,Utils.speed)
        if HelpBar.show==1 and SensorBar.show==1:
            concatenated=HelpBar.showpannel(concatenated,help_image,Utils.x,Utils.y,Utils.rotation,Utils.speed)
            concatenated=SensorBar.showpannel(concatenated,sensor_image)
        if HelpBar.show==0 and SensorBar.show==1:
            concatenated=SensorBar.showpannel(concatenated,sensor_image)
        cv2.imshow("FramexMap",concatenated)#pylint: disable=E1101
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
            Video.reccording_flag=Video.reccording_flag^1
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
        if Video.reccording_flag==1 and Video.recorded!=-1:
            Video.recorded=1
        if Video.reccording_flag==0 and Video.recorded==-1:
            time.sleep(0.5)
            Video.video_writer.release()
            Video.recorded=0
            Video.end_time=time.time()
            

            #video_writer = cv2.VideoWriter(output_file, fourcc, fps, frame_size)
        if not moved:
            player_car.reduce_speed()

class SensorBar:
    """class to manage sensors"""
    show=1
    last_key=-1
    trail_flag=0

    selected_sensor=0
    sensor_count=0
    sensor_description=[]
    sensor_key=[]
    
    @staticmethod
    def showpannel(frame,image):
        """
        SensorBar Bar GUI
        
        Parameters:
        frame (Mat): simulator frame
        image (Mat): blank HelpBar frame
        """
        
        cv2.putText(img=image,text="SensorBar",org=(10, 20),fontFace=Utils.font,fontScale=1,color=(9,0,0),thickness=2)#pylint: disable= E1101
        if SensorBar.sensor_count>0:
            for i in range(SensorBar.sensor_count+1):
                cv2.rectangle(img=image,pt1=(10,30+i*40),pt2=(40,60+i*40),color=(0,0,0),thickness=3)#pylint: disable=E1101
                cv2.putText(img=image,text=SensorBar.sensor_key[i],org=(20,50+i*40),fontFace=Utils.font,fontScale=0.5,color=(0,0,0),thickness=2)#pylint: disable=E1101
                cv2.putText(img=image,text=SensorBar.sensor_description[i],org=(50,50+i*40),fontFace=Utils.font,fontScale=0.5,color=(0,0,0),thickness=2)#pylint: disable=E1101
        elif SensorBar.sensor_count==0:
                cv2.rectangle(img=image,pt1=(10,30),pt2=(40,60),color=(0,0,0),thickness=3)#pylint: disable=E1101
                cv2.putText(img=image,text=SensorBar.sensor_key[0],org=(20,50),fontFace=Utils.font,fontScale=0.5,color=(0,0,0),thickness=2)#pylint: disable=E1101
                cv2.putText(img=image,text=SensorBar.sensor_description[0],org=(50,50),fontFace=Utils.font,fontScale=0.5,color=(0,0,0),thickness=2)#pylint: disable=E1101
        frame=cv2.hconcat([image,frame])#pylint: disable=E1101
        return frame
    
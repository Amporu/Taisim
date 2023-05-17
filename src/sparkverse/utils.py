"""
info:This module contains a collection of non categorizable functions
autor: Tucudean Adrian-Ionut
date: 17.05.2023
email: Tucudean.Adrian.Ionut@outlook.com
license: MIT
"""

import cv2
import pygame
import numpy as np

class Utils:
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
    keys=["Q","H","R","W","A","S","D"]
    description=["Quit","Hide/Show",  #pylint: disable=C0301
                 "Reccord",
                 "Move Forward",
                 "Move Left",
                 "Move Backward",
                 "Move Right"]
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
        height,width,channels=frame.shape
        image = np.ones((height, width//2, channels), dtype=np.uint8)*255
        if HelpBar.show==1:
            HelpBar.showpannel(frame,image)
class HelpBar:
    """class for controlling HelpBar menu"""
    show = 0
    merg = 0
    @staticmethod
    def showpannel(frame,image):
        """
        Help Bar GUI

        Parameters:
        frame (Mat): simulator frame
        image (Mat): blank HelpBar frame
        """
        
        cv2.putText(img=image,text="HelpBar",org=(10, 20),fontFace=Utils.font,fontScale=1,color=(9,0,0),thickness=2)#pylint: disable=E1101
        for i in range(end=len(Utils.keys)):
            cv2.rectangle(img=image,pt1=(10,30+i*40),pt2=(40,60+i*40),color=(255,0,0),thickness=3)#pylint: disable=E1101
            cv2.putText(img=image,text=Utils.keys[i],org=(20,50+i*40),fontFace=Utils.font,fontScale=0.5,color=(0,0,255),thickness=2)#pylint: disable=E1101
            cv2.putText(img=image,text=Utils.description[i],org=(50,50+i*40),fontFace=Utils.font,fontScale=0.5,color=(0,0,255),thickness=2)#pylint: disable=E1101
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
        cv2.imshow("FramexMap",frame)#pylint: disable=E1101
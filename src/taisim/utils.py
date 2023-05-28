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
#pylint: disable=too-many-branches
#pylint: disable=too-many-statements

from taisim.gui.help_bar import HelpBar
from taisim.gui.sensor_bar import SensorBar
from taisim.components.video import Video
import taisim.external_data as ex
from taisim.components.log import logger
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
    sensor_frames = np.zeros((9,) + (480,640,3), dtype=np.uint8)
    first_window = np.ones((480, 640, 3), dtype=np.uint8)*255
    image=cv2.imread(ex.LOGO)
    frame=np.array([])
    lidar_flag=0
    #print(image.shape)
    image=cv2.resize(image,(640,480),cv2.INTER_AREA)
    quit_flag=0
    font = cv2.FONT_HERSHEY_SIMPLEX   #pylint: disable=E1101
    """
    cv2.rectangle(first_window[0],(0,0),(200,50),(255,255,255),-1)
    cv2.rectangle(first_window,(0,0),(200,50),(255,0,0),5)
    cv2.putText(img=first_window,
                text="Welcome Window",
                org=(20,20),
                fontFace=font,
                fontScale=0.5,
                color=(0,0,0),
                thickness=2)
    cv2.putText(img=first_window,
                text="SparkVerse Simulator",
                org=(250,30),fontFace=font,
                fontScale=0.7,
                color=(255,0,0),
                thickness=2)
    cv2.putText(img=first_window,
                text="Select to display sensor by pressing keys [1] -> [9]",
                org=(20,100),fontFace=font,fontScale=0.6,
                color=(0,0,255),thickness=2)
    cv2.putText(img=first_window,
                text="dependecies: OpenCV, NumPy, Pygame",
                org=(20,380),
                fontFace=font,
                fontScale=0.6,
                color=(0,0,0),
                thickness=2)
    cv2.putText(img=first_window,
                text="author: Tucudean Adrian-Ionut",
                org=(20,400),
                fontFace=font,
                fontScale=0.6,
                color=(0,0,0),
                thickness=2)
    cv2.putText(img=first_window,
                text="email: Tucudean.Adrian.Ionut@outlook.com",
                org=(20,420),fontFace=font,
                fontScale=0.6,
                color=(0,0,0),
                thickness=2)
    cv2.putText(img=first_window,
                text="github: https://github.com/Amporu/SparkVerse",
                org=(20,440),
                fontFace=font,
                fontScale=0.6,
                color=(0,0,255),
                thickness=2)
    """

    sensor_frames[0]=image
    mask=np.array([])
    x,y=0,0
    rotation=0
    speed=0


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
    def display():
        """
        HelpBar display

        Parameters:
        frame (Mat): input frame
        """
        frame=Utils.sensor_frames[SensorBar.last_key].copy()
        mask=Utils.mask.copy()
        concatenated=cv2.vconcat([frame,mask])

        height,width,channels=concatenated.shape
        help_image = np.ones((height, width//2, channels), dtype=np.uint8)*255
        sensor_image = np.ones((height, width//2, channels), dtype=np.uint8)*255
        if HelpBar.show==1 and SensorBar.show==0:
            concatenated=HelpBar.showpannel(concatenated,
                                            help_image,
                                            Utils.x,
                                            Utils.y,
                                            Utils.rotation,
                                            Utils.speed)
        if HelpBar.show==1 and SensorBar.show==1:
            concatenated=HelpBar.showpannel(concatenated,
                                            help_image,
                                            Utils.x,
                                            Utils.y,
                                            Utils.rotation,
                                            Utils.speed)
            concatenated=SensorBar.showpannel(concatenated,sensor_image)
        if HelpBar.show==0 and SensorBar.show==1:
            concatenated=SensorBar.showpannel(concatenated,sensor_image)
        if Video.recorded==1:
            Video.start_time=time.time()

            Video.video_writer = cv2.VideoWriter(Video.output_file,
                                                Video.fourcc,
                                                Video.fps,
                                                (concatenated.shape[1],concatenated.shape[0]))
            Video.recorded=-1
        if Video.recorded==-1:
            Video.video_writer.write(concatenated)
            Video.end_time=time.time()
            Video.delta_time=Video.end_time-Video.start_time
        cv2.imshow("FramexMap",concatenated)#pylint: disable=E1101
    @staticmethod
    def move_player(player_car):
        """key input for player car"""
        keys = pygame.key.get_pressed()
        moved = False
        num_keys=[pygame.K_1,
                  pygame.K_2,
                  pygame.K_3,
                  pygame.K_4,
                  pygame.K_5,
                  pygame.K_6,
                  pygame.K_7,
                  pygame.K_8,
                  pygame.K_9]
        for i ,key in enumerate(num_keys):
            if keys[key]:
                SensorBar.last_key=i+1
                logger.info("<\033[38;2;255;165;0m%s\033[0m> : \033[92mSELECTED\033[0m",
                            SensorBar.sensor_description[i])
                time.sleep(0.5)
        if keys[pygame.K_q]:#pylint: disable=E1101
            HelpBar.last_key=0
            Utils.quit_flag==1
            pygame.quit()#pylint: disable=E1101
            quit()
        if keys[pygame.K_r]:#pylint: disable=E1101
            HelpBar.last_key=2
            time.sleep(0.5)
            Video.reccording_flag=Video.reccording_flag^1
            if Video.reccording_flag==1:
                logger.info("RECCORDING : \033[92mENABLED\033[0m")
            else:
                logger.info("RECCORDING : \033[91mDISABLED\033[0m")
        if keys[pygame.K_t]:#pylint: disable=E1101
            HelpBar.last_key=7

            HelpBar.trail_flag=HelpBar.trail_flag^1
            if HelpBar.trail_flag==1:
                logger.info("TRAIL : \033[92mENABLED\033[0m")
            else:
                logger.info("TRAIL : \033[91mDISABLED\033[0m")
            time.sleep(0.5)
        if keys[pygame.K_h]:#pylint: disable=E1101
            HelpBar.last_key=1
            HelpBar.show=HelpBar.show^1
            if HelpBar.show==1:
                logger.info("HELP BAR : \033[92mVISIBLE\033[0m")
            else:
                logger.info("HELP BAR : \033[91mHIDDEN\033[0m")
            time.sleep(0.5)
        if keys[pygame.K_e]:#pylint: disable=E1101
            SensorBar.show=SensorBar.show^1
            if SensorBar.show==1:
                logger.info("SENSOR BAR : \033[92mVISIBLE\033[0m")
            else:
                logger.info("SENSOR BAR : \033[91mHIDDEN\033[0m")
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
        if not moved:
            player_car.reduce_speed()

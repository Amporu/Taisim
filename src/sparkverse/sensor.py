"""
info:This is a the sensor module for our simulator
autor: Tucudean Adrian-Ionut
date: 19.05.2023
email: Tucudean.Adrian.Ionut@outlook.com
license: MIT
"""
import cv2
import pygame
from sparkverse.utils import Utils
class VirtualSensor:
    """class to generalize sensors we use"""
    def __init__(self,win,x,y,clock,flag,fps,track,angle):
        """class constructor
        Parameters:
        x (int): x position of the car centroid
        y (int): y position of the car centroid
        angle (int): angle of the sensor (0 means front of the car)
        """
        self.clock=clock
        self.flag=flag
        self.pos_x=x
        self.pos_y=y
        self.angle=angle
        self.win=win
        self.fps=fps
        self.track=track
class Camera(VirtualSensor):
    """ class for camera handling"""
    def __init__(self,simulator, angle=0,hfov=45,vfov=60):
        """
        info:camera class constructor

        Parameters:
        simulator (Simulator obj): simulator obj for pygame operations
        angle (int): sensor angle perspective
        hfov (int): horizontal FoV
        vfov (int): vertical FoV
        """
        super().__init__(win=simulator[0],
                         x=simulator[1].x_value,
                         y=simulator[1].y_value,
                         clock=simulator[2],
                         flag=simulator[3],
                         fps=simulator[4],
                         track=simulator[5],
                         angle=angle)
        self.hfov=hfov
        self.vfov=vfov
        self.player=simulator[1]
    def read(self):
        """function to read camera data
        Returns: 
        Track_image (Mat): the track of the simulator,
        camera_image (Mat): the camera perspective
        """
        self.clock.tick(self.fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.flag = False
                break
        angle=self.player.angle
        angle=angle%360
        Utils.move_player(self.player)
        frame = pygame.surfarray.array3d(pygame.display.get_surface())
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        frame=cv2.flip(frame,1)
        h,w=frame.shape[0],frame.shape[1]
        x,y=int(self.player.x_value),int(self.player.y_value)
        Utils.x,Utils.y=x,y
        return frame









class Lidar(VirtualSensor):
    """class for lidar handling"""
    def __init__(self,simulator,angle=0,angular_resolution=10):
        """ class constructor"""
        super().__init__(win=simulator[0],
                         x=simulator[1].x_value,
                         y=simulator[1].y_value,
                         clock=simulator[2],
                         flag=simulator[3],
                         fps=simulator[4],
                         track=simulator[5],
                         angle=angle)
        self.angular_resolution=angular_resolution
    def read(self):
        """function to read lidar data
        Returns: 
        Track_image (Mat): the track of the simulator,
        lidar_data_array (numpy.array[]): the lidar measurememnt
        """
        self.clock.tick(self.fps)
        print("lidar  sensor")
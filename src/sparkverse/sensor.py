"""
info:This is a the sensor module for our simulator
autor: Tucudean Adrian-Ionut
date: 19.05.2023
email: Tucudean.Adrian.Ionut@outlook.com
license: MIT
"""
#pylint: disable=C0301
import math
import cv2
import pygame
import numpy as np
from sparkverse.utils import Utils,SensorBar
from sparkverse.gui.help_bar import HelpBar
#pylint: disable=E1101
#pylint: disable=C0303
class VirtualSensor:
    """class to generalize sensors we use"""
    mask=np.array([])
    mask_flag=0
    sensor_count=0
    def __init__(self,win,xval,yval,clock,flag,fps,track,angle):
        """class constructor
        Parameters:
        x (int): x position of the car centroid
        y (int): y position of the car centroid
        angle (int): angle of the sensor (0 means front of the car)
        """
        self.sensor_count=VirtualSensor.sensor_count
        SensorBar.sensor_count=self.sensor_count
        SensorBar.sensor_description.append("cam"+str(self.sensor_count))
        SensorBar.sensor_key.append(str(self.sensor_count+1))
        VirtualSensor.sensor_count=VirtualSensor.sensor_count+1
        self.clock=clock
        self.flag=flag
        self.pos_x=xval
        self.pos_y=yval
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
        player (PlayerCar obj): to get data from the car
        """
        super().__init__(win=simulator()[0],
                         xval=simulator()[1].x_value,
                         yval=simulator()[1].y_value,
                         clock=simulator()[2],
                         flag=simulator()[3],
                         fps=simulator()[4],
                         track=simulator()[5],
                         angle=angle)
        self.hfov=hfov
        self.vfov=vfov
        self.player=simulator()[1]
    
    def read(self):
        """function to read camera data
        Returns: 
        Track_image (Mat): the track of the simulator,
        camera_image (Mat): the camera perspective
        """
        self.clock.tick(self.fps)

        Utils.draw(self.win,self.player,self.track)
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
        Utils.x,Utils.y=int(self.player.x_value),int(self.player.y_value)
        x_1 = int(self.player.x_value + 20 * math.cos(math.radians(self.angle+angle+180)))
        y_1 = int(self.player.y_value - 20 * math.sin(math.radians(self.angle+angle+180)))
        x_2 = int(self.player.x_value + 20 * math.cos(math.radians(self.angle+angle)))
        y_2 = int(self.player.y_value - 20 * math.sin(math.radians(self.angle+angle)))
        x_3 = int(self.player.x_value + 60 * math.cos(math.radians(self.angle+angle+130)))
        y_3 = int(self.player.y_value - 60 * math.sin(math.radians(self.angle+angle+130)))
        x_4 = int(self.player.x_value + 60 * math.cos(math.radians(self.angle+angle+50)))
        y_4 = int(self.player.y_value - 60 * math.sin(math.radians(self.angle+angle+50)))
        points = [(x_1, y_1), (x_2,y_2), (x_3,y_3), (x_4,y_4)]
        sorted_points = sorted(points, key=lambda x: (x[0], x[1]))

    # Find the top-left and bottom-left points
        if sorted_points[0][1] < sorted_points[1][1]:
            top_left = sorted_points[0]
            bottom_left = sorted_points[1]
        else:
            top_left = sorted_points[1]
            bottom_left = sorted_points[0]

        # Find the top-right and bottom-right points
        if sorted_points[2][1] < sorted_points[3][1]:
            top_right = sorted_points[2]
            bottom_right = sorted_points[3]
        else:
            top_right = sorted_points[3]
            bottom_right = sorted_points[2]
        if self.sensor_count==0:
            Utils.mask = frame.copy()
            
        min_x = min(top_left[0], top_right[0], bottom_left[0], bottom_right[0])
        max_x = max(top_left[0], top_right[0], bottom_left[0], bottom_right[0])
        min_y = min(top_left[1], top_right[1], bottom_left[1], bottom_right[1])
        max_y = max(top_left[1], top_right[1], bottom_left[1], bottom_right[1])
        if min_x < 10 or max_x > 630 or min_y<10 or max_y>470:
            self.player.bounce_back()
        cv2.line(Utils.mask,(int(bottom_left[0]),int(bottom_left[1])),(int(bottom_right[0]),int(bottom_right[1])),(255,255,255),2)
        cv2.line(Utils.mask,(int(bottom_right[0]),int(bottom_right[1])),(int(top_right[0]),int(top_right[1])),(255,255,255),2)
        cv2.line(Utils.mask,(int(top_right[0]),int(top_right[1])),(int(top_left[0]),int(top_left[1])),(255,255,255),2)
        cv2.line(Utils.mask,(int(top_left[0]),int(top_left[1])),(int(bottom_left[0]),int(bottom_left[1])),(255,255,255),2)
        
        tl_rect_x=min((top_left[0],bottom_left[0]))
        tl_rect_y=min((top_left[1],top_right[1]))
        br_rect_x=max((top_right[0],bottom_right[0]))
        br_rect_y=max((bottom_left[1],bottom_right[1]))
        alpha=br_rect_x-tl_rect_x
        beta=br_rect_y-tl_rect_y
        if alpha>beta:
            tl_rect_y=tl_rect_y-(alpha-beta)//2
            br_rect_y=br_rect_y+(alpha-beta)//2
        else:
            tl_rect_x=tl_rect_x-(beta-alpha)//2
            br_rect_x=br_rect_x+(beta-alpha)//2
        if SensorBar.last_key==self.sensor_count+1:
            cv2.circle(Utils.mask,(int(bottom_left[0]),int(bottom_left[1])),5,(0,255,0),1)
            cv2.circle(Utils.mask,(int(bottom_right[0]),int(bottom_right[1])),5,(0,0,255),1)
            cv2.circle(Utils.mask,(int(top_left[0]),int(top_left[1])),5,(255,255,0),1)
            cv2.circle(Utils.mask,(int(top_right[0]),int(top_right[1])),5,(0,255,255),1)
            cv2.rectangle(Utils.mask,(tl_rect_x,tl_rect_y),(br_rect_x,br_rect_y),(255,0,255),2)
            cv2.circle(Utils.mask,(tl_rect_x,tl_rect_y),5,(255,255,0),1)
            cv2.circle(Utils.mask,(tl_rect_x,br_rect_y),5,(0,255,0),1)
            cv2.circle(Utils.mask,(br_rect_x,tl_rect_y),5,(0,255,255),1)
            cv2.circle(Utils.mask,(br_rect_x,br_rect_y),5,(0,0,255),1)
            cv2.line(Utils.mask,(int(bottom_left[0]),int(bottom_left[1])),(tl_rect_x,br_rect_y),(0,255,0),2,cv2.LINE_AA)
            cv2.line(Utils.mask,(int(bottom_right[0]),int(bottom_right[1])),(br_rect_x,br_rect_y),(0,0,255),2,cv2.LINE_AA)
            cv2.line(Utils.mask,(int(top_right[0]),int(top_right[1])),(br_rect_x,tl_rect_y),(0,255,255),2,cv2.LINE_AA)
            cv2.line(Utils.mask,(int(top_left[0]),int(top_left[1])),(tl_rect_x,tl_rect_y),(255,255,0),2,cv2.LINE_AA)
            
        frame1=frame[tl_rect_y:br_rect_y,tl_rect_x:br_rect_x]
        height, width = frame1.shape[:2]
        center = (width / 2, height / 2)
        if HelpBar.trail_flag==1:
            HelpBar.enable_trail(self.player,Utils.mask)
        moment = cv2.getRotationMatrix2D(center, -(self.angle+angle), 1.0)
        rot_img = cv2.warpAffine(frame1, moment, (100, 100))
        rot_img=cv2.resize(rot_img,(640,480),cv2.INTER_AREA)#pylint: disable=E1101
        rot_img=rot_img[0:240,0:640]
        self.rotated_img=cv2.resize(rot_img,(640,480),cv2.INTER_AREA)#pylint: disable=E1101
        cv2.rectangle(self.rotated_img,(0,0),(200,50),(255,255,255),-1)
        cv2.rectangle(self.rotated_img,(0,0),(200,50),(255,0,0),5)
        cv2.putText(img=self.rotated_img,
                    text=str(SensorBar.sensor_description[self.sensor_count]),org=(20,20),fontFace=Utils.font,fontScale=0.5,color=(0,0,0),thickness=2)#pylint: disable=E1101
        Utils.sensor_frames[self.sensor_count+1]=self.rotated_img
        return self.rotated_img

class Lidar(VirtualSensor):
    """class for lidar handling"""
    def __init__(self,simulator,angle=0,angular_resolution=10):
        """ class constructor"""
        super().__init__(win=simulator()[0],
                         xval=simulator()[1].x_value,
                         yval=simulator()[1].y_value,
                         clock=simulator()[2],
                         flag=simulator()[3],
                         fps=simulator()[4],
                         track=simulator()[5],
                         angle=angle)
        self.player=simulator()[1]
        self.angular_resolution=angular_resolution
    def read(self):
        """function to read lidar data
        Returns: 
        Track_image (Mat): the track of the simulator,
        lidar_data_array (numpy.array[]): the lidar measurememnt
        """
        self.clock.tick(self.fps)

        Utils.draw(self.win,self.player,self.track)
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
        Utils.x,Utils.y=int(self.player.x_value),int(self.player.y_value)
        x_1 = int(self.player.x_value + 20 * math.cos(math.radians(self.angle+angle+180)))
        y_1 = int(self.player.y_value - 20 * math.sin(math.radians(self.angle+angle+180)))
        x_2 = int(self.player.x_value + 20 * math.cos(math.radians(self.angle+angle)))
        y_2 = int(self.player.y_value - 20 * math.sin(math.radians(self.angle+angle)))
        x_3 = int(self.player.x_value + 60 * math.cos(math.radians(self.angle+angle+130)))
        y_3 = int(self.player.y_value - 60 * math.sin(math.radians(self.angle+angle+130)))
        x_4 = int(self.player.x_value + 60 * math.cos(math.radians(self.angle+angle+50)))
        y_4 = int(self.player.y_value - 60 * math.sin(math.radians(self.angle+angle+50)))
        lines=[]
        step=360/self.angular_resolution
        for i in range(self.angular_resolution):
            if i==0:
                lines.append(-(self.angle+angle+step))
            else:
                lines.append(lines[i-1]-step)
        #print(lines)
        lidar_distance=[]
        x_p=[]
        y_p=[]
        x_lidar=[]
        y_lidar=[]
        mask_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        for i in range(self.angular_resolution):
            x_p1 = self.player.x_value + 30 * math.cos(math.radians(lines[i]))
            y_p1= self.player.y_value + 30 * math.sin(math.radians(lines[i]))
            x_p.append(int(x_p1))
            y_p.append(int(y_p1))
            distance=0
        #for i in range(self.angular_resolution):
            x_lid=0
            y_lid=0
            ok=0
            for j in range(1000):
                x_lid=int(x_p1 + j * math.cos(math.radians(lines[i])))
                y_lid=int(y_p1 + j * math.sin(math.radians(lines[i])))
                
                if (mask_gray[y_lid][x_lid]==0) and x_lid>10 and x_lid<mask_gray.shape[1]-10 and y_lid>10 and y_lid<mask_gray.shape[0]-10:
                    distance=distance+1
                else:
                    ok=1
                    x_lidar.append(x_lid)
                    y_lidar.append(y_lid)
                    lidar_distance.append(distance)
                    break
            if ok==0:
                x_lidar.append(x_lid)
                y_lidar.append(y_lid)
                lidar_distance.append(distance)
                
        #print(y_lidar)
        #print(x_lidar)
        #print(lines)
        if self.sensor_count==0:
            Utils.mask = frame.copy()
        #print(lidar_distance)
        for i in range(self.angular_resolution):
            cv2.line(Utils.mask,(x_p[i],y_p[i]),(x_lidar[i],y_lidar[i]),(0,255,0),1)
        
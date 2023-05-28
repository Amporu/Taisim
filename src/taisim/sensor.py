"""
info:This is a the sensor module for our simulator
autor: Tucudean Adrian-Ionut
date: 19.05.2023
email: Tucudean.Adrian.Ionut@outlook.com
license: MIT
"""
#pylint: disable=E1101
#pylint: disable=too-many-instance-attributes
#pylint: disable=all
import math
import cv2
import pygame
import numpy as np
from taisim.utils import Utils,SensorBar
from taisim.gui.help_bar import HelpBar
from taisim.simulator import Simulator
from taisim.components.log import logger
from taisim.external_data import COMPASS ,GPS
COMPASS_IMAGE=pygame.image.load(COMPASS)
GPS_IMAGE=pygame.image.load(GPS)
class VirtualSensor:
    """class to generalize sensors we use"""
    mask=np.array([])
    mask_flag=0
    sensor_count=0
    def __init__(self,simulator,title,angle,sensor_type):
        """class constructor
        Parameters:
        x (int): x position of the car centroid
        y (int): y position of the car centroid
        angle (int): angle of the sensor (0 means front of the car)
        """
        if sensor_type==1 :
            logger.info("sensor <\033[38;2;255;165;0m%s\033[0m> added as \033[94mCAMERA\033[0m",
                        title)
        if sensor_type==2 :
            logger.info("sensor <\033[38;2;255;165;0m%s\033[0m> added as \033[94mLIDAR\033[0m",
                        title)
        if sensor_type==3:
            logger.info("sensor <\033[38;2;255;165;0m%s\033[0m> added as \033[94mCOMPASS\033[0m",
                        title)
        if sensor_type==4:
            logger.info("sensor <\033[38;2;255;165;0m%s\033[0m> added as \033[94mGPS\033[0m",
                        title)
        self.sensor_count=VirtualSensor.sensor_count
        SensorBar.sensor_count=self.sensor_count
        SensorBar.sensor_description.append(title)
        SensorBar.sensor_key.append(str(self.sensor_count+1))
        VirtualSensor.sensor_count=VirtualSensor.sensor_count+1
        self.clock=simulator[2]
        self.flag=simulator[3]
        self.pos_x=simulator[1].x_value
        self.pos_y=simulator[1].y_value
        self.angle=angle
        self.win=simulator[0]
        self.fps=simulator[4]
        self.track=simulator[5]
        self.rotated_img=np.array([])
class Compass(VirtualSensor):
    """ class for compass handling"""
    def __init__(self,title="compass"):
        sim=Simulator.data()

        super().__init__(simulator=sim,title=title,angle=0,sensor_type=3)

        self.player=sim[1]

    def read(self):
        if self.sensor_count==0:
            self.clock.tick(self.fps)

            Utils.draw(self.win,self.player,self.track)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.flag = False
                    break
        angle=self.player.angle
        angle=angle%360
        if self.sensor_count==0:
            Utils.move_player(self.player)

        
            frame = pygame.surfarray.array3d(pygame.display.get_surface())
            frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
            Utils.frame=cv2.flip(frame,1)
        frame=Utils.frame
        h,w,c=frame.shape
        x_1 = int(self.player.x_value + 20 * math.cos(math.radians(self.angle+angle+90)))
        y_1 = int(self.player.y_value - 20 * math.sin(math.radians(self.angle+angle+90)))
        x_2 = int(self.player.x_value + 20 * math.cos(math.radians(self.angle+angle+180)))
        y_2 = int(self.player.y_value - 20 * math.sin(math.radians(self.angle+angle+180)))
        x_3 = int(self.player.x_value + 20 * math.cos(math.radians(self.angle+angle+270)))
        y_3 = int(self.player.y_value - 20 * math.sin(math.radians(self.angle+angle+270)))
        x_4 = int(self.player.x_value + 20 * math.cos(math.radians(self.angle+angle)))
        y_4 = int(self.player.y_value - 20 * math.sin(math.radians(self.angle+angle)))
        cv2.line(frame,(x_1,y_1),(x_2,y_2),(255,0,0),2)
        cv2.line(frame,(x_3,y_3),(x_4,y_4),(0,0,255),2)
        cv2.line(frame,(x_1,y_1),(x_4,y_4),(255,0,0),2)
        cv2.line(frame,(x_3,y_3),(x_2,y_2),(0,0,255),2)
        #cv2.line(frame,(int(self.player.x_value),0),(int(self.player.x_value),h),(0,255,0),1)
        #cv2.line(frame,(0,int(self.player.y_value)),(w,int(self.player.y_value)),(0,255,0),1)
        Utils.sensor_frames[self.sensor_count+1]=frame
        #self.win.blit(COMPASS_IMAGE,(0,0))
        return self.player.angle
class Gps(VirtualSensor):
    """ class for gps handling"""
    def __init__(self,title="compass"):
        """compass initialization"""
        sim=Simulator.data()
        super().__init__(simulator=sim,title=title,angle=0,sensor_type=4)

        self.player=sim[1]
    def read(self):
        self.win.blit(GPS_IMAGE,(self.pos_x-10,self.pos_y-10))
        """Read gps data"""
        if self.sensor_count==0:
            self.clock.tick(self.fps)

            Utils.draw(self.win,self.player,self.track)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.flag = False
                    break
        angle=self.player.angle
        angle=angle%360
        

        if self.sensor_count==0:
            Utils.move_player(self.player)
            frame = pygame.surfarray.array3d(pygame.display.get_surface())
            frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
            Utils.frame=cv2.flip(frame,1)
        frame=Utils.frame
        h,w,c=frame.shape
        x_1 = int(self.player.x_value + 20 * math.cos(math.radians(self.angle+angle+90)))
        y_1 = int(self.player.y_value - 20 * math.sin(math.radians(self.angle+angle+90)))
        x_2 = int(self.player.x_value + 20 * math.cos(math.radians(self.angle+angle+180)))
        y_2 = int(self.player.y_value - 20 * math.sin(math.radians(self.angle+angle+180)))
        x_3 = int(self.player.x_value + 20 * math.cos(math.radians(self.angle+angle+270)))
        y_3 = int(self.player.y_value - 20 * math.sin(math.radians(self.angle+angle+270)))
        x_4 = int(self.player.x_value + 20 * math.cos(math.radians(self.angle+angle)))
        y_4 = int(self.player.y_value - 20 * math.sin(math.radians(self.angle+angle)))
        cv2.line(frame,(x_1,y_1),(x_2,y_2),(255,0,0),2)
        cv2.line(frame,(x_3,y_3),(x_4,y_4),(0,0,255),2)
        cv2.line(frame,(x_1,y_1),(x_4,y_4),(255,0,0),2)
        cv2.line(frame,(x_3,y_3),(x_2,y_2),(0,0,255),2)
        cv2.line(frame,(int(self.player.x_value),0),(int(self.player.x_value),h),(0,255,0),1)
        cv2.line(frame,(0,int(self.player.y_value)),(w,int(self.player.y_value)),(0,255,0),1)
        Utils.sensor_frames[self.sensor_count+1]=frame
        return self.pos_x,self.pos_y
class Camera(VirtualSensor):
    """ class for camera handling"""

    def __init__(self,title="camera", angle=0):
        """
        info:camera class constructor
        
        Parameters:
        simulator (Simulator obj): simulator obj for pygame operations
        angle (int): sensor angle perspective
        hfov (int): horizontal FoV
        vfov (int): vertical FoV
        player (PlayerCar obj): to get data from the car
        """
        sim=Simulator.data()

        super().__init__(simulator=sim,title=title,angle=angle,sensor_type=1)

        self.player=sim[1]

    def read(self):
        """function to read camera data
        Returns: 
        Track_image (Mat): the track of the simulator,
        camera_image (Mat): the camera perspective
        """
        if self.sensor_count==0:
            self.clock.tick(self.fps)

            Utils.draw(self.win,self.player,self.track)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.flag = False
                    break
        angle=self.player.angle
        angle=angle%360
            
        if self.sensor_count==0:
            Utils.move_player(self.player)
            frame = pygame.surfarray.array3d(pygame.display.get_surface())
            frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
            Utils.frame=cv2.flip(frame,1)
        frame=Utils.frame
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
        cv2.line(img=Utils.mask,
                 pt1=(int(bottom_left[0]),int(bottom_left[1])),
                 pt2=(int(bottom_right[0]),int(bottom_right[1])),
                 color=(255,255,255),
                 thickness=2)
        cv2.line(img=Utils.mask,
                 pt1=(int(bottom_right[0]),int(bottom_right[1])),
                 pt2=(int(top_right[0]),int(top_right[1])),
                 color=(255,255,255),
                 thickness=2)
        cv2.line(img=Utils.mask,
                 pt1=(int(top_right[0]),int(top_right[1])),
                 pt2=(int(top_left[0]),int(top_left[1])),
                 color=(255,255,255),
                 thickness=2)
        cv2.line(img=Utils.mask,
                 pt1=(int(top_left[0]),int(top_left[1])),
                 pt2=(int(bottom_left[0]),int(bottom_left[1])),
                 color=(255,255,255),
                 thickness=2)

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
            cv2.line(img=Utils.mask,
                     pt1=(int(bottom_left[0]),int(bottom_left[1])),
                     pt2=(tl_rect_x,br_rect_y),
                     color=(0,255,0),thickness=2)
            cv2.line(img=Utils.mask,
                     pt1=(int(bottom_right[0]),int(bottom_right[1])),
                     pt2=(br_rect_x,br_rect_y),
                     color=(0,0,255),
                     thickness=2)
            cv2.line(img=Utils.mask,
                     pt1=(int(top_right[0]),int(top_right[1])),
                     pt2=(br_rect_x,tl_rect_y),
                     color=(0,255,255),
                     thickness=2)
            cv2.line(img=Utils.mask,
                     pt1=(int(top_left[0]),int(top_left[1])),
                     pt2=(tl_rect_x,tl_rect_y),
                     color=(255,255,0),
                     thickness=2)

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
                    text=str(SensorBar.sensor_description[self.sensor_count]),
                    org=(20,20),
                    fontFace=Utils.font,
                    fontScale=0.5,
                    color=(0,0,0),
                    thickness=2)
        Utils.sensor_frames[self.sensor_count+1]=self.rotated_img
        return self.rotated_img

class Lidar(VirtualSensor):
    """class for lidar handling"""
    def __init__(self,title="Lidar",angle=0,angular_resolution=10):
        sim=Simulator.data()
        """ class constructor"""
        super().__init__(simulator=sim,title=title,angle=angle,sensor_type=2)
        self.player=sim[1]
        self.angular_resolution=angular_resolution
    def read(self):
        """function to read lidar data
        Returns: 
        Track_image (Mat): the track of the simulator,
        lidar_data_array (numpy.array[]): the lidar measurememnt
        """
        if self.sensor_count==0:
            self.clock.tick(self.fps)

            Utils.draw(self.win,self.player,self.track)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.flag = False
                    break
        angle=self.player.angle
        angle=angle%360
        
        if self.sensor_count==0:
            Utils.move_player(self.player)
            frame = pygame.surfarray.array3d(pygame.display.get_surface())
            frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
            Utils.frame=cv2.flip(frame,1)
        frame=Utils.frame
        Utils.x,Utils.y=int(self.player.x_value),int(self.player.y_value)
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
        space=20
        mask_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        for i in range(self.angular_resolution):

            x_p1 = self.player.x_value + space * math.cos(math.radians(lines[i]))
            y_p1= self.player.y_value + space * math.sin(math.radians(lines[i]))
            x_p.append(int(x_p1))
            y_p.append(int(y_p1))
            distance=0
        #for i in range(self.angular_resolution):
            x_lid=0
            y_lid=0
            ok_flag=0
            for j in range(1000):
                x_lid=int(x_p1 + j * math.cos(math.radians(lines[i])))
                y_lid=int(y_p1 + j * math.sin(math.radians(lines[i])))

                if ((mask_gray[y_lid][x_lid]==0) and x_lid>10 and
                    x_lid<mask_gray.shape[1]-10 and y_lid>10
                    and y_lid<mask_gray.shape[0]-10):
                    distance=distance+1
                else:
                    ok_flag=1
                    x_lidar.append(x_lid)
                    y_lidar.append(y_lid)
                    lidar_distance.append(distance)
                    break
            if ok_flag==0:
                x_lidar.append(x_lid)
                y_lidar.append(y_lid)
                lidar_distance.append(distance)
        if self.sensor_count==0:
            Utils.mask = frame.copy()
        for i in range(self.angular_resolution):
            cv2.circle(Utils.mask,(int(self.player.x_value),int(self.player.y_value)),space,(255,255,255),2)
            if SensorBar.last_key==self.sensor_count+1:
                cv2.circle(Utils.mask,(int(self.player.x_value),int(self.player.y_value)),space,(255,0,255),2)
                cv2.line(Utils.mask,(x_p[i],y_p[i]),(x_lidar[i],y_lidar[i]),(0,255,0),1)
        return lidar_distance,lines
        
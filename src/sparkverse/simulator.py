"""
info:This module contains the implememntation of the SparkVerse Simulator
autor: Tucudean Adrian-Ionut
date: 17.05.2023
email: Tucudean.Adrian.Ionut@outlook.com
license: MIT
"""

import math
import pygame
import numpy as np
import cv2
import sparkverse.external_data as ex
import sparkverse.player as pl
from sparkverse.utils import Utils,HelpBar,draw
from sparkverse.sensor import Camera
#pylint: disable-all

class Simulator:
    """simulator class"""
    TRACK=pygame.image.load(ex.LEVEL1)
    WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))#),pygame.NOFRAME | pygame.HIDDEN)
    TITLE=pygame.display.set_caption("Pygame SIMULATOR")
    
    isRunning = True
    clock = pygame.time.Clock()
    player_car = pl.PlayerCar(2, 2)
    FPS=30
    @staticmethod
    def data():
        return Simulator.WIN,Simulator.player_car, Simulator.clock,Simulator.isRunning,Simulator.FPS
    @staticmethod
    def hide_simulator_window():
        """this function hids the pygame simulator window"""
        Simulator.WIN = pygame.display.set_mode((Simulator.WIDTH, Simulator.HEIGHT),pygame.NOFRAME | pygame.HIDDEN)

    @staticmethod
    def getpos():
        return pl.START_POS
    
    @staticmethod
    def setpos(x,y):
        pl.START_POS[0],pl.START_POS[1]=x,y
    @staticmethod
    def setfps(fps):
        Simulator.FPS=fps
    @staticmethod
    def setmap(map=ex.LEVEL1):
        if map==1:
            Simulator.TRACK=pygame.image.load(ex.LEVEL1)
        elif map==2:
            Simulator.TRACK=pygame.image.load(ex.LEVEL2)#
        elif map==3:
            Simulator.TRACK=pygame.image.load(ex.LEVEL3)
        elif map==4:
            Simulator.TRACK=pygame.image.load(ex.LEVEL4)
        elif map==5:
            Simulator.TRACK=pygame.image.load(ex.LEVEL5)
        elif map==6:
            Simulator.TRACK=pygame.image.load(ex.LEVEL6)
        elif map==7:
            Simulator.TRACK=pygame.image.load(ex.LEVEL7)
        else:
            Simulator.TRACK=pygame.image.load(map)
    def start():
        Simulator.setMap(ex.LEVEL1)

    def getCamera():
        #pass
        Simulator.clock.tick(Simulator.FPS)
        #1
        draw(Simulator.WIN,Simulator.player_car,Simulator.TRACK)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Simulator.isRunning = False
                break
        angle=Simulator.player_car.angle
        angle=angle%360
        #print(angle)
        Utils.move_player(Simulator.player_car)
        frame = pygame.surfarray.array3d(pygame.display.get_surface())
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        frame=cv2.flip(frame,1)
        h,w=frame.shape[0],frame.shape[1]
        x,y=int(Simulator.player_car.x_value),int(Simulator.player_car.y_value)
        Utils.x,Utils.y=x,y
        x=x+4
        
        x1 = int(x + 20 * math.cos(math.radians(angle+180)))
        y1 = int(y - 20 * math.sin(math.radians(angle+180)))
        x2 = int(x + 20 * math.cos(math.radians(angle)))
        y2 = int(y - 20 * math.sin(math.radians(angle)))
        x3 = int(x + 60 * math.cos(math.radians(angle+130)))
        y3 = int(y - 60 * math.sin(math.radians(angle+130)))
        x4 = int(x + 60 * math.cos(math.radians(angle+50)))
        y4 = int(y - 60 * math.sin(math.radians(angle+50)))
        
    # print(player_car.x)
        
        
        points = [(x1, y1), (x2,y2), (x3,y3), (x4,y4)]
        
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
            
        vertices=np.array([
            [top_left[0],top_left[1]],
            [top_right[0],top_right[1]],
            [bottom_right[0],bottom_right[1]],
            [bottom_left[0],bottom_left[1]]],np.int32)
        mask = frame.copy()
        try:
            cv2.line(mask,(int(bottom_left[0]),int(bottom_left[1])),(int(bottom_right[0]),int(bottom_right[1])),(255,255,255),2)
            cv2.line(mask,(int(bottom_right[0]),int(bottom_right[1])),(int(top_right[0]),int(top_right[1])),(255,255,255),2)
            cv2.line(mask,(int(top_right[0]),int(top_right[1])),(int(top_left[0]),int(top_left[1])),(255,255,255),2)
            cv2.line(mask,(int(top_left[0]),int(top_left[1])),(int(bottom_left[0]),int(bottom_left[1])),(255,255,255),2)
            cv2.circle(mask,(int(bottom_left[0]),int(bottom_left[1])),5,(0,255,0),1)
            cv2.circle(mask,(int(bottom_right[0]),int(bottom_right[1])),5,(0,0,255),1)
            cv2.circle(mask,(int(top_left[0]),int(top_left[1])),5,(255,255,0),1)
            cv2.circle(mask,(int(top_right[0]),int(top_right[1])),5,(0,255,255),1)
        except Exception as e:
        # def show_game_over_message():
            font = pygame.font.Font(None, 36)
            text = font.render(str(e), True, (255, 0, 0))
            text_rect = text.get_rect(center=(Simulator.WIDTH // 2, Simulator.HEIGHT // 2))
            Simulator.WIN.blit(text, text_rect)
            pygame.display.flip()

        tl_rect_x=min((top_left[0],bottom_left[0]))
        tl_rect_y=min((top_left[1],top_right[1]))
        br_rect_x=max((top_right[0],bottom_right[0]))
        br_rect_y=max((bottom_left[1],bottom_right[1]))
        a=br_rect_x-tl_rect_x
        b=br_rect_y-tl_rect_y
        if a>b:
            tl_rect_y=tl_rect_y-(a-b)//2
            br_rect_y=br_rect_y+(a-b)//2
        else:
            tl_rect_x=tl_rect_x-(b-a)//2
            br_rect_x=br_rect_x+(b-a)//2
        cv2.rectangle(mask,(tl_rect_x,tl_rect_y),(br_rect_x,br_rect_y),(255,0,255),1)
        cv2.circle(mask,(tl_rect_x,tl_rect_y),5,(255,255,0),1)
        cv2.circle(mask,(tl_rect_x,br_rect_y),5,(0,255,0),1)
        cv2.circle(mask,(br_rect_x,tl_rect_y),5,(0,255,255),1)
        cv2.circle(mask,(br_rect_x,br_rect_y),5,(0,0,255),1)

        cv2.line(mask,(int(bottom_left[0]),int(bottom_left[1])),(tl_rect_x,br_rect_y),(0,255,0),2,cv2.LINE_AA)
        cv2.line(mask,(int(bottom_right[0]),int(bottom_right[1])),(br_rect_x,br_rect_y),(0,0,255),2,cv2.LINE_AA)
        cv2.line(mask,(int(top_right[0]),int(top_right[1])),(br_rect_x,tl_rect_y),(0,255,255),2,cv2.LINE_AA)
        cv2.line(mask,(int(top_left[0]),int(top_left[1])),(tl_rect_x,tl_rect_y),(255,255,0),2,cv2.LINE_AA)
        frame1=frame[tl_rect_y:br_rect_y,tl_rect_x:br_rect_x]
        height, width = frame1.shape[:2]
        center = (width / 2, height / 2)
        if HelpBar.trail_flag==1:
            HelpBar.enable_trail(Simulator.player_car,mask)
        M = cv2.getRotationMatrix2D(center, -angle, 1.0)
        #dst_points = np.float32([[100, 100], [img.shape[1]-100, 100], [img.shape[1]-100, img.shape[0]-100], [100, img.shape[0]-100]])
        rotated_img = cv2.warpAffine(frame1, M, (100, 100))
        rotated_img=cv2.resize(rotated_img,(640,480),cv2.INTER_AREA)#pylint: disable=E1101
        rotated_img=rotated_img[0:240,0:640]
        return rotated_img,mask
    
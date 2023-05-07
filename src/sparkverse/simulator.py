import os
import sparkverse.external_data as ex
from sparkverse.utils import Utils,HelpBar
import pygame
import numpy as np
import cv2
import math
import time 
PLAYER=pygame.image.load(ex.CAR)
START_POS = (180, 200)
class CAR_PROPERTIES:
    def __init__(self, max_vel, rotation_vel):
        self.img = self.IMG
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = START_POS
        self.acceleration = 0.1
       
    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel
        Utils.rotation=self.angle % 360

    def draw(self, win):
        Utils.blit_rotate_center(win, self.img, (self.x, self.y), self.angle)

    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        Utils.speed=self.vel
        self.move()

    def move_backward(self):
        self.vel = max(self.vel - self.acceleration, -self.max_vel/2)
        Utils.speed=self.vel
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        self.y -= vertical
        self.x -= horizontal

    def collide(self, mask, x=0, y=0):
        car_mask = pygame.mask.from_surface(self.img)
        offset = (int(self.x - x), int(self.y - y))
        poi = mask.overlap(car_mask, offset)
        return poi

    def reset(self):
        self.x, self.y = self.START_POS
        self.angle = 0
        self.vel = 0


class PlayerCar(CAR_PROPERTIES):
    IMG = PLAYER
    

    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()

    
def draw(win, player_car,background):
    


    win.blit(background,(0,0))
    player_car.draw(win)
    
    pygame.display.update()


def move_player(player_car):
    keys = pygame.key.get_pressed()
    moved = False
    if keys[pygame.K_q]:
        pygame.quit()
    if keys[pygame.K_h]:
        HelpBar.show=HelpBar.show^1
        time.sleep(0.5)
        #print(HelpBar.show)
    if keys[pygame.K_a]:
        player_car.rotate(left=True)
    if keys[pygame.K_d]:
        player_car.rotate(right=True)
    if keys[pygame.K_w]:
        moved = True
        player_car.move_forward()
    if keys[pygame.K_s]:
        moved = True
        player_car.move_backward()

    if not moved:
        player_car.reduce_speed()


class Simulator(Utils):
    TRACK=pygame.image.load(ex.LEVEL1)
    WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))#),pygame.NOFRAME | pygame.HIDDEN)
    TITLE=pygame.display.set_caption("Pygame SIMULATOR")
    
    isRunning = True
    clock = pygame.time.Clock()
    player_car = PlayerCar(2, 2)
    #TRACK=pygame.image.load("images/LineFollower1.png")
    Pos=[]
    START_POS = (180, 200)
    FPS=30
    def hideSimulatorWindow():
        Simulator.WIN = pygame.display.set_mode((Simulator.WIDTH, Simulator.HEIGHT),pygame.NOFRAME | pygame.HIDDEN)

    def getPos():
        return Simulator.START_POS
    def setPos(x,y):
        Simulator.START_POS[0],Simulator.START_POS[1]=x,y
    def setFPS(fps):
        Simulator.FPS=fps
    def setMap(map=ex.LEVEL1):
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

        draw(Simulator.WIN,Simulator.player_car,Simulator.TRACK)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Simulator.isRunning = False
                break
        angle=Simulator.player_car.angle
        angle=angle%360
        #print(angle)
        move_player(Simulator.player_car)
        frame = pygame.surfarray.array3d(pygame.display.get_surface())
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        frame=cv2.flip(frame,1)
        h,w=frame.shape[0],frame.shape[1]
        x,y=int(Simulator.player_car.x),int(Simulator.player_car.y)
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
        #$src_pts = np.float32([[0, 0], [frame.shape[1], 0], [frame.shape[1], frame.shape[0]], [0, frame.shape[0]]])
        #M = cv2.getPerspectiveTransform(src_pts, vertices)
    # Fill the ROI defined by the vertices with white pixels
        #rect = cv2.minAreaRect(points)

    # Draw the rectangle on a black image
        #ximg = np.zeros((512, 512, 3), np.uint8)
        try:
            cv2.line(mask,(int(bottom_left[0]),int(bottom_left[1])),(int(bottom_right[0]),int(bottom_right[1])),(255,255,255),2)
            cv2.line(mask,(int(bottom_right[0]),int(bottom_right[1])),(int(top_right[0]),int(top_right[1])),(255,255,255),2)
            cv2.line(mask,(int(top_right[0]),int(top_right[1])),(int(top_left[0]),int(top_left[1])),(255,255,255),2)
            cv2.line(mask,(int(top_left[0]),int(top_left[1])),(int(bottom_left[0]),int(bottom_left[1])),(255,255,255),2)
            cv2.circle(mask,(int(bottom_left[0]),int(bottom_left[1])),5,(0,255,0),1)
            cv2.circle(mask,(int(bottom_right[0]),int(bottom_right[1])),5,(0,0,255),1)
            cv2.circle(mask,(int(top_left[0]),int(top_left[1])),5,(255,255,0),1)
            cv2.circle(mask,(int(top_right[0]),int(top_right[1])),5,(0,255,255),1)
        except:
        # def show_game_over_message():
            font = pygame.font.Font(None, 36)
            text = font.render("Game Over", True, (255, 0, 0))
            text_rect = text.get_rect(center=(Simulator.WIDTH // 2, Simulator.HEIGHT // 2))
            Simulator.WIN.blit(text, text_rect)
            pygame.display.flip()
        center_x=int((x1+x2+x3+x4)/4)
        center_y=int(int(y1+y2+y3+y4)/4)
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
        if len(Simulator.Pos)>=100:
            Simulator.Pos.pop(0)
        else:
            if len(Simulator.Pos)>0 and (Simulator.Pos[-1][0]!=int(Simulator.player_car.x)or (Simulator.Pos[-1][0]<Simulator.player_car.x+1 and Simulator.Pos[-1][0]>Simulator.player_car.x-1)) and (Simulator.Pos[-1][1]!=int(Simulator.player_car.y)or (Simulator.Pos[-1][0]<Simulator.player_car.y+1 and Simulator.Pos[-1][0]>Simulator.player_car.y-1)):
                Simulator.Pos.append((int(Simulator.player_car.x),int(Simulator.player_car.y)))
        
            if len(Simulator.Pos)==0:
                Simulator.Pos.append((int(Simulator.player_car.x),int(Simulator.player_car.y)))
        for i in range(len(Simulator.Pos)):
            cv2.circle(mask,Simulator.Pos[i],3,(0,255,0),1)
        #print(len(Pos))
    # cv2.circle(mask,(player_car.x,player_car.y),3,(0,255,0),1,)
        M = cv2.getRotationMatrix2D(center, -angle, 1.0)
        #dst_points = np.float32([[100, 100], [img.shape[1]-100, 100], [img.shape[1]-100, img.shape[0]-100], [100, img.shape[0]-100]])
        rotated_img = cv2.warpAffine(frame1, M, (100, 100))
        rotated_img=cv2.resize(rotated_img,(640,480),cv2.INTER_AREA)
        rotated_img=rotated_img[0:240,0:640]
        return rotated_img,mask
"""info:This is a the player module for our simulator
autor: Tucudean Adrian-Ionut
date: 20.05.2023
email: Tucudean.Adrian.Ionut@outlook.com
license: MIT
"""
# pylint: disable=too-many-instance-attributes
import math
import pygame
import taisim.external_data as ex
from taisim.utils import Utils
from taisim.components.log import logger
PLAYER=Utils.scale_image(pygame.image.load(ex.CAR),0.5)
START_POS = (180, 200)
class CarProperties:
    """class for car properties"""
    def __init__(self, max_vel, rotation_vel):
        """class constructor

        Parameters:
        max_vel (float): max velocity of the car (default: 1)
        rotation_vel (float): max velocity of rotation (default: 1)
        """
        self.img = PLAYER
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x_value, self.y_value = START_POS
        self.acceleration = 0.1

        logger.info("CAR : \033[92mOK\033[0m")
    def rotate(self, left=False, right=False):
        """function to rotate the car

        Parameters:
        left (boolean): turn left if true
        right (boolean): turn right if true 
        """
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel
        Utils.rotation=self.angle % 360
    
    def draw(self, win):
        """function to draw images
        Parameters:
        win (pygameobj): imput window
        """
        Utils.blit_rotate_center(win, self.img, (self.x_value-4, self.y_value-2), self.angle)

    def move_forward(self):
        """function to translate the car forward"""
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        Utils.speed=self.vel
        self.move()
    def bounce_back(self):
        """function to bounce the car back"""
        self.vel = min(self.vel - self.acceleration*4, self.max_vel/2)
        Utils.speed=self.vel
        self.move()

    def bounce(self):
        """function to bounce the car in the oposite direction"""
        self.angle=abs(180-self.angle)
    def bounce_forward(self):
        """function to bounce the car forward"""
        self.vel = min(self.vel + self.acceleration*4, self.max_vel)
        Utils.speed=self.vel
        self.move()
    def move_backward(self):
        """function to translate the car forward"""
        self.vel = max(self.vel - self.acceleration, -self.max_vel/2)
        Utils.speed=self.vel
        self.move()

    def move(self):
        """function to move and rotate the car"""
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        self.y_value -= vertical
        self.x_value -= horizontal

    def collide(self, mask, xpos=0, ypos=0):
        """colide method"""
        car_mask = pygame.mask.from_surface(self.img)
        offset = (int(self.x_value - xpos), int(self.y_value - ypos))
        poi = mask.overlap(car_mask, offset)
        return poi

    def reset(self):
        """reset method"""
        self.x_value, self.y_value = START_POS
        self.angle = 0
        self.vel = 0
class PlayerCar(CarProperties):
    """Player car class"""
    IMG = PLAYER
    #@classmethod
    def reduce_speed(self):
        """function to reduce speed"""
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()
    def control(self,speed,rotation_vel):
        """simpler"""
        self.angle+=rotation_vel
        if speed==0:
            self.vel=0
        self.vel = min(self.vel + speed, self.max_vel)
        Utils.speed=self.vel
        Utils.rotation=self.angle%360
        self.move()
def draw(win, player_car,background):
    """function to draw character and background"""
    win.blit(background,(0,0))
    player_car.draw(win)
    pygame.display.update()

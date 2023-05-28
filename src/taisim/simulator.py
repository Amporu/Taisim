"""
info:This module contains the implememntation of the SparkVerse Simulator
autor: Tucudean Adrian-Ionut
date: 17.05.2023
email: Tucudean.Adrian.Ionut@outlook.com
license: MIT
"""
import pygame
import taisim.external_data as ex
import taisim.player as pl
from taisim.utils import Utils
from taisim.components.log import logger

#pylint: disable=E1101
class Simulator(Utils):
    """simulator class"""
    logger.info("TRACK PRESET : \033[92mLEVEL1\033[0m")
    TRACK=pygame.image.load(ex.LEVEL1)
    WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))#),pygame.NOFRAME | pygame.HIDDEN)
    pygame.event.set_grab(True)
    TITLE=pygame.display.set_caption("Pygame SIMULATOR")

    isRunning = True
    clock = pygame.time.Clock()
    player_car = pl.PlayerCar(2, 2)
    FPS=30

    @staticmethod
    def data():
        """function that returns simulator variables"""
        return (Simulator.WIN,
                Simulator.player_car,
                Simulator.clock,
                Simulator.isRunning,
                Simulator.FPS,
                Simulator.TRACK)

    @staticmethod
    def hide_simulator_window():
        """this function hids the pygame simulator window"""
        logger.info("SIMULATOR WINDOW SET : \033[92mHIDDEN\033[0m")
        Simulator.WIN = pygame.display.set_mode((Simulator.WIDTH,
                                                 Simulator.HEIGHT),
                                                 pygame.NOFRAME | pygame.HIDDEN)
    @staticmethod
    def setfps(fps):
        """set simulator fps"""
        Simulator.FPS=fps
    @staticmethod
    def track(track_image=ex.LEVEL1):
        """set the track """
        if track_image==1:
            logger.info("TRACK SET : \033[92mLEVEL1\033[0m")
            Simulator.TRACK=pygame.image.load(ex.LEVEL1)
        elif track_image==2:
            logger.info("TRACK SET : \033[92mLEVEL2\033[0m")
            Simulator.TRACK=pygame.image.load(ex.LEVEL2)#
        elif track_image==3:
            logger.info("TRACK SET : \033[92mLEVEL3\033[0m")
            Simulator.TRACK=pygame.image.load(ex.LEVEL3)
        elif track_image==4:
            logger.info("TRACK SET : \033[92mLEVEL4\033[0m")
            Simulator.TRACK=pygame.image.load(ex.LEVEL4)
        elif track_image==5:
            logger.info("TRACK SET : \033[92mLEVEL5\033[0m")
            Simulator.TRACK=pygame.image.load(ex.LEVEL5)
        elif track_image==6:
            logger.info("TRACK SET: \033[92mLEVEL6\033[0m")
            Simulator.TRACK=pygame.image.load(ex.LEVEL6)
        elif track_image==7:
            logger.info("TRACK SET : \033[92mLEVEL7\033[0m")
            Simulator.TRACK=pygame.image.load(ex.LEVEL7)
        else:
            logger.info("TRACK SET : \033[92m%s\033[0m",track_image)
            Simulator.TRACK=pygame.image.load(track_image)
    @staticmethod
    def start():
        """initalization of the simulator"""
        Simulator.track(ex.LEVEL1)

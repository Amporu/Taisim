"""
info:This is a simple example on starting the simulator
autor: Tucudean Adrian-Ionut
date: 19.05.2023
email: Tucudean.Adrian.Ionut@outlook.com
license: MIT
"""

from taisim.simulator import Simulator
from taisim.sensor import Camera,Lidar,Compass,Gps
import taisim.external_data as ex

Simulator.hide_simulator_window()  #hide pygame window if you want
Simulator.track(ex.LEVEL1)   #select maps ranging from LEVEL1 to LEVEL 7 or input path
CAM=Camera("Front camera",0)

LIDAR=Lidar("Lidar",0,50)
COMPASS=Compass("compass")
GPS=Gps("GPS")
while Simulator.isRunning :
    frame=CAM.read() #extract camera frame
    distance,angles=LIDAR.read() #extract lidar measurement
    angle=COMPASS.read()
    x,y=GPS.read()
    """ your code here"""
    Simulator.display() #display everything

"""
info:This is a simple example on starting the simulator
autor: Tucudean Adrian-Ionut
date: 19.05.2023
email: Tucudean.Adrian.Ionut@outlook.com
license: MIT
"""

from sparkverse.simulator import Simulator
from sparkverse.sensor import Camera,Lidar
import sparkverse.external_data as ex

Simulator.hide_simulator_window()  #hide pygame window if you want
Simulator.track(ex.LEVEL1)   #select maps ranging from LEVEL1 to LEVEL 7 or input path
CAM=Camera("Front camera",0)
CAM1=Camera("LEFT",90)
LIDAR=Lidar("Lidar",0,50)

while Simulator.isRunning :
    frame=CAM.read() #extract camera frame
    frame1=CAM1.read()
    DISTANCE,ANGLES=LIDAR.read() #extract lidar measurement
    """ your code here"""
    Simulator.display() #display everything

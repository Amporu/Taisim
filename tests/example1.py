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
CAM=Camera(title="Front camera",angle=0)
LIDAR=Lidar(title="Lidar",angle=0,angular_resolution=100)
COMPASS=Compass(title="compass")
GPS=Gps(title="GPS")
while Simulator.isRunning :
    frame=CAM.read() #extract camera frame
    distance,angles=LIDAR.read() #extract lidar measurement
    angle=COMPASS.read() #extract compass measurement
    x,y=GPS.read()  #extract gps measurement
    
    """ your code here"""
    Simulator.display() #display control panel
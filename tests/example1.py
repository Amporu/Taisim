"""
info:This is a simple example on starting the simulator
autor: Tucudean Adrian-Ionut
date: 19.05.2023
email: Tucudean.Adrian.Ionut@outlook.com
license: MIT
"""
#pylint disable E0401
#pylint disableE0611
from sparkverse.simulator import Simulator
from sparkverse.sensor import Camera,Lidar
import sparkverse.external_data as ex
Simulator.hide_simulator_window()  #hide pygame window if you want
Simulator.track(ex.LEVEL1)   #select maps ranging from LEVEL1 to LEVEL 7 
                             #or just imput path to your png file
CAM=Camera(simulator=Simulator.data,angle=0)  #camera object initialized
#CAM1=Camera(simulator=Simulator.data,angle=0)
LIDAR=Lidar(simulator=Simulator.data,angle=0,angular_resolution=50)


while Simulator.isRunning :
    frame=CAM.read() #extract camera 
    #frame1=CAM1.read() #extract seccond camera
    lidar1=LIDAR.read() #extract lidar measurement
    """ your code here"""
    Simulator.display() #display everything

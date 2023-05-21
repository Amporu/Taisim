"""
info:This is a simple example on starting the simulator
autor: Tucudean Adrian-Ionut
date: 19.05.2023
email: Tucudean.Adrian.Ionut@outlook.com
license: MIT
"""
import cv2
from sparkverse.simulator import Simulator
from sparkverse.sensor import Camera,Lidar
Simulator.hide_simulator_window()
cam=Camera(Simulator.data,90)
cam1=Camera(Simulator.data,0)
lidar=Lidar(Simulator.data,0,30)
#cam2=Camera(Simulator.data,270)
while Simulator.isRunning :
    frame=cam.read() #extract camera and map
    frame1=cam1.read()
    lidar1=lidar.read()
    #print(frame1.shape)
    #frame2=cam2.read()
    #cv2.imshow("frame1",frame1)
    #cv2.imshow("frame",frame)
    Simulator.display()

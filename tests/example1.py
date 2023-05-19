"""
info:This is a simple example on starting the simulator
autor: Tucudean Adrian-Ionut
date: 19.05.2023
email: Tucudean.Adrian.Ionut@outlook.com
license: MIT
"""
#pylint: disable-all
import cv2
from sparkverse.simulator import Simulator,Camera
#from sparkverse.sensor import Camera
Simulator.hide_simulator_window()
cam=Camera(Simulator.data,0)

while cam.flag :
    frame=cam.read() #extract camera and map
    """code here"""
    cv2.imshow("Simulator".frame)
    #concatenated=cv2.vconcat([frame,track]) #attach the map and camera frame
    #Simulator.display(concatenated)

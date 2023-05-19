from sparkverse.simulator import Simulator
import cv2

#Simulator.setMap(1) #set the desired map LEVEL1 to LEVEL7 or input path to image file

while(Simulator.isRunning):
  frame,map=Simulator.getCamera() #extract camera and map
  """code here"""
  concatenated=cv2.vconcat([frame,map]) #attach the map and camera frame
  Simulator.display(concatenated)
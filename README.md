<p align="center">
<a href="https://www.linkedin.com/in/adrian-ionu%C8%9B-%C8%9Bucudean-37aa59244">
    <img src="https://img.shields.io/badge/-LinkedIn-blue">
</a>
<a href="https://www.reddit.com/r/TAISIM/">
    <img src="https://img.shields.io/badge/-Reddit-red">
</a>
<a href="mailto:Tucudean.Adrian.Ionut@outlook.com">
    <img src="https://img.shields.io/badge/-Email-darkgreen?style=flat-square&logo=#0078D4&logoColor=black">
</a>

<a href="[https://pypi.org/user/TucuAI/](https://static.pepy.tech/personalized-badge/taisim?period=total&units=abbreviation&left_color=black&right_color=orange&left_text=Downloads)">
    <img src="https://img.shields.io/badge/PyPi-TucuAI-blueviolet">
</a>

<br/> 



</p>

![base_logo_transparent_background](/src/taisim/data/taisim.png)

TAISIM is a Python-based simulator designed for testing and developing computer vision applications. With a primary focus on autonomous driving systems that rely on virtual sensor inputs, it provides a versatile platform for a variety of tasks, from lane keeping to complex navigation in agricultural environments.

## Latest Release

<p align="center">
    
[![Downloads](http://pepy.tech/badge/taisim)](http://pepy.tech/project/taisim)
<a href="https://github.com/Amporu/Taisim/releases">
    <img src="https://img.shields.io/badge/-0.1.0-important">
 
<br/> 
    
</p>
    
## Dependencies
  * OpenCV
  * Pygame

## Key Features

### Virtual Sensors and Map Interface: 
  Tucu provides a simple interface to camera and map data, allowing you to easily integrate it with your computer vision algorithms.
  * Virtual Cameras
  * Virtual Lidars
  * Virtual Ultrasonic sensors
  * Virtual Infrared sensors
### Custom Map Imports: 
In addition to default maps, SparkVerse allows for the import of custom maps. This flexibility facilitates testing across diverse environments and scenarios.
```python
Simulator.track("path_to_your_image.png")
```
### Optimized & CrossPlatform: 
Efficient performance on single-core computers makes mir4u accessible to a wide range of users and potentially suitable for real-time applications or embedded systems.
Soo far was tested on:

[![Linux](https://img.shields.io/badge/linux-black?style=for-the-badge&logo=Linux)](https://github.com/Amporu)
    
[![Windows](https://img.shields.io/badge/Windows-black?style=for-the-badge&logo=Windows)](https://github.com/Amporu)
    
[![MacOS](https://img.shields.io/badge/MacOS-black?style=for-the-badge&logo=MacOS)](https://github.com/Amporu)

## Installation
To install via `pip` use:
```sh
pip install taisim #Python2.x
pip3 install taisim #Python3.x
```
## Basic Usage
The usage of the package is very easy. It does not require any initialisation. Just import and start coding:
```python
from taisim.simulator import Simulator
from taisim.sensor import Camera,Lidar,Compass,Gps
import taisim.external_data as ex

#Simulator.hide_simulator_window()  #hide pygame window if you want
Simulator.track(ex.LEVEL1)   #select maps ranging from LEVEL1 to LEVEL 7 or input path
CAM=Camera(title="Front camera",angle=0).  #initialize virtual camera
LIDAR=Lidar(title="Lidar",angle=0,angular_resolution=100) #initialize virtual lidar
COMPASS=Compass(title="compass") #initialize virtual compass
GPS=Gps(title="GPS").  #initialize virtual GPS
while Simulator.isRunning :
    frame=CAM.read() #extract camera frame
    distance,angles=LIDAR.read() #extract lidar measurement
    angle=COMPASS.read() #extract compass measurement
    x,y=GPS.read()  #extract gps measurement
    ## movement
    Simulator.control(linear_vel=1,angular_vel=5)
    # liniar_vel and angular_Vel between [-5;5] 
    # linear_vel logic: 0=stop , more=forward , less=backward 
    # angular_vel logic: 0= forward , more=left, less=right
    
    """ your code here"""
    Simulator.display() #display control panel
```



![base_logo_transparent_background](/assets/Untitled%20Project.gif)

## Simulator Examples
TAISIM is suitable for a range of computer vision applications, including but not limited to:

   * Lane Keeping: 
     Test and develop algorithms for keeping a vehicle within the boundaries of a lane.
   * Line Following:
     Test and develop the simplest algorithm for following a line.
   * Maze Running: 
     Develop and evaluate navigation algorithms capable of finding a path through complex environments.
   * Agricultural Crop Following: 
   Ideal for tasks like crop identification, health monitoring, or autonomous navigation between crop rows.


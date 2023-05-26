<p align="center">
<a href="https://www.linkedin.com/in/adrian-ionu%C8%9B-%C8%9Bucudean-37aa59244">
    <img src="https://img.shields.io/badge/-LinkedIn-blue">
</a>
<a href="mailto:Tucudean.Adrian.Ionut@outlook.com">
    <img src="https://img.shields.io/badge/-Email-darkgreen?style=flat-square&logo=#0078D4&logoColor=black">
</a>

<a href="[https://pypi.org/user/TucuAI/](https://static.pepy.tech/personalized-badge/sparkverse?period=total&units=abbreviation&left_color=black&right_color=orange&left_text=Downloads)">
    <img src="https://img.shields.io/badge/PyPi-TucuAI-blueviolet">
</a>

<br/> 



</p>

![base_logo_transparent_background](/assets/customcolor_icon_transparent_background.png)

Mirau is a Python-based simulator designed for testing and developing computer vision applications. With a primary focus on autonomous driving systems that rely on virtual sensor inputs, it provides a versatile platform for a variety of tasks, from lane keeping to complex navigation in agricultural environments.

## Latest Release

<p align="center">
    
[![Downloads](http://pepy.tech/badge/sparkverse)](http://pepy.tech/project/sparkverse)
    
<a href="https://github.com/Amporu/SparkVerse/releases">
    <img src="https://img.shields.io/badge/0%20.%200-.%203-blueviolet">
 
<br/> 
    
</p>
    
## Dependencies
  * OpenCV
  * Pygame

## Key Features

### Virtual Sensors and Map Interface: 
  SparkVerse provides a simple interface to camera and map data, allowing you to easily integrate it with your computer vision algorithms.
  * Virtual Cameras
  * Lidars
  * Ultrasonic sensors
  * Infrared sensors
### Custom Map Imports: 
In addition to default maps, SparkVerse allows for the import of custom maps. This flexibility facilitates testing across diverse environments and scenarios.
```python
Simulator.track("path_to_your_image.png")
```
### Optimized & CrossPlatform: 
Efficient performance on single-core computers makes SparkVerse accessible to a wide range of users and potentially suitable for real-time applications or embedded systems.
Soo far was tested on:

[![Linux](https://img.shields.io/badge/linux-black?style=for-the-badge&logo=Linux)](https://github.com/Amporu)
    
[![Windows](https://img.shields.io/badge/Windows-black?style=for-the-badge&logo=Windows)](https://github.com/Amporu)
    
[![MacOS](https://img.shields.io/badge/MacOS-black?style=for-the-badge&logo=MacOS)](https://github.com/Amporu)

## Installation
To install via `pip` use:
```sh
pip install sparkverse #Python2.x
pip3 install sparkverse #Python3.x
```
## Basic Usage
The usage of the package is very easy. It does not require any initialisation. Just import and start coding:
```python
from sparkverse.simulator import Simulator
from sparkverse.sensor import Camera,Lidar
import sparkverse.external_data as ex

#Simulator.hide_simulator_window()  #hide pygame window if you want (works only on Linux and MacOS
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
```



![base_logo_transparent_background](/assets/demo.gif)

## Simulator Examples
Mirau is suitable for a range of computer vision applications, including but not limited to:

   * Lane Keeping: 
     Test and develop algorithms for keeping a vehicle within the boundaries of a lane.
   * Line Following:
     Test and develop the simplest algorithm for following a line.
   * Maze Running: 
     Develop and evaluate navigation algorithms capable of finding a path through complex environments.
   * Agricultural Crop Following: 
   Ideal for tasks like crop identification, health monitoring, or autonomous navigation between crop rows.

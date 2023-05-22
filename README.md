<p align="center">
<a href="https://www.linkedin.com/in/adrian-ionu%C8%9B-%C8%9Bucudean-37aa59244">
    <img src="https://img.shields.io/badge/-LinkedIn-blue">
</a>
<a href="mailto:Tucudean.Adrian.Ionut@outlook.com">
    <img src="https://img.shields.io/badge/-Email-darkgreen?style=flat-square&logo=#0078D4&logoColor=black">
</a>

<a href="https://pypi.org/user/TucuAI/">
    <img src="https://img.shields.io/badge/PyPi-TucuAI-blueviolet">
</a>

<br/> 



</p>

![base_logo_transparent_background](https://github.com/Amporu/SparkVerse/assets/109149566/ae904844-298e-433e-bbcf-b5c0032cd01f)

SparkVerse is a Python-based simulator designed for testing and developing computer vision applications. With a primary focus on autonomous driving systems that rely on virtual sensor inputs, it provides a versatile platform for a variety of tasks, from lane keeping to complex navigation in agricultural environments.

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
CAM=Camera(simulator=Simulator.data,angle=90)  #camera object initialized
CAM1=Camera(simulator=Simulator.data,angle=0)
LIDAR=Lidar(simulator=Simulator.data,angle=0,angular_resolution=50)


while Simulator.isRunning :
    frame=CAM.read() #extract camera 
    frame1=CAM1.read() #extract seccond camera
    lidar1=LIDAR.read() #extract lidar measurement
    """ your code here"""
    Simulator.display() #display everything
```



![base_logo_transparent_background](/assets/demo.gif)

## Simulator Examples
SparkVerse is suitable for a range of computer vision applications, including but not limited to:

   * Lane Keeping: 
     Test and develop algorithms for keeping a vehicle within the boundaries of a lane.
   * Line Following:
     Test and develop the simplest algorithm for following a line.
   * Maze Running: 
     Develop and evaluate navigation algorithms capable of finding a path through complex environments.
   * Agricultural Crop Following: 
   Ideal for tasks like crop identification, health monitoring, or autonomous navigation between crop rows.

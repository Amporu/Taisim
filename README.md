# Simple Python Simulator for Autonomous Driving Systems based on camera

SparkVerse is a Python-based simulator designed for testing and developing computer vision applications. With a primary focus on autonomous driving systems that rely on virtual sensor inputs, it provides a versatile platform for a variety of tasks, from lane keeping to complex navigation in agricultural environments.

## Latest Release
[0.0.1](https://github.com/Amporu/SparkVerse/releases)


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
Simulator.initMap("path_to_your_image.png")
```
### Optimized & CrossPlatform: 
Efficient performance on single-core computers makes SparkVerse accessible to a wide range of users and potentially suitable for real-time applications or embedded systems.
Soo far was tested on:
  * Linux 
  * Windows 10&11
  * MacOS

## Installation
To install via `pip` use:
```sh
pip install sparkverse #Python2.x
pip3 install sparkverse #Python3.x
```
## Basic Usage
The usage of the package is very easy. It does not require any initialisation. Just import and start coding:
```python
import cv2
from sparkverse.simulator import Simulator
from sparkverse.sensor import Camera,Lidar
Simulator.hide_simulator_window()
Simulator.track(1) # add your "image_path.png" or use our default maps from 1 to 7
cam=Camera(Simulator.data,90)
lidar=Lidar(Simulator.data,0,30)
while Simulator.isRunning :
    frame=cam.read() #extract camera and map
    frame1=cam1.read()
    lidar1=lidar.read()
    Simulator.display()
```
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

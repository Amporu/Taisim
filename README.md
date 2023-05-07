# SpaceX API wrapper in Python
<div align="center">

[![GitHub release](https://img.shields.io/github/release/phadnisvinay30/SpaceX-Python.svg)](https://github.com/phadnisvinay30/SpaceX-Python/releases)
[![GitHub issues](https://img.shields.io/github/issues/phadnisvinay30/SpaceX-Python.svg)](https://github.com/phadnisvinay30/SpaceX-Python/issues)
[![GitHub stars](https://img.shields.io/github/stars/phadnisvinay30/SpaceX-Python.svg)](https://github.com/phadnisvinay30/SpaceX-Python/stargazers)
[![GitHub license](https://img.shields.io/github/license/phadnisvinay30/SpaceX-Python.svg)](https://github.com/phadnisvinay30/SpaceX-Python)

### Simple and Easy API Wrapper for [r-spacex/SpaceX-API](https://github.com/r-spacex/SpaceX-API)!

<br><br>

</div>

## Documentation
This is a python simulator that is best use for autonomous driving systems based on a camera module.
<br>
See the [Wiki](https://github.com/phadnisvinay30/SpaceX-Python/wiki) for full wrapper documentation.

## Installation
To install via `pip` use:
```sh
pip install sparkverse #Python2.x
```

## Basic Usage
The usage of the wrapper is very easy. It does not require any initialisation. Just import and start coding:
```python
from sparkverse.simulator import Simulator
import sparkverse.external_data as ex #contains all maps preinstalled alltoghether with the library

import cv2
Simulator.setMap(ex.LEVEL1) #set the desired map LEVEL1 to LEVEL7 or input path to image file
while(Simulator.isRunning):
  frame,map=Simulator.getCamera() #extract camera and map
  """code here"""
  concatenated=cv2.vconcat([frame,map]) #attach the map and camera frame
  Simulator.Display(concatenated)      #special display with keyboard input for easy user experience
```

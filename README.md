# Simple Python Simulator for Autonomous Driving Systems based on camera

## Latest Release
[0.0.1](https://github.com/Amporu/SparkVerse/releases)




## Documentation
Currently the package has a pydoc addaptation.
<br>


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
import cv2
while(Simulator.isRunning):
  frame,map=Simulator.getCamera() #extract camera and map
  """code here"""
  concatenated=cv2.vconcat([frame,map]) #attach the map and camera frame
  Simulator.Display(concatenated)      #special display with keyboard input for easy user experience
```

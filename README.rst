.. raw:: html

   <p align="center">

.. raw:: html

   </p>

.. figure:: /assets/customcolor_icon_transparent_background.png
   :alt: base_logo_transparent_background

   base_logo_transparent_background

Tucu is a Python-based simulator designed for testing and developing
computer vision applications. With a primary focus on autonomous driving
systems that rely on virtual sensor inputs, it provides a versatile
platform for a variety of tasks, from lane keeping to complex navigation
in agricultural environments.

Latest Release
--------------

.. raw:: html

   <p align="center">

|Downloads|

.. raw:: html

   </p>

Dependencies
------------

-  OpenCV
-  Pygame

Key Features
------------

Virtual Sensors and Map Interface:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tucu provides a simple interface to camera and map data, allowing you to
easily integrate it with your computer vision algorithms. \* Virtual
Cameras \* Lidars \* Ultrasonic sensors \* Infrared sensors ### Custom
Map Imports: In addition to default maps, SparkVerse allows for the
import of custom maps. This flexibility facilitates testing across
diverse environments and scenarios.

.. code:: python

   Simulator.track("path_to_your_image.png")

Optimized & CrossPlatform:
~~~~~~~~~~~~~~~~~~~~~~~~~~

Efficient performance on single-core computers makes mir4u accessible to
a wide range of users and potentially suitable for real-time
applications or embedded systems. Soo far was tested on:

|Linux|

|Windows|

|MacOS|

Installation
------------

To install via ``pip`` use:

.. code:: sh

   pip install tucu #Python2.x
   pip3 install tucu #Python3.x

Basic Usage
-----------

The usage of the package is very easy. It does not require any
initialisation. Just import and start coding:

.. code:: python

   from tucu.simulator import Simulator
   from tucu.sensor import Camera,Lidar
   import tucu.external_data as ex

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

.. figure:: /assets/demo.gif
   :alt: base_logo_transparent_background

   base_logo_transparent_background

Simulator Examples
------------------

mir4u is suitable for a range of computer vision applications, including
but not limited to:

-  Lane Keeping: Test and develop algorithms for keeping a vehicle
   within the boundaries of a lane.
-  Line Following: Test and develop the simplest algorithm for following
   a line.
-  Maze Running: Develop and evaluate navigation algorithms capable of
   finding a path through complex environments.
-  Agricultural Crop Following: Ideal for tasks like crop
   identification, health monitoring, or autonomous navigation between
   crop rows.

.. |Downloads| image:: http://pepy.tech/badge/sparkverse
   :target: http://pepy.tech/project/sparkverse
.. |Linux| image:: https://img.shields.io/badge/linux-black?style=for-the-badge&logo=Linux
   :target: https://github.com/Amporu
.. |Windows| image:: https://img.shields.io/badge/Windows-black?style=for-the-badge&logo=Windows
   :target: https://github.com/Amporu
.. |MacOS| image:: https://img.shields.io/badge/MacOS-black?style=for-the-badge&logo=MacOS
   :target: https://github.com/Amporu

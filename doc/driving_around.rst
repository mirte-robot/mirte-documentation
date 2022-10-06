Driving around
##############

.. warning::

   Currently the robot is controllable via multiple interfaces. At the moment
   this does assume you have two motors called 'left' and 'right'. Please
   make sure that your :ref:`settings are correct <Configure Settings to match Hardware>`.



From web interface
==================

The robot can be controller from the web interface by goin to the 'control' tab:

      .. image:: images/driving_around.png
        :width: 600
        :alt: Driving around from the web interface

Teleop Key
==========

In ROS you can also drive around with your keyboard:

.. code-block:: bash

    mirte$ roslaunch mirte_teleop teleopkey.launch


With a PS3/4 Controller
=======================

Make sure you have paired to PS controller to a USB Bluetooth dongle (see :ref:`Supported Hardware <PS3/4 Controller>`).

If all works fine, one can start the ROS launchfile:

.. code-block:: bash

    mirte$ roslaunch mirte_teleop teleop_joy.launch


Android
=======

There is also an Android app which allows you to control Mirte (or any ROS-based robot). You can
download `ROS-mobile here <https://play.google.com/store/apps/details?id=com.schneewittchen.rosandroid>`_. 
In order to drive around you need to connect to the robot:

- Master URL: <your robot ip>
- Master port: 11311
- Wi-Fi: <connect to the same network as the robot>

In the details tab you still need to add the Joystick widget and set the topic name:

- Topic Name: /mobile_base_controller/cmd_vel

You can now drive around in the 'viz' tab. When a USB camera is attached you can also
view the image stream. You nees to add a Camera widget in teh details tab and set the
topic name:

- Topic Name: /webcam/image_raw/compressed

Driving around
##############

.. warning::

   Currently the robot is controllable via multiple interfaces. At the moment
   this does assume you have two motors called 'left' and 'right'. Please
   make sure that your :ref:`settings are correct <Configure Software to match Hardware>`.





From web interface
==================



Teleop Key
==========

.. code-block:: bash

    mirte$ roslaunch mirte_teleop teleop_key.launch


PS3/4 Controller
================


.. code-block:: bash

    mirte$ sudo bluetoothctl
    [bluetooth]# agent on
    [bluetooth]# default-agent 
    [bluetooth]# scan on


Connect the PS3 via a USB cable to the SBC (on the Orange Pi Zero one might need the expansion board in order
to have more USB ports). Press the connect button (PS logo) on the controller. In the terminal one will see
the device being found. Type "yes" to confirm and exit the bluetoothctl.

To test the controller one can:

.. code-block:: bash

    mirte$ sudo jstest /dev/input/js0

If all works fine, one can start the ROS launchfile:

.. code-block:: bash

    mirte$ roslaunch mirte_teleop teleopjoy.launch


Android
=======

There is also an Android app which allows you to control Mirte (or any ROS-based robot).




https://play.google.com/store/apps/details?id=com.schneewittchen.rosandroid


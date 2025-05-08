Driving around
##############

.. warning::

   Currently the robot is controllable via multiple interfaces. At the moment
   this does assume you have two motors called 'left' and 'right'. Please
   make sure that your :ref:`settings are correct <DC Motor>`.



From web interface
==================

The robot can be controller from the web interface by goin to the 'control' tab:

      .. _image:: images/driving_around.png
        :width: 600
        :alt: Driving around from the web interface

Teleop Key
==========

In ROS you can also drive around with your keyboard:

.. code-block:: bash

    mirte$ ros2 launch mirte_teleop teleop_key.launch.py

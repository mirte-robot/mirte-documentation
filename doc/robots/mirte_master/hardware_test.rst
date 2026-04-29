Hardware tests
##############

Before we can actually test the robot, we need to install the software. 
You can follow the instructions from here and either install the MIRTE-OS
on the EMMC, or run it from SD card.

Please note that at the moment you will need to get some development image
located at: https://github.com/ArendJan/mirte-sd-image-tools/actions/runs/24549626442

This also holds for the uf2 for the Pico. Please upload this one:
https://github.com/ArendJan/Telemetrix4RpiPico/releases/tag/rolling

Please note that currently these images are using the development MIRTE ROS 
packages from: https://github.com/ArendJan/mirte-ros-packages/tree/develop

After booting you can login to the robot, and run the following test:

``$ ros2 run mirte_test mirte_master_hw_test``

Please note that you need to make sure the distance sensor gets some data (e.g.
moving your hand in front of the sensor)

.. warning::

   Sometimes the timing of some of the sensordata (e.g. lidar and/or camera) is 
   off which currently will fail the test. In that case you can check if you
   get data on the missing topics.
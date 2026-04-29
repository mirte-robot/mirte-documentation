Preparations
############

Before you can assemble the robot it makes sense to prepare some parts.


Soldering
---------

There are two parts that need to be soldered. 1) The 5V step down needs to be
soldered on the MIRTE PCB as can be seen below. And 2) the spring contact to the
wire.

Servo settings
--------------

Before assembling the arm, please make sure that the servo's have the correct ID,
and are positioned in their 0 state. In order to do so, we have created a script 
that does this for each servo.

Each servo needs to be set seperately (so the servos can not be connected/daisy chained
with eachother). For this setup you should upload the right uf2 to the Raspberry Pi Pico,
You should now add the switch and the battery mount to the MIRTE PCB as on the 
picture below.

.. list-table::
   :header-rows: 1

   * - Servo
     - Type
     - ID
     - uf2
   * - Rotation
     - HX-12H
     - 2
     - `set_servo2.uf2 <https://github.com/ArendJan/mirte_set_serial_servos/releases/download/v1/set_servos2.uf2>`_
   * - Shoulder
     - HTD-45H
     - 3
     - `set_servo3.uf2 <https://github.com/ArendJan/mirte_set_serial_servos/releases/download/v1/set_servos3.uf2>`_
   * - Elbow
     - HTD-35H
     - 4
     - `set_servo4.uf2 <https://github.com/ArendJan/mirte_set_serial_servos/releases/download/v1/set_servos4.uf2>`_
   * - Wrist
     - HX-12H
     - 5
     - `set_servo5.uf2 <https://github.com/ArendJan/mirte_set_serial_servos/releases/download/v1/set_servos5.uf2>`_
   * - Gripper
     - HX-12H
     - 6
     - `set_servo6.uf2 <https://github.com/ArendJan/mirte_set_serial_servos/releases/download/v1/set_servos6.uf2>`_

The steps you need to take for each servo are:

1) Upload the right uf2 to the Pico
2) Connect the servo to the PCB
3) Turn on the PCB by pressing the switch
4) Check if you saw the servo moving and/or validate by connecting the Pico to a (linux) pc 
   and read from serial: ``$ tio -b 115200 /dev/ttyACM0``

.. tip::

   When assembling multiple MIRTE Masters at once it makes sense to set all the servos 
   with the same ID. 
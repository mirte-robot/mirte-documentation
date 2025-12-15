Building a custom MIRTE
#######################

Apart from using one of our own MIRTE designs, you can of course also just
build your own robot or use MIRTE OS on an existing robot. In this
tutorial we will explain how to get started. Like with the robots from
the MIRTE family, you have to go through 4 steps:

1) Design and build the frame
2) Connect the electronics
3) Install the software
4) Configure the software


Design and build the frame
==========================

Designing a robot might be challenging. It is good to know the limitations 
of the MIRTE software so you can take that into account in your design.

Low level hardware
------------------
For the lower level hardware you can take a look at the :ref:`supported hardware
section <supported-hardware>` for the microcontroller peripherals. This includes 
DC motors (or actually different types of motor controllers). With that you 
should be able to control all types of DC motors through a motorcontroller.
Please take a look at the other peripheras (like servo's, and sensors) to 
see the limitations of each of them.

All these peripherals are communicating through our own implementation
of Telemetrix. Technically it is possible to add other peripherals. This
does involve implementing this on both the server- and client-side of 
Telemetrix.


Higher level hardware
---------------------

Depending on your application you can of course also include (depth) camera's
or 2D lidars though USB. Since the MIRTE stack runs on ROS, it is highly
advised to check if your hardware is supported by ROS. This makes integration
way easier.


Compute power
-------------

SBC
+++

The MIRTE OS is based on the Ubuntu flavor of `Armbian <https://armbian.com>`_. 
The easiest way to get MIRTE OS to work is using one of the supported SBCs:

- Orange Pi Zero 2
- Orange Pi 3b 
- Raspberry Pi 4/5

The closer you stay to this, the easier it will get.

+------------------------------------------------------------------------------------------+-----------------------+
| `Supported SBCs <https://github.com/mirte-robot/mirte-sd-image-tools/releases/latest>`_  | Easy                  |
+------------------------------------------------------------------------------------------+-----------------------+
| `Armbian supported SBCs <https://www.armbian.com/download/>`_                            | Moderately easy       |
+------------------------------------------------------------------------------------------+-----------------------+
| `Ubuntu machines <https://ubuntu.com/certified>`_                                        | Possible              |
+------------------------------------------------------------------------------------------+-----------------------+
| `Other ubuntu-like machines <https://distrowatch.com/search.php?basedon=Ubuntu>`_        | Hard                  |
+------------------------------------------------------------------------------------------+-----------------------+
| `Non-ubuntu Linux machines <https://distrowatch.com/>`_                                  | Really hard/imossible |
+------------------------------------------------------------------------------------------+-----------------------+
| Non-linux machines                                                                       | Impossible            |
+------------------------------------------------------------------------------------------+-----------------------+


MCU
+++

The MIRTE software stack is running Telemetrix to communicate to the lower
lever hardware. The default setup is using the Raspberry Pi Pico as MCU. 

We also support Arduino-based MCU's. So as long as your MCU supports the
Arduino SDK, it should be able to run our version of Telemetrix. You might
run into some issues though, due to possible limitations of the MCU.


Robot types
-----------

The design choices you make fully depend on your requirements. It might be
that you just want to slightly modify our design. But you can also design
a fully new type of robot.

Modified MIRTE robot
++++++++++++++++++++

The easiest way to get started is to (slightly) modify the base of one of 
the MIRTE robots. This can be useful if you just want to modify the location
of a sensor, want to use different motors, or want to use a different 
battery. 

**MIRTE Pioneer**: We used FreeCAD to create the MIRTE Pioneer so everyone
will be able to modify the original files. The files can be found
in the `mirte-frame <https://github.com/mirte-robot/mirte-frame>`_ 
repository.

**MIRTE Master**: We used Solidworks to create the MIRTE Master since this
is mostly used in a professional setting. But STEP files are also generated
to be used in other CAD-programs. You can find the files in the 
`mirte-master-frame <https://github.com/mirte-robot/mirte-master-frame>`_
repository.


Custom robot
++++++++++++

But of course you can also fully design an new MIRTE robot. For example an
outdoor, a boat, or a walking robot. By default you are able to use the ROS 
(and where available Python and Blockly) interfaces of each hardware peripheral. 
To also use the higher level capabilitiesof ROS (like Nav2 and/or MoveIt!) you 
should also create a URDF of your robot. 

It is good to know that the closer you stay to a differential or meccanum drive
mobile robot, the easier it is. Other drives (like Ackermann) can also be used
using ros2_controlm but still need some manual changes. The same thing holds
for the articulated arm.


Connect the electronics
=======================

Connecting all the hardware might be challenging, but is of course also part
of building your own robot. How to connect the cables, highly depends on the 
chose setup of your hardware peripherals. For reference you can have a look
at an :ref:`example setup <pico-wiring>`.

Your design can be a simple breadboard, a PCB (for example the MIRTE PCB), or
your own PCB design. You can also decide to use one of the MIRTE PCBs as
starting point. We used KiCad to design our PCBs, so everyone should be able
to modify our designs. The designs can be found in the `mirte_pcb
<https://github.com/mirte-robot/mirte-pcb>`_ repository.


Install the software
====================

After you have build and connected your robot, it is time to install the software.
This includes the MIRTE OS software for the computer, and our Telemetrix version
for the MCU.

Computer (SBC)
--------------

As menstioned earlier, installing the MIRTE OS can be done with different levels
of complexity. When sticking to one of the supported SBCs you can just :ref:`follow
the instructions <install_mirte_os>`.

If you want to use the MIRTE software on another SBC with Armbian support, you can 
create an image yourself using the `scripts we use <https://github.com/mirte-robot/mirte-sd-image-tools>`_
to build the default images.

In case you are not using an Arbian suported computer, you can also install
everyting yourself using our `install scripts <https://github.com/mirte-robot/mirte-install-scripts>`_.
Do note that you will probably run into some issues here, depending how close
your setup is to a regular Ubuntu system. This installation expects a Ubuntu 22.04
release.

Depending on your hardware choices and application, you might also need to install
some other ROS packages. Please note that these will probably not be exposed to 
the MIRTE Python API or MIRTE Blocky IDE.


Microcontroller (MCU)
---------------------

This should be similar to the regular :ref:`instructions <install_mirte_mcu>` on 
installing Telemetrix on the MCU.


Configure the robot
===================

Depending on the chosen hardware, you still need to configure the software in 
a way that it reflects your hardware. To do this you can follow the regular
instructions for :ref:`connecting to the robot <connect>`, and :ref:`accessing
the interface <access-interface>`.

To get the low level hardware to work, you need to update the settings for 
the robot. This can be done in the :ref:`regular way as well <configure-hardware>`,
and can be done via the web interface or by modifying the yaml file.

This should get you a robot, which you can control through ROS (and for some
peripherals also Python and Blockly). This only controls the lower levels of the 
robot though. So you should be able to control the single motors, but you will
probably not be able to send Twist commands (and use Nav2) or use MoveIt!

In order for these to work, you need to create a URDF of your robot. Building
a URDF is outside the scope of this tutorial, but ou can find the URDFs of both 
MIRTE robots in the `mirte_description package 
<https://github.com/mirte-robot/mirte-ros-packages/tree/main/mirte_description>`_.

After having setup the URDF in the right way (correct names etc), you will 
probably also have to change the `ros2_control hardware interface 
<https://github.com/mirte-robot/mirte-ros-packages/tree/develop/mirte_control>`_.
These can be found here:

`MIRTE Pioneer base (differentail) ros2_control hardware interface 
<https://github.com/mirte-robot/mirte-ros-packages/tree/develop/mirte_control/mirte_pioneer_control/hardware>`_

`MIRTE Master base (meccanum) ros2_control hardware interface 
<https://github.com/mirte-robot/mirte-ros-packages/tree/develop/mirte_control/mirte_master_base_control/hardware>`_

`MIRTE Master arm (4 DOF) ros2_control hardware intreface 
<https://github.com/mirte-robot/mirte-ros-packages/tree/develop/mirte_control/mirte_master_arm_control/hardware>`_

After having done this, you should be able to have a functioning MIRTE robot.






Configure Mirte
###############


Prepare microcontroller
=======================

Mirte also need some software on the microcontroller. Mirte uses the telemetrix protocol 
for this. There are two ways to upload this to the microcontroller.


Prepare from web interface
--------------------------



Prepare from terminal
---------------------

.. code-block:: bash

    mirte$ cd /usr/local/src/mirte/mirte_install_scripts
    mirte$ ./run_arduino.sh upload_stm32 Telemetrix4Arduino

You can also upload to Arduino Nano (both new and old bootloader) and Arduino Uno. In that 
case replace 'upload_stm32' with 'upload_nano', 'upload_nano_old', or 'upload_uno'.



Configure Software to match Hardware
====================================

This step in only needed in case you are not using the Mirte PCB (or followed the STM 
breadboard instructions). For other MCUs teh software still needs to know which pin is 
connected to what kind of hardware. This can be done in two ways.


From the Web Interface
----------------------



From the Terminal
-----------------

The configuration to map the pins to sensorstypes is done in /usr/local/src/mirte/mirte_control/config/mirte_base_config.yaml. 
This file consists of multiple sections needed for Mirte to know which pins to control. 
For convenience there are already three examples given for the STM32 on a breadboard, 
the Mirte PCB and an Arduino nano on a breadboard. The default settings are the Mirte PCB. 
Below we will got though all sections (of the STM32 on a breadboard).

.. code-block:: yaml

   device:
     mirte:
       type: breadboard
       mcu: stm32                     # [stm32, nano, nano_old, uno]

Each config needs to state which type of device is is controlling. In this case we have 
one device called 'mirte' of type 'breadboard' with a 'stm32' on it. The sampling interval 
is set to 10ms (100Hz), being the interval the data will be communicated from the mcu. 


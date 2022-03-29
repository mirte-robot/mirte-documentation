Configure Mirte
###############


Prepare microcontroller
=======================

Mirte also need some software on the microcontroller. Mirte uses a modified version
of the telemetrix protocol for this. There are two ways to upload this to the microcontroller.


Prepare from web interface
--------------------------

On the webinterface this is as easy as selecting the right MCU and press upload.

      .. image:: images/upload_telemetrix.png
        :width: 600
        :alt: Upload Telemetrix from web interface


Prepare from terminal
---------------------

On the terminal this can also be done by running a script:

.. code-block:: bash

    mirte$ cd /usr/local/src/mirte/mirte-install-scripts
    mirte$ ./run_arduino.sh upload_stm32 Telemetrix4Arduino

You can also upload to Arduino Nano (both new and old bootloader) and Arduino Uno. In that 
case replace 'upload_stm32' with 'upload_nano', 'upload_nano_old', or 'upload_uno'.



Configure Settings to match Hardware
====================================

This step in only needed in case you are not using the Mirte PCB (or followed the STM 
breadboard instructions). For other MCUs (or other wiring of the STM32) the software still
needs to know which pin is connected to what kind of hardware. This can be done in two ways.


From the Web Interface
----------------------

On the webinterface this can be done by removing and adding the peripherals in order
to match your robot hardware:

      .. image:: images/save_settings.png
        :width: 600
        :alt: Save settings


From the Terminal
-----------------

The configuration to map the pins to sensortypes is done in `/usr/local/src/mirte/mirte-ros-packages/mirte_telemetrix/config/mirte_user_config.yaml <https://github.com/mirte-robot/mirte-ros-packages/blob/main/mirte_telemetrix/config/mirte_user_config.yaml>`_. 
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


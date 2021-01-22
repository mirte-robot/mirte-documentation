Configure Software to match Hardware
####################################

This step in only needed in case you are not using the Zoef PCB (or followed the STM breadboard instructions). For other MCUs teh software still needs to know which pin is connected to what kind of hardware. This can be done in two ways.


From the Web Interface
=======================



From the Terminal
=======================

The configuration to map the pins to sensorstypes is done in /usr/local/src/zoef/zoef_control/config/zoef_base_config.yaml. This file consists of multiple sections needed for Zoef to know which pins to control. For convenience there are already three examples given for the STM32 on a breadboard, the Zoef PCB and an Arduino nano on a breadboard. The default settings are the Zoef PCB. Below we will got though all sections (of the STM32 on a breadboard).

Device
------
.. code-block:: yaml

   device:
     zoef:
       type: breadboard               # [breadboard, zoef_pcb], zoef_pcb implies a stm32 as mcu
       mcu: stm32                     # [stm32, nano, nano_old]
       samping_interval: 10           # integer in ms

Each config needs to state which type of device is is controlling. In this case we have one device called 'zoef' of type 'breadboard' with a 'stm32' on it. The sampling interval is set to 10ms (100Hz), being the interval the data will be communicated from the mcu. 


Motor
-----
.. code-block:: yaml

   motor:
     left_motor:
       device: zoef
       pins:
         1a: D5               # pin needs PWM
         1b: D6               # pin needs PWM
     right_motor:
       device: zoef
       pins:
         1a: D9               # pin needs PWM
         1b: D10              # pin needs PWM

The motors will be defined seperately. In this case there are two motors called 'left_motor' and 'right_motor', both controlled on the 'zoef' device defined above. The pins are set corrsponding to the L9110s motor driver. Other motor drivers will also work but the 1a/b refernce does not make sense.


Wheel encoder
-------------
.. code-block:: yaml

   encoder:
     left_encoder:
       device: zoef
       pins:
         pin: D2            # pin needs interrupt support
       ticks_per_wheel: 20
     right_encoder:
       device: zoef
       pins:
         pin: D3            # pin needs interrupt support
       ticks_per_wheel: 20



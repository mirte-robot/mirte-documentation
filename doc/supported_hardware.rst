Supported Hardware
##################


DC Motor
========
.. code-block:: yaml

   motor:
     left_motor:
       device: mirte
       pins:
         1a: D5               # pin needs PWM
         1b: D6               # pin needs PWM
     right_motor:
       device: mirte
       pins:
         1a: D9               # pin needs PWM
         1b: D10              # pin needs PWM

The motors will be defined seperately. In this case there are two motors called 'left_motor' and 'right_motor', both controlled on the 'mirte' device defined above. The pins are set corrsponding to the L9110s motor driver. Other motor drivers will also work but the 1a/b refernce does not make sense.


Wheel encoder
=============
.. code-block:: yaml

   encoder:
     left_encoder:
       device: mirte
       pins:
         pin: D2            # pin needs interrupt support
       ticks_per_wheel: 20
     right_encoder:
       device: mirte
       pins:
         pin: D3            # pin needs interrupt support
       ticks_per_wheel: 20


Servo
=====
.. code-block:: yaml

   servo:
     front:
       device: mirte
       pin: D9

.. warning::
   The servo uses the Servo library from Arduino (through Telemetrix). This also means that, when 
   a servo is used and the library is enabled, the last timer on teh MCU will be used for timing
   of the servos. This timer therefore can not be used for PWM anymore. For Arduino Nano/Uno this
   means pins 9 and 10 will not have PWM anymore. For the SMT32 this means pins X/Y will not have
   PWM anymore.








The motors will be defined seperately. In this case there are two motors called 'left_motor' and 'right_motor', both controlled on the 'mirte' device defined above. The pins are set corrsponding to the L9110s motor driver. Other motor drivers will also work but the 1a/b refernce does not make sense.



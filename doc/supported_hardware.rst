Supported Hardware
##################

Raw pins
========

.. tabs::

   .. group-tab:: ROS

      .. code-block:: bash

         $ rosservice /mirte/get_pin_value "{}"
         $ rosservice /mirte/set_pin_value "{}"

      Setting a pin can be either 'analog' (PWM) or 'digital'. The pin itself can be defined
      as the print on the MCU (e.g. 'A2'). you can have a look in the web interface to
      see all options. 

   .. group-tab:: Python

      .. code-block:: python
      
         from mirte_robot import robot
         mirte = robot.createRobot()

         mirte.getPinValue()
         mirte.setPinValue()
        
      Setting a pin can be either 'analog' (PWM) or 'digital'. The pin itself can be defined
      as the print on the MCU (e.g. 'A2'). you can have a look in the web interface to
      see all options.

   .. group-tab:: Blockly

      Blocky code 



.. warning::
    Currently there is no check on whether a pin is already in use by some hardware defined
    in the yaml configuration discussed earlier. Therefore there is no expected behaviour 
    when using getting or setting raw pins.


DC Motor
========

Depending on the type of 


L9110S
------
.. code-block:: yaml

   motor:
     left:
       name: left
       device: mirte
       type: l9110s
       pins:
         1a: B1
         1b: A10     # PWM

L298N
-----

.. code-block:: yaml

   motor:
     left:
       name: left
       device: mirte
       type: l298n
       pins:
         1a: B3
         1b: B1
         en: A10    # PWM


.. tabs::

   .. group-tab:: ROS

      .. code-block:: bash

         $ rosservice call /mirte/set_left_speed "speed: 50"

   .. group-tab:: Python

      .. code-block:: python
      
         from mirte_robot import robot
         mirte = robot.createRobot()

         mirte.setMotorSpeed('left', 50)
        
   .. group-tab:: Blockly

      Blocky code 

Speed can be an value between -100 and 100.


The motors will be defined seperately. In this case there are two motors called 'left_motor' and 'right_motor', both controlled on the 'mirte' device defined above. The pins are set corrsponding to the L9110s motor driver. Other motor drivers will also work but the 1a/b refernce does not make sense.


Wheel encoder
=============
.. code-block:: yaml

   encoder:
     left:
       name: left
       device: mirte
       pins:
         pin: B14    # interrupt


.. tabs::

   .. group-tab:: ROS

      As a topic (non-blocking):

      .. code-block:: bash

         $ rostopic echo /mirte/encoder/left

      As a service (blocking):

      .. code-block:: bash

         $ rosservice call /mirte/get_encoder_left "{}"

   .. group-tab:: Python

      .. code-block:: python
      
         from mirte_robot import robot
         mirte = robot.createRobot()

         mirte.getEncoder('left')
        
   .. group-tab:: Blockly

      Blocky code 

.. note::

   A maximum of 4 wheel encoders is supported.

Servo
=====
.. code-block:: yaml

   servo:
     left:
       name: left
       device: mirte
       pins:
         pin: B5

.. tabs::

   .. group-tab:: ROS

      .. code-block:: bash

         $ rosservice call /mirte/set_left_servo_angle "angle: 90"

   .. group-tab:: Python

      .. code-block:: python
      
         from mirte_robot import robot
         mirte = robot.createRobot()

         mirte.setServoAngle('left', 90)
        
   .. group-tab:: Blockly

      Blocky code 


Angle can be a value bewteen 0 and 180.

.. note::

   A maximum of 12 servos is supported.

.. warning::

   The servo uses the Servo library from Arduino (through Telemetrix). This also means that, when 
   a servo is used and the library is enabled, the last timer on teh MCU will be used for timing
   of the servos. This timer therefore can not be used for PWM anymore. For Arduino Nano/Uno this
   means pins 9 and 10 will not have PWM anymore. For the SMT32 this means pins X/Y will not have
   PWM anymore.


Keypad
======
.. code-block:: yaml

   encoder:
     left:
       name: left
       device: mirte
       pins:
         pin: A4     # analog input

.. tabs::

   .. group-tab:: ROS

      As a topic (non-blocking):

      .. code-block:: bash

         $ rostopic echo /mirte/keypad/left

      As a service (blocking):

      .. code-block:: bash

         $ rosservice call /mirte/get_keypad_left "{}"

   .. group-tab:: Python

      .. code-block:: python
      
         from mirte_robot import robot
         mirte = robot.createRobot()

         mirte.getKeypad('left')
        
   .. group-tab:: Blockly

      Blocky code 


OLED
====
.. code-block:: yaml

   oled:
     left:
       name: left
       device: mirte
       pins:
         scl: B6
         sda: B7

.. tabs::
   
   .. group-tab:: ROS

      .. code-block:: bash

         $ rosservice call /mirte/set_left_image "{type: 'text', value: 'hello mirte'}"
         $ rosservice call /mirte/set_left_image "{type: 'image', value: 'mirte_logo'}"
         $ rosservice call /mirte/set_left_image "{type: 'animation', value: 'eye'}"

   .. group-tab:: Python

      .. code-block:: python
      
         from mirte_robot import robot
         mirte = robot.createRobot()

         mirte.setOLEDText('left', 'hello mirte')
         mirte.setOLEDImage('left', 'mirte_logo')
         mirte.setOLEDAnimation('left', 'eye')
        
   .. group-tab:: Blockly

      Blocky code 

Distance sensor
===============
.. code-block:: yaml

   distance:
     left:
       name: left
       device: mirte
       pins:
         trigger: A5
         echo: A6

.. tabs::
   
   .. group-tab:: ROS

      As a topic (non-blocking):

      .. code-block:: bash

         $ rostopic echo /mirte/distance/left

      As a service (blocking):

      .. code-block:: bash

         $ rosservice call /mirte/get_distance_left "{}"

   .. group-tab:: Python

      .. code-block:: python
      
         from mirte_robot import robot
         mirte = robot.createRobot()

         mirte.getDistance('left')

   .. group-tab:: Blockly

      Blocky code

.. note::

   A maximum of 6 distance sensors is supported.

IR sensor
=========
.. code-block:: yaml

   intensity:
     left:
       name: left
       device: mirte
       pins:
         digital: B0
         analog: A1     # analog input

.. tabs::
   
   .. group-tab:: ROS

      As a topic (non-blocking):

      .. code-block:: bash

         $ rostopic echo /mirte/intensity/left
         $ rostopic echo /mirte/intensity/left_digital

      As a service (blocking):

      .. code-block:: bash

         $ rosservice call /mirte/get_intensity_left "{}"
         $ rosservice call /mirte/get_intensity_left_digital "{}"

   .. group-tab:: Python

      .. code-block:: python
      
         from mirte_robot import robot
         mirte = robot.createRobot()

         mirte.getIntensity('left')

      .. warning::
        
         Currently only the analog value is returned.

   .. group-tab:: Blockly

      Blocky code






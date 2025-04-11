Supported Hardware
##################


Microcontroller Peripherals
***************************

Raw pins
========

.. tabs::

   .. group-tab:: ROS

      .. code-block:: bash

         $ rosservice call /mirte/get_pin_value "{pin: '', type: ''}"
         $ rosservice call /mirte/set_pin_value "{pin: '', type: '', value: }"

      Setting a pin can be either 'analog' (PWM) or 'digital'. The pin itself can be defined
      as the print on the MCU (e.g. 'GP3'). You can have a look in the web interface to
      see all options. 

   .. group-tab:: Python

      .. code-block:: python
      
         from mirte_robot import robot
         mirte = robot.createRobot()

         mirte.getAnalogPinValue()

      .. autoclass:: robot::Robot
         :members: setAnalogPinValue, getAnalogPinValue, setDigitalPinValue, getDigitalPinValue
         :undoc-members:
         :noindex:

   .. group-tab:: Blockly

      .. image:: ../_images/blockly_raw.png




.. warning::
    Currently there is no check on whether a pin is already in use by some hardware defined
    in the yaml configuration discussed earlier. Therefore there is no expected behavior 
    when using getting or setting raw pins.


DC Motor
========

Depending on the interface of your motor controller, the DC motor can be controlled though three
different interfaces:

   - **ddp** (digital, digital, pwm): This interface uses two digital pins to set the direction of
     the motor, and uses a PWM dignal to set the speed. The L298 can use this interface.
   - **dp** (digital, pwm): This interface uses one digital pin for teh direction, and pwm for the speed.
     The downside is that the motor will slightly 'kick' when switching between forward and backward.
     This can be done on both L298 and L9110.
   - **pp** (pwm, pwm): This interface uses two PWM signals to control the motor. The downside is that
     this will take up 2 PWM pins. Can be used on both L298 and L9110.

As you can see the choice for interface depends on the actual interface provided by the motor
controller, and the number of (PWM) pins you have available on the MCU.


ddp (e.g. L298)
---------------
.. code-block:: yaml

   motor:
     left:
       name: left
       device: mirte
       type: ddp
       pins:
         d1: GP19
         d2: GP18
         p1: GP17     # pwm

dp (e.g. L298 or L9110)
-----------------------

.. code-block:: yaml

   motor:
     left:
       name: left
       device: mirte
       type: dp
       pins:
         d1: GP19
         p1: GP18      # pwm

pp (e.g. L298 or L9110)
-----------------------

.. code-block:: yaml

   motor:
     left:
       name: left
       device: mirte
       type: pp
       pins:
         p1: GP19       # pwm
         p2: GP18       # pwm


.. tabs::

   .. group-tab:: ROS

      .. code-block:: bash

         $ rosservice call /mirte/set_left_speed "speed: "

   .. group-tab:: Python

      .. code-block:: python
      
         from mirte_robot import robot
         mirte = robot.createRobot()

         mirte.setMotorSpeed('left', 50)
        
      .. autoclass:: robot::Robot
         :members: setMotorSpeed
         :undoc-members:
         :noindex:

   .. group-tab:: Blockly

      .. image:: ../_images/blockly_motor.png



The motors will be defined separately. In this case there are two motors called 'left_motor' and 
'right_motor', both controlled on the 'mirte' device defined above. The pins are set corresponding 
to the L9110s motor driver.

.. warning::
   
   Please not that it is adviced to call the motors 'left' and 'right'. You can chose your own names
   when you are only using these interfaces. In order to also get the ROS twist message (and steering
   in the web interface to work) you **need** to have the motors called 'left' and 'right'.

Servo
=====
.. code-block:: yaml

   servo:
     left:
       name: left
       device: mirte
       pins:
         pin: GP3

.. tabs::

   .. group-tab:: ROS

      .. code-block:: bash

         $ rosservice call /mirte/set_left_servo_angle "angle: 90"

   .. group-tab:: Python

      .. code-block:: python
      
         from mirte_robot import robot
         mirte = robot.createRobot()

         mirte.setServoAngle('left', 90)
        
      .. autoclass:: robot::Robot
         :members: setServoAngle
         :undoc-members:
         :noindex:

   .. group-tab:: Blockly

      .. image:: ../_images/blockly_servo.png



Keypad
======
.. code-block:: yaml

   encoder:
     left:
       name: left
       device: mirte
       pins:
         pin: GP28     # analog input

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
        
      .. autoclass:: robot::Robot
         :members: getKeypad
         :undoc-members:
         :noindex:


   .. group-tab:: Blockly

      .. image:: ../_images/blockly_keypad.png



OLED
====
.. code-block:: yaml

   oled:
     left:
       name: left
       device: mirte
       pins:
         scl: GP5
         sda: GP4

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
        
      .. autoclass:: robot::Robot
         :members: setOLEDText, setOLEDImage, setOLEDAnimation
         :undoc-members:
         :noindex:

   .. group-tab:: Blockly

      .. image:: ../_images/blockly_oled.png

Distance sensor
===============
.. code-block:: yaml

   distance:
     left:
       name: left
       device: mirte
       pins:
         trigger: GP7
         echo: GP6

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

      .. autoclass:: robot::Robot
         :members: getDistance
         :undoc-members:
         :noindex:

   .. group-tab:: Blockly

      .. image:: ../_images/blockly_distance.png

IR sensor
=========
.. code-block:: yaml

   intensity:
     left:
       name: left
       device: mirte
       pins:
         digital: GP16
         analog: GP26     # analog input

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

      .. autoclass:: robot::Robot
         :members: getIntensity
         :undoc-members:
         :noindex:

   .. group-tab:: Blockly

      .. image:: ../_images/blockly_ir.png


USB Camera
**********

By default the robot assumes you have connected the supported USB cam.
Currently only a ROS interface is defined.

.. tabs::

   .. group-tab:: ROS

      The camera image is published in three ways (using `ROS image transport <http://wiki.ros.org/image_transport>`_).

      .. code-block:: bash

         $ rostopic echo /webcam/image_raw
         $ rostopic echo /webcam/image_raw/compressed
         $ rostopic echo /webcam/image_raw/theora


Other USB Cameras
=================

In case you have another USB webcam, you might need to change the parameters of the `USB cam <https://wiki.ros.org/usb_cam>`_ to
reflect your webcam. This then needs to be changed in the `launchfile <https://github.com/mirte-robot/mirte-ros-packages/blob/3cbfac4a66425defc56f39b94bafca7794dd227e/mirte_bringup/launch/minimal.launch#L44>`_:

.. code-block:: bash      

   $ v4l2-ctl --list-formats-ext
   $ nano /home/mirte/mirte_ws/src/mirte_bringup/launch/minimal.launch


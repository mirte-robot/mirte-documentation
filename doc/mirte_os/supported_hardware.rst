Supported Hardware
##################


Microcontroller Peripherals
***************************

Raw pins
========

.. tabs::

   .. group-tab:: ROS

      .. code-block:: bash

         $ ros2 service call /io/get_analog_pin_value mirte_msgs/srv/GetAnalogPinValue "{pin: }"
         $ ros2 service call /io/get_digital_pin_value mirte_msgs/srv/GetDigitalPinValue "{pin: }"
         $ ros2 service call /io/set_digital_pin_value mirte_msgs/srv/SetDigitalPinValue "{pin: ,value: false}"
         $ ros2 service call /io/set_pwm_pin_value mirte_msgs/srv/SetPWMPinValue "{pin: ,value: false}"

      Setting a pin can be either 'analog' (PWM) or 'digital'. The pin itself can be defined
      as the print on the MCU (e.g. 'GP3'). You can have a look in the web interface to
      see all options. 

   .. group-tab:: Python

      .. code-block:: python
      
         from mirte_robot import robot
         mirte = robot.createRobot()

         mirte.getAnalogPinValue()

      .. automethod:: robot.Robot.setAnalogPinValue
         :noindex:

      .. automethod:: robot.Robot.getAnalogPinValue
         :noindex:

      .. automethod:: robot.Robot.setDigitalPinValue
         :noindex:

      .. automethod:: robot.Robot.getDigitalPinValue
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

         $ ros2 service call /io/motor/left/set_speed mirte_msgs/srv/SetMotorSpeed "{speed: 50}"

   .. group-tab:: Python

      .. code-block:: python
      
         from mirte_robot import robot
         mirte = robot.createRobot()

         mirte.setMotorSpeed('left', 50)

      .. automethod:: robot.Robot.setMotorSpeed        
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

         $ ros2 service call /io/servo/right/set_angle mirte_msgs/srv/SetServoAngle "{angle: 90, degrees: true}"

   .. group-tab:: Python

      .. code-block:: python
      
         from mirte_robot import robot
         mirte = robot.createRobot()

         mirte.setServoAngle('left', 90)

      .. automethod:: robot.Robot.setServoAngle        
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

         $ ros2 topic echo /io/keypad/left

      As a service (blocking):

      .. code-block:: bash

         $ /io/keypad/left/get_key

   .. group-tab:: Python

      .. code-block:: python
      
         from mirte_robot import robot
         mirte = robot.createRobot()

         mirte.getKeypad('left')

      .. automethod:: robot.Robot.getKeypad        
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

         $ ros2 service call /io/oled/right/set_text mirte_msgs/srv/SetOLEDText "{text: 'hello'}"

   .. group-tab:: Python

      .. code-block:: python
      
         from mirte_robot import robot
         mirte = robot.createRobot()

         mirte.setOLEDText('left', 'hello mirte')

      .. automethod:: robot.Robot.setOLEDText        
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

         $ ros2 topic echo /io/distance/left/get_range

      As a service (blocking):

      .. code-block:: bash

         $ ros2 service call /io/distance/left/get_range mirte_msgs/srv/GetRange

   .. group-tab:: Python

      .. code-block:: python
      
         from mirte_robot import robot
         mirte = robot.createRobot()

         mirte.getDistance('left')

      .. automethod:: robot.Robot.getDistance
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

         $ ros2 topic echo /io/intensity/left
         $ ros2 topic echo /io/intensity/left/digital

      As a service (blocking):

      .. code-block:: bash

         $ ros2 service call /io/intensity/left/get_analog mirte_msgs/srv/GetIntensity
         $ ros2 service call /io/intensity/left/get_digital mirte_msgs/srv/GetIntensityDigital

   .. group-tab:: Python

      .. code-block:: python
      
         from mirte_robot import robot
         mirte = robot.createRobot()

         mirte.getIntensity('left')

      .. automethod:: robot.Robot.getIntensity
         :noindex:

   .. group-tab:: Blockly

      .. image:: ../_images/blockly_ir.png


Color sensor
============
.. code-block:: yaml

   color:
     left:
       name: left
       device: mirte
       pins:
       pins:
         scl: GP5
         sda: GP4

.. tabs::

   .. group-tab:: ROS

      As a topic (non-blocking):

      .. code-block:: bash

         $ ros2 topic echo /io/color/left/hsl
         $ ros2 topic echo /io/color/left/rgb

      As a service (blocking):

      .. code-block:: bash

         $ ros2 service call /io/intensity/left/get_analog mirte_msgs/srv/GetIntensity
         $ ros2 service call /io/intensity/left/get_digital mirte_msgs/srv/GetIntensityDigital

   .. group-tab:: Python

      .. code-block:: python

         from mirte_robot import robot
         mirte = robot.createRobot()

         mirte.getColor('left')['h']

      .. automethod:: robot.Robot.getColor
         :noindex:

   .. group-tab:: Blockly

      .. image:: ../_images/blockly_color.png


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


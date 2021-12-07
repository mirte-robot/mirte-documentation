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
      as the print on the MCU (e.g. 'A2'). you can have a look in the web interface to
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

      TODO



.. warning::
    Currently there is no check on whether a pin is already in use by some hardware defined
    in the yaml configuration discussed earlier. Therefore there is no expected behavior 
    when using getting or setting raw pins.


DC Motor
========

Depending on the type of motor controller used, you can control a motor. 

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

      TODO


The motors will be defined separately. In this case there are two motors called 'left_motor' and 'right_motor', both controlled on the 'mirte' device defined above. The pins are set corresponding to the L9110s motor driver. Other motor drivers will also work but the 1a/b reference does not make sense.


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
        
      .. autoclass:: robot::Robot
         :members: getEncoder
         :undoc-members:
         :noindex:

   .. group-tab:: Blockly

      TODO

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
        
      .. autoclass:: robot::Robot
         :members: setServoAngle
         :undoc-members:
         :noindex:

   .. group-tab:: Blockly

      Blocky code 



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
        
      .. autoclass:: robot::Robot
         :members: getKeypad
         :undoc-members:
         :noindex:


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
        
      .. autoclass:: robot::Robot
         :members: setOLEDText, setOLEDImage, setOLEDAnimation
         :undoc-members:
         :noindex:

   .. group-tab:: Blockly

      TODO

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

      .. autoclass:: robot::Robot
         :members: getDistance
         :undoc-members:
         :noindex:

   .. group-tab:: Blockly

      TODO

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

      .. autoclass:: robot::Robot
         :members: getIntensity
         :undoc-members:
         :noindex:

   .. group-tab:: Blockly

      TODO


USB Camera
**********

By default the robot assumes you have connected the supported USB cam (see :ref:`basic hardware <Get Mirte Hardware>`).
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


PS3/4 Controller
****************

To control the robot with a PS3/4 controller you first need to connect the controller with
a bluetooth dongle. So first insert a bluetooth dongle (flaky Chinese dongles will also work
for the OrangePi, not (yet) for RaspberryPi). You first need to pair the dongle with the
PS controller:

.. code-block:: bash

    mirte$ sudo bluetoothctl
    [bluetooth]# agent on
    [bluetooth]# default-agent
    [bluetooth]# scan on


Connect the PS3 via a USB cable to the SBC (on the Orange Pi Zero one might need the expansion board in order
to have more USB ports). A PS$ controller does not need to be connected to the USB. Press the connect button 
(PS logo) on the controller. In the terminal one will see the device being found. Type "yes" to confirm and 
exit the bluetoothctl.

To test the controller one can:

.. code-block:: bash

    mirte$ sudo jstest /dev/input/js0

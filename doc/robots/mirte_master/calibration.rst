Calibration
###########

Now that we have assembled the robot we might need to tune some of the settings
for the robot to operate correctly.

Base PID
--------

Change PID parameters of the base controller with:

``$ ros2 param set /pid_wheels_controller gains.front_left_wheel_joint.p 1.0``

``$ ros2 param set /pid_wheels_controller gains.front_left_wheel_joint.i 1.0``

``$ ros2 param set /pid_wheels_controller gains.front_left_wheel_joint.d 1.0``


Arm position
------------

Although you tried the best you could to assemble the arm in the home (i.e.
upright) position, it is impossible to have this exactly right. We therefore
still need to calibrate the servo's

``$ ros2 run mirte_test mirte_master_calibrate.py``

.. warning::

   This script should unlock the servo's. If you feel that one of the servo'saw
   is still locked (i.e. you are unable to change it), please restart the script.
   Due to a bug, the Elbow (HTD-35H) might stay locked. 







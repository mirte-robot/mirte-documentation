FAQ
###


I have another (Single Board) Computer lying around, can I get this to work as well? 
------------------------------------------------------------------------------------
Currently this computer would need to have a USB (to connect to the microcontroller) and wifi (e.g. through a dongle). You might then try to install Mirte from source. You will have the best change with a 32bit Ubuntu distribution installed.

I have another microcontroller lying around, can I get this to work as well?
----------------------------------------------------------------------------
As long as you can get telemetrix on there, this should work as well. It depends on the specs of this MCU wheter all hardware can be supported. Some hardware need interrupt pins, some hardware need pwm or i2c. 

Can you add hardware X to the platform?
---------------------------------------
Depending on the usecasse we will. A lot of hardware is already usable in ROS. So at some point it does not make sense to expose those to the Python or Blockly API. Sensors at the arduino level might be incorporated (as long as they make sense in a robotics application).

I changed my password when logging into SSH, but the AP password, Arduino IDE password, and web interface password did not change?
----------------------------------------------------------------------------------------------------------------------------------
This is 'correct' and we still need to find a way to solve this.

I am not able to connect to mirte.local.
----------------------------------------
This might be a problem related to Windows/Android. If you are running Linux or MacOS this should work. First make sure that you are on the same network. Also check if you can ping mirte.local. Also make sure that you are trying to connect to http://mirte.local/ (the http:// in front, and / at the end might be needed).

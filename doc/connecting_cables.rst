Connecting the Cables
#####################


Connecting the power
====================

.. tabs::

   .. group-tab:: Mirte PCB

      Currently the PCB is only used by ourselves. Instructions can therefore be found in the same (Dutch) `instruction manual <https://surfdrive.surf.nl/files/index.php/s/RULqnIFU7yhXLJZ/download?path=%2F&files=W2%20-%20in%20elkaar%20zetten.pdf>`_.

   .. group-tab:: STM32

      .. tabs::

         .. group-tab:: Orange Pi Zero

            .. tabs::

               .. group-tab:: USB

               .. group-tab:: dupont

         .. group-tab:: Raspberry Pi

            .. tabs::

               .. group-tab:: USB

               .. group-tab:: dupont
         
   .. group-tab:: Arduino Nano

      .. tabs::

         .. group-tab:: Orange Pi Zero

            .. tabs::

               .. group-tab:: USB

               .. group-tab:: dupont

         .. group-tab:: Raspberry Pi

            .. tabs::

               .. group-tab:: USB

               .. group-tab:: dupont


   .. group-tab:: Arduino Uno

      .. tabs::

         .. group-tab:: Orange Pi Zero

            .. tabs::

               .. group-tab:: USB

               .. group-tab:: dupont

         .. group-tab:: Raspberry Pi

            .. tabs::

               .. group-tab:: USB

               .. group-tab:: dupont






Connecting the peripherals
==========================

The Mirte PCB is nothing more than just a bunch of cables on a board. You can of
course also connect the same hardware to a breadboard. The fritzing image below 
shows you how to connect all the hardware in order to get the same pin layout
as the PCB. But you are also free to chose different pins and change the 
configuration later on.

.. tabs::

   .. group-tab:: Mirte PCB

      Currently the PCB is only used by ourselves. Instructions can therefore be found in the same (Dutch) `instruction manual <https://surfdrive.surf.nl/files/index.php/s/RULqnIFU7yhXLJZ/download?path=%2F&files=W2%20-%20in%20elkaar%20zetten.pdf>`_.

   .. group-tab:: STM32

      .. image:: images/full_PCB_bb.png
        :width: 600
        :alt: Alternative text


   .. group-tab:: Arduino Nano

     .. image:: images/full_nano_bb.png
       :width: 600
       :alt: Alternative text

     .. note::
       Please note that:

       - Only two motors are connected.
       - The motors are now controlled with one PWM and one digital pin.
       - Two I2C OLED screens are only possible when you have two OLEDS with different addresses (either by default, or soldered).

   .. group-tab:: Arduino Uno

     .. image:: images/full_uno_bb.png
       :width: 600
       :alt: Alternative text

     .. note::
       Please note that:

       - Only two motors are connected.
       - The motors are now controlled with one PWM and one digital pin.
       - Two I2C OLED screens are only possible when you have two OLEDS with different addresses (either by default, or soldered).
       - The digital value of the IR line sensor is not used.
       - The power of all peripherals (or at least the motor controller) needs to come from the breadboard power supply.




Using another MCU
#################


Prepare microcontroller
=======================

As mentioned during the :ref:`software installation <Install MIRTE Software>` the MIRTE robot needs
some software on the microcontroller to work. MIRTE uses a modified version of the Telemetrix 
protocol for this. This step is only needed when you have another MCU then the Raspberry Pi
Pico (i.e. STM32, Arduino Nano, or Arduino Uno).

From the terminal you can upload Telemetrix by executing:

.. code-block:: bash

    mirte$ cd /usr/local/src/mirte/mirte-install-scripts
    mirte$ ./run_arduino.sh upload_stm32 Telemetrix4Arduino

You can also upload to Arduino Nano (both new and old bootloader) and Arduino Uno. In that 
case replace 'upload_stm32' with 'upload_nano', 'upload_nano_old', or 'upload_uno'.

After this one still needs to configure the robot to match the pins of the MCU as
described in :ref:`Configure MIRTE<Configure MIRTE>`.

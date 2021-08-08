Programming the MCU
###################


From terminal
=============


Using Platform IO
=================



Using the Arduino IDE
=====================
.. warning::
   Since Windows does not fully support mDNS (services) programming from the Arduino IDE will not work on Windows unless you follow the instructions here.
.. warning::
   Currently this is only supported for the SMT32.


Under water ROS assumes an MCU with telemetrix_ installed on it (basically making the MCU a dump machine). Of course you can also program directly on teh MCU. This will break all ROS, Python, Blockly functionality though. In order to program the MCU from the Arduino IDE the PC with the IDE should be connected to the same network as Mirte (or the AP that Mirte created). 

.. _telemetrix: https://github.com/MrYsLab/telemetrix

The Arduino IDE should be configured in the same way as if the MCU was connected to the PC through USB. For the STM this means:

1. Add 'https://github.com/stm32duino/BoardManagerFiles/raw/master/STM32/package_stm_index.json' to 'File' > 'Settings' > 'Additional Boards Manager URLs'
2. Install 'STM32 Cores' from 'Tools' > 'Board: xxxx' > 'Boards Manager...'
3. Select 'Generic STM32F1 series' as 'Board', and make sure the other settings are as in the image below.
4. Compile and run will compile locally and upload the hex to Mirte (passwd: mirte_mirte)

.. note::
   Uploading in this way will stop the ROS master.


.. image:: Mirte_Arduino_IDE.png
  :width: 600
  :alt: Mirte Arduino IDE

You can test this by running the blink example for the STM:

.. code-block:: c

   void setup() {
      pinMode(PC13, OUTPUT);
   }

   void loop() {
     digitalWrite(PC13, HIGH);
     delay(1000);
     digitalWrite(PC13, LOW);
     delay(1000);
   }

.. warning::
   When uploading incorrect images to te STM (for example 'PC_13' instead of 'PC13'), the STM32 might hang, and uploading will not work. In that case you have to press the physical reset button on the STM while the IDE is uploading.

.. note::
   You can always bring up ROS againg by perparing the MCU again (by installing telemetrix on the MCU).




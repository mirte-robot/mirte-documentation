Prepare microcontroller
#######################

Mirte also need some software on the microcontroller. Mirte uses the telemetrix protocol for this. There are two ways to upload this to the microcontroller.


Upload from web interface
=========================
.. warning::
   Currently this method only supports the STM32. For other supported MCUs see instrcutions below.



Upload from commandline
================================

Upload to STM32
---------------
.. code-block:: bash

    mirte$ cd /usr/local/src/mirte/mirte_arduino
    mirte$ ./run.sh upload FirmataExpress

Upload to Arduino Nano (new bootloader)
---------------------------------------
.. code-block:: bash

    mirte$ cd /usr/local/src/mirte/mirte_arduino
    mirte$ ./run.sh upload_nano FirmataExpress

Upload to Arduino Nano (old bootloader)
---------------------------------------
.. code-block:: bash

    mirte$ cd /usr/local/src/mirte/mirte_arduino
    mirte$ ./run.sh upload_nano_old FirmataExpress

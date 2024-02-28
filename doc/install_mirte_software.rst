Install Mirte Software
######################

For Mirte to work we need to install software on both the SD 
card and the microcontroller.

Download prebuilt SD card image
===============================

.. tabs::

  .. tab:: Orange Pi Zero 2

    1. Download the latest SD card image `here <https://surfdrive.surf.nl/files/index.php/s/GQqcuJnuVDlHPfQ/download>`_ (currently v0.1_rc1).
    2. Burn the image onto the SD card with for example `Balena Etcher <https://www.balena.io/etcher/>`_.
    3. Put the SD card in the Orange Pi Zero 2.

  .. tab:: Raspberry Pi 2/3/4

    1. Download the latest SD card image `here <https://surfdrive.surf.nl/files/index.php/s/CzwE5b951vGXGjE/download>`_ (currently v0.1_rc1).
    2. Burn the image onto the SD card with for example `Balena Etcher <https://www.balena.io/etcher/>`_.
    3. Put the SD card in the Raspberry Pi.

Install MCU software
====================

Currently this step is only needed for the Raspberry Pi Pico, which is
the default MCU for Mirte. Instruxtions on installing this for
other MCUs can be found here.

1. Download the latest uf2 with the Mirte version of Telemetrix `here <https://surfdrive.surf.nl/files/index.php/s/wyXJYGDnWs8gUNL/download>`_.
2. Connect the Pico to you computer using a USB cable (with data) while pressing the BOOTSEL button.
3. Copy the uf2 file to the mass storage device called RPI_RP2.

Installation
############

For the MIRTE Pioneer or MIRTE Master to work we need to install software on both the SD card and the microcontroller.
It might be useful to do this before fully assembling the robot. But it can also be done at a later stage.


.. _install_mirte_os:

Install MIRTE OS image
======================

.. tabs::

  .. group-tab:: MIRTE Pioneer

    The MIRTE Pioneer uses the Orange Pi Zero2. So we need to download the correct image:

    1. Download the latest SD card image `here <https://github.com/mirte-robot/mirte-sd-image-tools/releases/latest>`_ (mirte_orangepizero2.img.xz).
    2. Burn the image onto the SD card with for example `Balena Etcher <https://www.balena.io/etcher/>`_.
    3. Put the SD card in the Orange Pi Zero 2.

    .. image:: ./_images/mirte_sd.svg

    The SD image will have two partitions. One containing the MIRTE software, which is read-only and serves as an overlayfs lower folder. The other one
    will be expanded to the max size and serves as an upper folder for overlayfs. This measn that all your work/changes will be stored in that partition.

  .. group-tab:: MIRTE Master

    The MIRTE Master uses the Orange Pi 3B. This board can be extended with eMMC memory. You can install the MIRTE OS
    on an SD card, or on eMMC.

    .. tabs::

      .. tab:: SD

        1. Download the latest SD card image `here <https://github.com/mirte-robot/mirte-sd-image-tools/releases/latest>`_ (mirte_master_mirte_orangepi3b.img.xz).
        2. Burn the image onto the SD card with for example `Balena Etcher <https://www.balena.io/etcher/>`_.
        3. Put the SD card in the Orange Pi 3B.

        .. image:: ./_images/mirte_sd.svg

        The SD image will have two partitions. One containing the MIRTE software, which is read-only and serves as an overlayfs lower folder. The other one
        will be expanded to the max size and serves as an upper folder for overlayfs. This measn that all your work/changes will be stored in that partition.


      .. tab:: eMMC

        1. Download the latest SD card image `here <https://github.com/mirte-robot/mirte-sd-image-tools/releases/latest>`_ (mirte_master_installer_orangepi3b.img.xz).
        2. Burn the image onto the SD card with for example `Balena Etcher <https://www.balena.io/etcher/>`_.
        3. Put the SD card in the Orange Pi 3B.
        4. Boot the Orange Pi 3B, and wait approximately 20 min until the robot shuts off.
        5. Remove the SD card.

        .. image:: ./_images/mirte_installer_sd.svg

        The MIRTE software will be installed on the eMMC. This will be read-only and serve as the lower overlayfs folder. It makes sense to have an
        SD card with an empty overlayfs partition to store all your work/changes. This is the overlay_image download.


  .. tab:: Custom SBC

    Currently we support images for the Orange Pi Zero 2 (MIRTE Pioneer), Orange Pi 3B (MIRTE Master), and the Raspberry Pi.
    Depending on you hardware you can run the MIRTE OS from an SD card, or from eMMC.

    .. tabs::

      .. tab:: SD

        1. Download the latest SD card image for your hardware `here <https://github.com/mirte-robot/mirte-sd-image-tools/releases/latest>`_.
        2. Burn the image onto the SD card with for example `Balena Etcher <https://www.balena.io/etcher/>`_.
        3. Put the SD card in your SBC.

        .. image:: ./_images/mirte_sd.svg

        The SD image will have two partitions. One containing the MIRTE software, which is read-only and serves as an overlayfs lower folder. The other one
        will be expanded to the max size and serves as an upper folder for overlayfs. This measn that all your work/changes will be stored in that partition.

      .. tab:: eMMC

        1. Download the latest SD card image for your hardware `here <https://github.com/mirte-robot/mirte-sd-image-tools/releases/latest>`_.
        2. Burn the image onto the SD card with for example `Balena Etcher <https://www.balena.io/etcher/>`_.
        3. Put the SD card in your SBC
        4. Boot the Orange Pi 3B, and wait until the robot shuts off (this can take some time. eg 20 mins on the MIRTE Master).
        5. Remove the SD card.

        .. image:: ./_images/mirte_installer_sd.svg

        The MIRTE software will be installed on the eMMC. This will be read-only and serve as the lower overlayfs folder. It makes sense to have an
        SD card with an empty overlayfs partition to store all your work/changes. This is the overlay_image download.

.. _install_mirte_mcu:

Install MCU software
====================

The MIRTE OS software needs to communicate (via Telemetrix) with the microcontroller (MCU).
One therefore also need to install this onto the MCU.

.. tabs::

  .. group-tab:: MIRTE Pioneer

     1. Download the latest uf2 with the MIRTE version of Telemetrix `here <https://github.com/mirte-robot/mirte-sd-image-tools/releases/latest>`_ (Telemetrix4RpiPico.uf2).
     2. Connect the Pico to you computer using a (data) USB cable while pressing the BOOTSEL button.
     3. Copy the uf2 file to the mass storage device called RPI_RP2.

  .. group-tab:: MIRTE Master

     These instructions assume you have the Raspberry Pi Pico connected to the OrangePi 3B via
     USB, and have installed MIRTE OS on the OrangePi 3B. Login to a terminal on the OrangePi 3B
     and:

     .. code-block:: bash

        mirte$ cd /usr/local/src/mirte/mirte-install-scripts
        mirte$ ./run_arduino.sh upload_pico

  .. tab:: Custom MCU

     Currently this step is only needed for the Raspberry Pi Pico, which is
     the default MCU for MIRTE. When using a Raspberry Pi Pico, you can follow
     the instructions of the MIRTE Pioneer. Instructions on installing this for
     other MCUs can be found :ref:`here <Using another MCU>`.

Installed Software
==================

After installing your MIRTE OS v0.2 image you will have a robot running:

+------------------+---------+--------+--------+--------+
| SBC              | Armbian | Ubuntu | kernel | ROS    |
+==================+=========+========+========+========+
| Orange Pi Zero 2 | 25.2.3  | 22.04  | 6.6.62 | Humble |
+------------------+---------+--------+--------+--------+
| Orange Pi 3b     | 25.2.3  | 22.04  | 6.13.3 | Humble |
+------------------+---------+--------+--------+--------+
| Raspberry Pi 3/4 | 24.8.1  | 22.04  | 6.6.45 | Humble |
+------------------+---------+--------+--------+--------+


Updating Software
=================

Updating the software currently means reinstallign the software: downloading
the newest software image, and installing it on an SD-card. Please note that
you will loose your own work done on the MIRTE if you use the same SD-card as
before. 

After re-installation you might also need to update the software on the MCU.
If your current version of the MIRTE Telemetrix on the MCU is relatively new,
this step will be easy.

.. tabs::

  .. group-tab:: MIRTE Pioneer

     These instructions assume you have the Raspberry Pi Pico connected to the OrangePi Zero2 via
     the MIRTE PBC, and have installed MIRTE OS on the OrangePi Zero2. Login to a terminal on the 
     OrangePi and:

     .. code-block:: bash

        mirte$ cd /usr/local/src/mirte/mirte-install-scripts
        mirte$ ./run_arduino.sh upload_pico
        mirte$ ./run_arduino.sh upload_pico # need to do this twice due (known issue)

     If this does not work (even after the second try), you will probably have an older
     version of the Telemetrix software installed which is not able to auto-update. Please
     follow the instructions above to upload the new software.

  .. group-tab:: MIRTE Master

     These instructions assume you have the Raspberry Pi Pico connected to the OrangePi 3B via
     USB, and have installed MIRTE OS on the OrangePi 3B. Login to a terminal on the OrangePi 3B
     and:

     .. code-block:: bash

        mirte$ cd /usr/local/src/mirte/mirte-install-scripts
        mirte$ ./run_arduino.sh upload_pico

  .. tab:: Custom MCU

     Currently this step is only needed for the Raspberry Pi Pico, which is
     the default MCU for MIRTE. When using a Raspberry Pi Pico, you can follow
     the instructions of the MIRTE Pioneer. Instructions on installing this for
     other MCUs can be found :ref:`here <Using another MCU>`.

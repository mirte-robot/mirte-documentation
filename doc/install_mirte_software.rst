Install Mirte Software
######################

For Mirte to work we need to install software on both the SD card as on the microcontroller. This part only covers the installation of the SD software.

Download prebuilt SD card image
===============================
.. warning::
   The prebuilt SD card will currentl only work on the Orange Pi Zero. All other plaforms will have to install from source (which will be supported later).

1. Download the SD card image from here.
2. Burn the image onto the SD card with for example Balena Etcher.
3. Put the SD card in the Orange Pi Zero.


Install from source (Not supported Yet)
=======================================
.. warning::
  Installing from source might fail on the Orange Pi Zero due to low specs. Installing from source is only recommended when using a more powerful computer.

.. prompt:: bash $

    wget https://github.com/mirte_robot/mirte_install_scripts/raw/install_mirte.sh | sh

Please get yourself a cup of coffee, this might take some time........

Connect to Zoef
###############

After booting up Zoef for the first time the robot is in acces point (AP) mode and a wifi network will be available with ssid Zoef_XXXXXX. You can connect to this network with the password zoef_zoef. While in AP mode, the ip address of Zoef is 192.168.42.1, but you could also access it with zoef.local or zoef_XXXXXX.local. In this tutorial we will always use zoef.local. 



Access Web Interface (Easy)
===========================






Access to SSH
=============

On Linux and MacOS you can ssh by opening a terminal. On Windows you could use a MobaXTerm. You can connect to Zoef via SSH (first time login password is zoef_zoef):

.. prompt:: bash $

    ssh zoef@zoef.local


Connecting Zoef to your own Wifi
================================

You can connect Zoef to your local wifi network from the web interface. 
.. note::
Even after you connected to your own network, Zoef will start an Acces Point in case it is not able to conect to it (e.g. when somewhere else). 

.. warning::
   For Windows users only: Windows 10 does not fully support mDSN. Therefore, when connecting to your own Wifi the zoef.local will not be resolved. One needs to install Apple Bonjour from here. On Windows 10 one might also need to disable the Windows mDNS service from the registry.






Connect to Mirte
################

After booting up Mirte for the first time the robot is in acces point (AP) mode and a wifi network will be available with ssid Mirte_XXXXXX. You can connect to this network with the password mirte_mirte. While in AP mode, the ip address of Mirte is 192.168.42.1, but you could also access it with mirte.local or mirte_XXXXXX.local. In this tutorial we will always use mirte.local. 



Access Web Interface (Easy)
===========================






Access to SSH
=============

On Linux and MacOS you can ssh by opening a terminal. On Windows you could use a MobaXTerm. You can connect to Mirte via SSH (first time login password is mirte_mirte):

.. prompt:: bash $

    ssh mirte@mirte.local


Connecting Mirte to your own Wifi
=================================

You can connect Mirte to your local wifi network from the web interface. 
.. note::
Even after you connected to your own network, Mirte will start an Acces Point in case it is not able to conect to it (e.g. when somewhere else). 

.. warning::
   For Windows users only: Windows 10 does not fully support mDSN. Therefore, when connecting to your own Wifi the mirte.local will not be resolved. One needs to install Apple Bonjour from here. On Windows 10 one might also need to disable the Windows mDNS service from the registry.






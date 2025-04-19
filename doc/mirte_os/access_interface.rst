Accessing the interface
#######################

MIRTE has two interfaces: the web interface and the linux terminal through SSH.
With the web interface one is able to program the robot in Blockly and Python, 
while Python and ROS are your options when connected with SSH.



Web Interface
=============

The web interface can be accessed by opening your favorite browser and going
to http://mirte.local. This will bring you to the web interface.

.. note::

   When connected to another Acces Point, the web interface will prompt you
   for your username (mirte) and password (the one you set). This will not be
   done when connected to a Windows hotspot (IP range 192.168.137.1-255). 


Terminal
========

.. note::

   In this tutorial we will use '$' when the command needs to be executed on
   your own machine, while we use 'mirte$' when a command needs to be executed
   on the MIRTE robot.

On Linux and MacOS you can SSH by opening a terminal. On Windows you could 
the optional built-in SSH client (Windows 10/11), use Putty, or MobaXTerm. You can 
connect to MIRTE via SSH (first time login password is 'mirte_mirte'):

.. code-block:: bash

    $ ssh mirte@mirte.local

The first time you login you will be prompted to change your password (to at
least 8 characters). After changing this your SSH connection will be closed and 
you have to reconnect using the same command. This will also change the password 
for the Wifi network on the next boot of the robot.

.. warning::

   Please note that the password of the Wifi network will be changed. Your OS
   might have (auto)saved the old password, so you have to tell your OS
   to 'forget' the network, so you can login using your new passeord.




Keybased SSH login
------------------

When frequently connecting to the terminal it might be useful to connect
to MIRTE without passwords using shared keys. This can be done easily if you
connect from another terminal (so only on MaxOS and Linux) on your local 
machine. You can set this up in the following way.

On MIRTE:

.. code-block:: bash

    mirte$ ssh-keygen -t rsa -f ~/.ssh/id_rsa -q -P ""

On your own machine:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: bash

         $ ssh-copy-id mirte@mirte.local

   .. group-tab:: MacOS

      .. code-block:: bash

         $ ssh-copy-id mirte@mirte.local

   .. group-tab:: Windows

      .. code-block:: bash

         > ssh-keygen.exe -t rsa -f ~/.ssh/id_rsa -q -P ""
         > type $env:USERPROFILE\.ssh\id_rsa.pub | ssh mirte@mirte.local "cat >> .ssh/authorized_keys"








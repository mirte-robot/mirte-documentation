Accessing the interface
#######################

Mirte has two interfaces: the web interface and the linux terminal through SSH.
With the web interface one is able to program the robot in Blockly and Python, 
while Python and ROS are your options when connected with SSH.



Web Interface
=============

The web interface can be accessed by opening your favorite browser and going
to http://mirte.local. This will bring you to the web interface.

.. note::

   When your Mirte robot is connected to a network (so not via AP or USB) the
   web interface will ask for a password. Please select your own Mirte robot
   and fill in password 'mirte_mirte'. Note that this password is currently
   **not** changed when you reset your ssh password (see known issues).


Terminal
========

On Linux and MacOS you can SSH by opening a terminal. On Windows you could 
the optional built-in SSH client (Windows 10), use Putty, or MobaXTerm. You can 
connect to Mirte via SSH (first time login password is 'mirte_mirte'):

.. code-block:: bash

    $ ssh mirte@mirte.local


.. note::

   In this tutorial we will use '$' when the command needs to be executed on
   your own machine, while we use 'mirte$' when a command needs to be executed
   on the Mirte robot.
  

The first time you login you will be prompted to change your password. After
changing this your connection will be lost and you have to reconnect using
the same command. Please have a look at the known issues regarding current
password management.

Keybased SSH login
------------------

When connecting to the terminal frequently it might be useful to connect
to Mirte without passwords using shared keys. This can be done easily if you
connect from another terminal (so only on MaxOS and Linux) on your local 
machine. You can set this up in the following way.

On Mirte:

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








Renaming MIRTE
==============

By default the MIRTE robot will base its name (and SSID) on the robots MAC address. This
makes sure that the ID/name is connected to the robot (i.e. the computer) and will not change
when you create a new SD image. 

In some cases it might be useful to rename the unique ID of your MIRTE. This can be done by
changing this default behaviour to a random ID, or by modifying it manually.

Random name
-----------

To set the robot to create a random ID on boot (this will only be done once), you have to set
the USE_MAC value in /usr/local/src/mirte/mirte-install-scripts/network_setup.sh to false. And
you have to make sure that the robot will regenerate a new ID by setting the current hostname
to its initial value Mirte_XXXXXX:

.. code-block:: bash

   mirte$ sudo bash -c "echo Mirte-XXXXXX > /etc/hostname"
   mirte$ sudo reboot now


Custom name
-----------

You can also override the name manually. This will prevent the robot from creating a name.
This can be done by changing the linux hostname:

.. code-block:: bash

   mirte$ sudo bash -c "echo <you_robot_name> > /etc/hostname"
   mirte$ sudo reboot now




Programming Mirte
#################

The goal of Mirte is to get everyone to learn about robotics. This means that there are multiple layers of complexity available.

.. warning:: 
   Currently there is no check on whether a pin is already in use by some
   hardware defined in the yaml configuration discussed earlier. Therefore
   there is no expected behaviour when using either:

   - $ rosservice /mirte/get_pin_value # for ROS)
   - $ rosservice /mirte/set_pin_value # for ROS)
   - mirte.getPinValue() # in Python
   - mirte.setPinValue() # in Python
   - get and set pin values in Blockly

Blockly
=======




Python
======

Depending on the settings in teh web interface, the Python shown in the web interface will be editable or not. 

From web interface
------------------

In Jupyter Notebook
-------------------

From PyCharm IDE
----------------

From terminal
-------------

.. code-block:: python

   import robot
   mirte = robot.createRobot()


The full interface can be found here.




ROS
===


In Jupyter Notebook
-------------------

By default the Jupyter is not running. You can start it as a service:

.. code-block:: bash

   mirte$ sudo service mirte_jupyter start

Jupyter will run on http://mirte.local:8888 showing some examples from Jupyter-ROS (which are located at /home/mirte/jupyter-ros). If you want Jupyter to start on boot you can run:

.. code-block:: bash

   mirte$ sudo systemctrl enable mirte_jupyter


From terminal
-------------

With Blockly being converted into Python, under water the Python code just becomes a running ROS node when started. When robot.createRobot() is called a node named mirte_python_api will be started. So all controll software is done in ROS. You can find the full API of services and topics here.

When Mirte start a systemd service will launch the Mirte bringup. This service can be stopped and started manyally as well:

.. code-block:: bash

   mirte$ sudo service mirte_ros stop
   mirte$ sudo service mirte_ros start

You can also run the launchfile yourself (only when you stopped the systemd service):

.. code-block:: bash

   mirte$ roslaunch mirte_bringup bringup.launch


















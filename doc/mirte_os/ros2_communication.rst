ROS2 Communication
##################

ROS2 (DSS) uses a discovery mechanism to communicate between the nodes. By default
this will allow all computers in the same network as the robot to discover the 
ROS2 nodes. This might not be usefull in an educational setup. Therefore there are 
three setups you can use on the MIRTE robot:

.. list-table::
   :widths: 30 40 40
   :header-rows: 1

   * - Type
     - Discovery
     - Useful setup
   * - localhost (MIRTE default)
     - Only on the robot
     - All robots on the same network, but no need to use ROS from another machine
   * - zenoh
     - Only those who set zenoh conf
     - All robots on the same network, and want to use ROS from another machine
   * - full (ROS2 default)
     - All in network
     - Just one robot on the network (or AP version)

These settings are mostly useful in a router setup, but is also good to know in a setup where
the robot acts as the access point (AP). The default in MIRTE is localhost. In that
way users not using ROS (eg secondary school MIRTE Pioneer teachers) can easily
connect all MIRTE robots to the same network. This default might only be not the 
preferred way for the more advanced users. They should be able to modify the 
settings to their needs.

The settings are stored in ~/.mirte_settings.sh. These are already sourced in your
~/.bashrc, and also sourced when starting the mirte-ros systemd service. After changing
these settings, you should restart the mirte-ros service, and open a new terminal. Or 
just reboot.

.. tabs::

  .. tab:: localhost (MIRTE default)

    In this setup, only the robot itself is able to discover nodes.

    .. tabs::

       .. group-tab:: Router

         .. image:: ./_images/ros2_communication_router_localhostonly.svg

       .. group-tab:: AP (MIRTE default)

         .. image:: ./_images/ros2_communication_ap_localhostonly.svg

    On the MIRTE robot in ~/.mirte_settings.sh:

    .. code-block:: bash

      export MIRTE_ZENOH=false
      export ROS_LOCALHOST_ONLY=1

    For this to take effect, you need to restart ROS.

  .. tab:: zenoh

    This is a setup comparable with the ROS master in ROS1.

    .. tabs::

       .. group-tab:: Router

         .. image:: ./_images/ros2_communication_router_zenoh.svg

       .. group-tab:: AP (MIRTE default)

         .. image:: ./_images/ros2_communication_ap_zenoh.svg

    On the MIRTE robot in ~/.mirte_settings.sh:

    .. code-block:: bash

      export MIRTE_ZENOH=true
      export ROS_LOCALHOST_ONLY=0

    For this to take effect, you need to restart ROS.
    And on your own machine, you should have the mirte-zenoh-setup 
    package installed (which should install ros-humble-rmw-zenoh-cpp
    when using rosdep), and start it with: 

    .. code-block:: bash

      $ ros2 run rmw_zenoh_cpp rmw_zenohd

    And in another terminal source your workspace with the right IP
    address:

    .. code-block:: bash

      $ export MIRTE_ZENOH=<mirte_ip>
      $ source install/setup.bash


  .. tab:: full

    This is the default setup for a fresh ROS2 installation.

    .. tabs::

       .. group-tab:: Router

         .. image:: ./_images/ros2_communication_router_fulldiscovery.svg

       .. group-tab:: AP (MIRTE default)

         .. image:: ./_images/ros2_communication_ap_fulldiscovery.svg

    On the MIRTE robot in ~/.mirte_settings.sh:

    .. code-block:: bash

      export MIRTE_ZENOH=false
      export ROS_LOCALHOST_ONLY=0

    For this to take effect, you need to restart ROS.

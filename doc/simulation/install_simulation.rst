Installation
############

.. note:: 

   We currently only have a Gazebo Classic simulation of the MIRTE robots.

The simulation will not run on the MIRTE robot, but on your own machine.
We assume you have ros-humble-base installed. To get the simulation up and
running you need to install a couple of packages in your ROS2 workspace
(eg ~/ros2_ws/):

.. code-block:: bash

   $ git clone https://github.com/mirte-robot/mirte-gazebo src
   $ vcs import src/ < src/mirte-gazebo/sources.repos

Optionally, you can remove the unused ROS packages. This will make the 
install, and build go much faster. Only do this as long as you have no 
changes in these folders.

.. code-block:: bash

   $ cd src/mirte_ros_packages
   $ rm -r mirte_bringup/ mirte_telemetrix_cpp/ mirte_teleop/ mirte_test/ mirte_zenoh_setup/
   $ cd ../..

And finally install the dependencies and build everyting:

.. code-block:: bash

   $ rosdep install --from-paths src --ignore-src -r -y
   $ colcon build --symlink-install
   $ source install/setup.bash





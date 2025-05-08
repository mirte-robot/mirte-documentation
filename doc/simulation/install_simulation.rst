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
   $ cd src/mirte_ros_packages
   $ shopt -s extglob
   $ rm -rf !("mirte_msgs"|"mirte_control"|"mirte_description"|"mirte_moveit_config")
   $ cd ../..

And finally install the dependencies and build everyting:

.. code-block:: bash

   $ rosdep install --from-paths src --ignore-src -r -y
   $ colcon build --symlink-install
   $ source install/setup.bash





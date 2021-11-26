Mirte Development
#################

As mentioned before we are currently still developing Mirte. But the ultimate goal is to have a vibrant
community contributing to the project.

.. warning::
   Currently none of the interfaces (hardware, software) are definitive. This means that we might still
   change this. Developing educational material around Mirte is possible, but you should be able to
   modify this in case we change the interfaces.


Software architecture
=====================

As the robot is meant for education, most of the design decisions we made were made with that in mind. This
means we were forced to make decisions in the speed vs usability (/learnability) tradeoff and decided to go
for the learnability over speed. We this improving speed should, at some point, be done by the students
themselves.

.. tabs::

   .. tab:: Overall

      .. image:: images/architecture_full.png
        :width: 600
        :alt: Full Software Architecture

      Full architecture overview of the Mirte software. Repositories are shown in red, ROS nodes in blue, and
      systemd services in green. More explanation can be found in the corresponding tabs. The dataflow is
      shown with arrows and will be explained in the next section.

   .. tab:: Repositories

      .. image:: images/architecture_repos.png
        :width: 600
        :alt: Overview of software repositories.

      The software of Mirte is stored in multiple repositories on `github <https://github.com/mirte-robot>`_, 
      but can also be found on the Mirte robot in /usr/local/src/mirte. 
 
      - `mirte-web-interface <https://github.com/mirte-robot/mirte-web-interface>`_: Is the repository 
        where the Vue frontend and nodeJS backend are stored. They are in one repository since they are 
        frequently updated together.
      - `mirte-python <https://github.com/mirte-robot/mirte-python>`_: Contains the python API of the
        sensors and actuators. This basically is a wrapper around the ROS topics and services for all
        the sensors and actuators.
      - `mirte-ros-packages <https://github.com/mirte-robot/mirte-ros-packages>`_: Contains the ROS packages
        to communicate with the hardware (MCU, PS controller, camera, etc) and the differential drive controller.
      - `mirte-telemetrix-aio <https://github.com/mirte-robot/mirte-telemetrix-aio>`_: Is a fork of
        telemetrix-aio to also support our own wheel encoder library (needed to get the interrupts of the encoder).
      - `mirte-telemetrix4Arduino <https://github.com/mirte-robot/mirte-telemetrix4Arduino>`_: Is a fork 
        of telemetrix4Arduino to also add support for the wheel encoder.
      - `mirte-arduino-libraries <https://github.com/mirte-robot/mirte-arduino-libraries>`_: Contains the
        implementation of our own wheel encoder.
      - `mirte-oled-images <https://github.com/mirte-robot/mirte-oled-images>`_: Contains the images and
        image sequences to show on the OLED.
      - `mirte-install-scripts <https://github.com/mirte-robot/mirte-install-scripts>`_: Contains all scripts
        needed to install the Mirte software on the robot. This includes our own repositories and dependencies,
        but also creates a user and enables the Wifi AP and systemd services.
      - `mirte-sd-image-tools <https://github.com/mirte-robot/mirte-sd-image-tools>`_: Contains all things 
        needed to build an ARM sd card image with everything installed from the mirte-install-scripts repo 
        for both the Orange Pi Zero (Armbian Ubuntu) and Raspberry Pi (Ubuntu). 


   .. tab:: ROS nodes

      .. image:: images/architecture_nodes.png
        :width: 600
        :alt: Overview of ROS nodes.

      A couple of ROS nodes are used to control the robot (please note that the default for ROS packages
      are underscores):

      - **mirte_telemetrix**: This node initializes the telemetrix-aio pins based on the settings in the ROS
        parameter server. Each actuator will create a corresponding service. Each sensor will create
        both a service and a topic.
      - **mirte_control**: This is the ROS control wrapper for a differential drive robot. ROS control
        will already account for the kinematics from Twist message to rad/s per wheel. This rad/s per
        wheel is then transformed to speed (range -100 to 100) of the robot. 
      - **mirte_teleop**: This can be the teleop-key or teleop-joy node. In both cases the input from the
        device will be transformed into a Twist message.
      - **robot.py**: The robot.py node is included in the user defined python script. When run, this will
        start as a node as well. This node is only active when the user runs their script.
 

   .. tab:: Systemd

      .. image:: images/architecture_systemd.png
        :width: 600
        :alt: Systemd services.

      In order to start all needed software on boot there are 3 systemd services activated:

      - **mirte-ap**: Service which starts the wifi-connect software. This will bring up a Wifi AP when
        no connection to a known network can be established. Otherwise it will connect to the known
        router. This service is executed as root.
      - **mirte-web-interface**: Service starts the web interface backend. The backend will also serve
        the frontend built by VueJS. This service is executed as the mirte user.
      - **mirte-ros**: Service will bringup ROS by launching minimal.launch.  This service is executed 
        as the mirte user.
      - **mirte-jupyter**: Service will start Jupyter Notebook which can be accessed on port 8888.

      All of them will start at boot, but can also be stopped:

      .. code-block:: bash

         mirte$ sudo service mirte-ros stop

      , started:

      .. code-block:: bash

         mirte$ sudo service mirte-ros start

      , or inspected:

      .. code-block:: bash

         mirte$ sudo journalctl -u mirte-ros -f



Software flows
==============


.. tabs::

   .. tab:: Settings

      .. image:: images/architecture_settings.png
        :width: 600
        :alt: Settings flow.


      Like described earlier there are some things that you need to set before you can use the
      robot. This involves both uploading telemetrix to the MCU, and defining the connected
      hardware. Both can be done via commandline and web interface.

      When uploading telemetrix to the MCU from the web interface, a request will be sent to 
      the backend to execute the same command as you would execute when in a terminal.

      When a user changes the settings in the web interface a YAML file is generated and uploaded 
      via the backend to the robot. This will overwrite the mirte_user_config.yaml file and 
      overwrite the parameters in the running parameter server. The backend will also stop the 
      running telemetrix node and restart it so the initialization will be done again with the new 
      parameters. By restarting the telemetrix node, this node will get the new settings from
      the parameter server and initialize this using mirte-telemetrix-aio which will apply it
      on the MCU with mirte-telemetrix4Arduino.

      You can also connect to your own wifi. Whe doing this from the web interface, it will
      communicate the change right away to the wifi-connect server which will use NetworkManager
      accordingly.

      .. note::

         In the current implementation the YAML config is generated in the web interface
         and uploaded to the robot through the backend. We will redesign this in the future
         and implement a version where the web interface will communicate via roslibjs and
         therefore also be able to reflect the settings as they are.

      .. note::

         Usually one does not change the parameters within a running ROS system. We do think
         that these kind of settings belong to the parameter server since they usually do not
         change. In this educational robot we try to also make it easy to modify your robot.


   .. tab:: Sensors

      .. image:: images/architecture_sensors.png
        :width: 600
        :alt: Sensor data flow.

      Sensordata are read continuously in telemetrix (with a preset frequency). They are then
      communicated over USB from the MCU via mirte-telemetrix4Arduino to mirte-telemetrix-aio.
      The ROS node ROS_telemetrix_api.py from mirte_telemetrix will read these values as they
      get in via the callback from mirte-telemetrix-aio. They will then be published as a topic,
      and the last value is stored in order to be returned by a service call. These sensor
      values will the be send to the webinterface via roslibjs.


   .. tab:: Actuators

      .. image:: images/architecture_actuators.png
        :width: 600
        :alt: Actuator data flow.

      When a user changes the actuator values in the web interface this will be communicated to
      the ROS_telemetrix_api.py node from mirte-telemetrix-aio (or to mirte-control in case 
      a Twist message is generated to drive around). The ROS_telemetrix_api.py node will the
      call the corresponding mirte-telemetrix-aio function which will pass this to 
      mirte-telemetrix4Arduino on the MCU.


   .. tab:: Python

      .. image:: images/architecture_programming_python.png
        :width: 600
        :alt: Python programming flow.

      TODO

   .. tab:: Blockly

      .. image:: images/architecture_programming_blockly.png
        :width: 600
        :alt: Blockly programming flow.

      TODO


Building a custom SD image
==========================

The latest image can be downloaded from `the download site <http://dl.mirte.org>`_. For university
or maker level this might not fully do what you want in your course. In that case you can modify
the image yourself and add software or default settings. This can be done with the mirte-sd-image-tools.
Note that this can onlu be done on Linux machines.

1. Checkout the mirte-sd-image-tools:

   .. code-block:: bash

      $ git clone https://github.com/mirte-robot/mirte-sd-image-tools
      $ cd mirte-sd-image-tools

2. Install the prerequisites (`singularity container <https://sylabs.io/guides/3.0/user-guide/installation.html#install-the-debian-ubuntu-package-using-apt>`_ ) 
   preferably via apt.

3. Build the singularity image:

   .. code-block:: bash

      $ ./install.sh

4. Rename your downloaded version to mirte_orangepi_sd.img or mirte_raspberrypi_sd.img:

   .. code-block:: bash

      $ mv mirte_<timestamp>_orangepi_sd.img mirte_orangepi_sd.img

5. Resize the image to make space for extra software:

   .. code-block:: bash

      $ sudo singularity run --app prepare_image --bind ./mirte_orangepi_sd.img:/mirte_sd.img image_tools.sif

6. Chroot into the sd image:

   .. code-block:: bash

      $ ./run.sh image_shell orangepi

7. Run any command you think is needed to modify your image and exit when done.

8. You can shrink and xz the image again for distribution:

   .. code-block:: bash

      $ sudo singularity run --app shrink_image --bind ./mirte_orangepi_sd.img:/mirte_sd.img image_tools.sif
      $ xz -vT6 ./mirte_orangepi_sd.img




Development for Web Interface
=============================

Developing the Vue frontend on the orangepi might be tricky due to the limited RAM of the 
SBC. It therefore is advised to checkout the mirte-web-interface on your own machine
and develop there:

.. code-block:: bash

   $ git clone https://github.com/mirte-robot/mirte-web-interface
   $ cd mirte-web-interface
   $ sudo apt install -y python3-pip python3-setuptools python3-wheel
   $ sudo -H pip install nodeenv
   $ nodeenv --node=16.2.0 node_env
   $ source node_env/bin/activate
   (node_env)$ npm install .
   (node_env)$ npm serve

You can now access the web interface on http::/localhost:4000. Since this is running locally
on your machine. Not everything might be working (eg. the connection to ROS). You can therefore
also build the frontend locally and upload it to the robot:

.. code-block:: bash

   $ npm run build && ssh mirte@mirte.local "rm -rf /usr/local/src/mirte/mirte_web_interface/vue-frontend/dist" && scp -r dist/ mirte@mirte.local:/usr/local/src/mirte/mirte_web_interface/vue-frontend




Adding another language
=======================

Multi lingual support is only available in the web interface and tutorials. We think children should
learn technology in their own language instead of having to learn a foreign language at the same time. 
At some point we do think students should be able to use English as a language to learn more about
technology. 

The main language is English and can be found the `frontend <https://github.com/mirte-robot/mirte-web-interface/vue-frontend/locales/en.json>`_ 
code. Adding a language can be as simple as a pull request with another json file.

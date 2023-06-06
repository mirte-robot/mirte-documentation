Mirte Development
#################

As mentioned before we are currently still developing Mirte. But the ultimate goal is to have a vibrant
community contributing to the project.

.. warning::
   Currently none of the interfaces (hardware, software) are definitive. This means that we might still
   change this. Developing educational material around Mirte is possible, but you should be able to
   modify this in case we change the interfaces.


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

You can now access the web interface on http://localhost:4000. Since this is running locally
on your machine. Not everything might be working (eg. the connection to ROS). You can therefore
also build the frontend locally and upload it to the robot:

.. code-block:: bash

   $ npm run build && ssh mirte@mirte.local "rm -rf /usr/local/src/mirte/mirte-web-interface/vue-frontend/dist" && scp -r dist/ mirte@mirte.local:/usr/local/src/mirte/mirte-web-interface/vue-frontend




Adding another language
=======================

Multi lingual support is only available in the web interface and tutorials. We think children should
learn technology in their own language instead of having to learn a foreign language at the same time. 
At some point we do think students should be able to use English as a language to learn more about
technology. 

The main language is English and can be found the `frontend <https://github.com/mirte-robot/mirte-web-interface/blob/main/vue-frontend/locales/en.json>`_ 
code. Adding a language can be as simple as a pull request with another json file.

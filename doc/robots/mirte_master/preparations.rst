Preparations
############

Before you can assemble the robot it makes sense to prepare some parts.


MIRTE PCB
---------

.. carousel::
   :show_controls:
   :show_fade:
   :show_buttons_on_top:
   :show_captions_below:

   .. figure:: _images/build_instructions/pcb_step_1.jpg
   .. figure:: _images/build_instructions/pcb_step_2.jpg

       ..

       Solder the step-down onto the PCB. Make sure to have it in the
       right direction.

   .. figure:: _images/build_instructions/pcb_step_3.jpg
   
       ..

       Cut 30 cm of cable.

   .. figure:: _images/build_instructions/pcb_step_4.jpg

       ..

       Put the cable through the holes. Make sure the colors are on the
       correct side.

   .. figure:: _images/build_instructions/pcb_step_5.jpg

       ..

       Strip the ends.

   .. figure:: _images/build_instructions/pcb_step_6.jpg

       ..

       And solder the spring contacts.

   .. figure:: _images/build_instructions/pcb_step_7.jpg

       ..

       Put the spring contacts in place and tighten the cable.

   .. figure:: _images/build_instructions/pcb_step_8.jpg
   .. figure:: _images/build_instructions/pcb_step_9.jpg

       ..

       Add the ferrules in order to finish the battery cap.

   .. figure:: _images/build_instructions/pcb_step_10.jpg

       ..

       Attach the battery cap to the PCB.

   .. figure:: _images/build_instructions/pcb_step_11.jpg
   .. figure:: _images/build_instructions/pcb_step_12.jpg

       ..

       Remove the green wire using a flat screwdriver.

   .. figure:: _images/build_instructions/pcb_step_13.jpg
   .. figure:: _images/build_instructions/pcb_step_14.jpg

       ..

       Notice the "NC" an "C" labels on the plug.

   .. figure:: _images/build_instructions/pcb_step_15.jpg

       ..

       And make sure to put the "NC" label where the green cable was.

   .. figure:: _images/build_instructions/pcb_step_16.jpg
   .. figure:: _images/build_instructions/pcb_step_17.jpg

       ..

       Add ferrules to the yellow and white wire.

   .. figure:: _images/build_instructions/pcb_step_19.jpg

       ..

       And connect the button wires to the PCB as seen in the picture.

   .. figure:: _images/build_instructions/pcb_step_20.jpg
   .. figure:: _images/build_instructions/pcb_step_21.jpg

       ..

       Add the blade fuse.

   .. figure:: _images/build_instructions/pcb_step_22.jpg
   .. figure:: _images/build_instructions/pcb_step_23.jpg

       ..

       Add the Raspberry Pi Pico.

   .. figure:: _images/build_instructions/pcb_step_24.jpg
   .. figure:: _images/build_instructions/pcb_step_25.jpg
 
       ..

       The PCB is already capable of having an emergency button attached. We do
       not use this yet. So we need to short this for now.


Servo settings
--------------

Before assembling the arm, please make sure that the servo's have the correct ID,
and are positioned in their 0 state. In order to do so, we have created a script 
that does this for each servo.

Each servo needs to be set seperately (so the servos can not be connected/daisy chained
with eachother). For this setup you should upload the right uf2 to the Raspberry Pi Pico,
You should now add the switch and the battery mount to the MIRTE PCB as on the 
picture below.

.. list-table::
   :header-rows: 1

   * - Servo
     - Type
     - ID
     - uf2
   * - Rotation
     - HX-12H
     - 2
     - `set_servo2.uf2 <https://github.com/ArendJan/mirte_set_serial_servos/releases/download/v1/set_servos2.uf2>`_
   * - Shoulder
     - HTD-45H
     - 3
     - `set_servo3.uf2 <https://github.com/ArendJan/mirte_set_serial_servos/releases/download/v1/set_servos3.uf2>`_
   * - Elbow
     - HTD-35H
     - 4
     - `set_servo4.uf2 <https://github.com/ArendJan/mirte_set_serial_servos/releases/download/v1/set_servos4.uf2>`_
   * - Wrist
     - HX-12H
     - 5
     - `set_servo5.uf2 <https://github.com/ArendJan/mirte_set_serial_servos/releases/download/v1/set_servos5.uf2>`_
   * - Gripper
     - HX-12H
     - 6
     - `set_servo6.uf2 <https://github.com/ArendJan/mirte_set_serial_servos/releases/download/v1/set_servos6.uf2>`_

The steps you need to take for each servo are:

1) Upload the right uf2 to the Pico
2) Connect the servo to the PCB
3) Turn on the PCB by pressing the switch
4) Check if you saw the servo moving and/or validate by connecting the Pico to a (linux) pc 
   and read from serial: ``$ tio -b 115200 /dev/ttyACM0``

.. tip::

   When assembling multiple MIRTE Masters at once it makes sense to set all the servos 
   with the same ID. 


DC motor alignment
------------------

In order to assembe the MIRTE Master correctly, we need to maek sure that
the connector on the motor is roughtly on the same orentation as the motor
shaft. Unfortunately, not all motors have this setup. So for some we need
to change this orientation by rotating the gearbox.

.. carousel::
   :show_controls:
   :show_fade:
   :show_buttons_on_top:
   :show_captions_below:

   .. figure:: _images/build_instructions/motors_step_1.jpg

       ..

       Orient the motors with their shaft down.

   .. figure:: _images/build_instructions/motors_step_2.jpg

       ..

       Depending on your motors, you need to reorientate the shaft location.
       In this picture, only the left one is correct. The others need to be
       changed.

   .. figure:: _images/build_instructions/motors_step_3.jpg

       ..

       Carefully disasseble the metal cover. The gearbox consists of all
       loose elements. Make sure to take the cover up as straight as 
       possible.

   .. figure:: _images/build_instructions/motors_step_4.jpg

       ..

       Carefully remove the geabox, and unscrew the last plate.

   .. figure:: _images/build_instructions/motors_step_5.jpg

       ..

       Put the gearbox back on the plate, and try to turn the plate/gearbox
       combo until it is roughtly in the right direction, and the screws of
       the plate are aligned with holes.

   .. figure:: _images/build_instructions/motors_step_7.jpg

       ..

       Fix the plate in the right orientation.

   .. figure:: _images/build_instructions/motors_step_8.jpg

       ..

       Put back the gearbox. Especially the brass stands might have misaligned
       a bit while doing so. Make sure to wobble the geabox carefully in order
       to realign the gearbox.

   .. figure:: _images/build_instructions/motors_step_9.jpg
   .. figure:: _images/build_instructions/motors_step_10.jpg

       ..

       Reattach the cover.

   .. figure:: _images/build_instructions/motors_step_11.jpg

       ..

       All motors should have their connector roughly on the same side as the shaft.
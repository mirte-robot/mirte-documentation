Hardware specs
##############

The MIRTE Master was designed to be the upgraded bigger brother of the MIRTE Pioneer. With
this the students can focus more on robot applications rather than the inner workings of
the robot. Like with the MIRTE Pioneer, we tried to minimize the number of custom components. 

With the MIRTE Master you can decide to build just the mobile base, the manipulator arm, or
both. Please find below the components you need for these.

.. warning::

   Currently we have only built the base, and both. The standalone arm is not yet finished.

.. warning::

   The hardes part to get your hands on is probably the custom MIRTE PCB. We will have a look
   at finding ways to easily order these. Ideas are more than welcome. For now, do not hesitate
   to contact us on `discord <https://discord.gg/T54MZTberQ>`_ to get discuss instructions.


.. list-table::
   :widths: 5 5 5 35 50
   :header-rows: 1

   * - base 
     - arm
     - both
     - component
     - type
   * - 1
     - 1
     - 1
     - Computer
     - `Orange Pi 3B v2.1 <http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-3B.html>`_
   * - 1
     - 1
     - 1
     - eMMC (optional)
     - 32GB eMMC
   * - 1
     - 1
     - 1
     - micro SD card
     - Intenso 16Gb (class 10) micro SD card
   * - 1
     - 1
     - 1
     - Microcontroller
     - `Raspberry Pi Pico H (RP2040) <https://www.raspberrypi.com/products/raspberry-pi-pico/>`_
   * - 1
     - 1
     - 1
     - MIRTE Master PCB
     - `MIRTE Master main control PCB <https://github.com/ArendJan/mirte-pcb/tree/v3_mirte_master>`_   
   * - 1
     - 1
     - 1
     - OLED Screen
     - `white SSD1306 128x64 I2C <https://nl.aliexpress.com/item/1005007755490093.html>`_
   * - 4
     - 0
     - 4 
     - DC motors (incl encoders)
     - `12V 107RPM JGB37-520 <https://nl.aliexpress.com/item/1005005021902364.html>`_
   * - 1
     - 0
     - 1
     - Mecanum wheel (set of 4)
     - `97mm (2 left, 2 right) <https://nl.aliexpress.com/item/1005007533099560.html>`_ [#f1]_
   * - 1
     - 0
     - 1
     - Depth Camera
     - `Orbbec Astra Mini Pro <https://www.orbbec.com/products/structured-light-camera/astra-series/>`_
   * - 1
     - 0
     - 1
     - 2D Lidar
     - `Slamtec rplidar C1 <https://www.seeedstudio.com/RPLiDAR-C1M1-R2-Portable-ToF-Laser-Scanner-Kit-12M-Range-p-5840.html>`_
   * - 2 
     - 0
     - 2
     - Ultrasonic sensor
     - `HC-SR04 <https://nl.aliexpress.com/item/32283526790.html>`_
   * - 1
     - 0
     - 1
     - IMU
     - `MPU-9250 <https://nl.aliexpress.com/item/1005009122504274.html>`_
   * - 0
     - 3
     - 3
     - 12KG.CM Servo
     - `HX-12H (12KG.CM) Servo <https://www.hiwonder.com/products/hx-12h>`_
   * - 0
     - 1
     - 1
     - 35KG.CM Servo
     - `HTD-35H (35KG.CM) Servo <https://www.hiwonder.com/products/htd-35h>`_
   * - 0
     - 1
     - 1
     - 45KG.CM Servo
     - `HTD-45H (45KG.CM) Servo <https://www.hiwonder.com/products/htd-45h>`_ 
   * - 0
     - 1
     - 1
     - Ball bearing
     - `6812 2RS <https://nl.aliexpress.com/item/1005007420073930.html>`_
   * - 0
     - 1
     - 1
     - USB camera
     - `OV9726 <https://nl.aliexpress.com/item/1005008554975902.html>`_

Electronic components
---------------------

.. list-table::
   :widths: 5 5 5 35 50
   :header-rows: 1

   * - base
     - arm
     - both
     - component
     - type
   * - 1
     - 1
     - 1
     - switch
     - `switch <https://www.tinytronics.nl/nl/schakelaars/manuele-schakelaars/drukknoppen-en-schakelaars/metalen-drukknop-16mm-reset-met-3v-blauwe-led-verlichting>`_
   * - 1
     - 1
     - 1
     - 12-5V step down
     - `12-5V step down <https://nl.aliexpress.com/item/1005006721587257.html>`_
   * - 1
     - 1
     - 1
     - 5A Blade fuse
     - `5A Blade fuse <https://nl.rs-online.com/web/p/car-fuses/7874108>`_
   * - 1
     - 0
     - 1
     - battery
     - `Parkside Performance 12V, 5Ah <https://www.lidl.nl/p/parkside-performance-accu-12-v-5-ah/p100396693>`_

   * - 1
     - 0
     - 1
     - Spring contact
     - `Spring contact <https://nl.rs-online.com/web/p/grounding-contacts/7884880>`_
   * - 1
     - 0
     - 1
     - 20cm wire
     -
   * - 0
     - 1
     - 0
     - USB-C module
     - USB-C module

Cables
------

.. list-table::
   :widths: 5 5 5 35 50
   :header-rows: 1

   * - base
     - arm
     - both
     - component
     - usage
   * - 1
     - 1
     - 1
     - `JST XH cables 4 pins, double head, 10-20cm <https://nl.aliexpress.com/item/1005002179605258.html>`_
     - OLED screen
   * - 2
     - 1
     - 2
     - micro USB cable (USB A - USB B micro) 15 cm [#f2]_
     - Pico & RPLidar 
   * - 1
     - 1
     - 1
     - USB-C cable (USB A - USB C) 20 cm
     - Orange Pi 3B Power  
   * - 2
     - 0
     - 2
     - `JST XH cables 4 pins, double head, 30cm <https://nl.aliexpress.com/item/1005002179605258.html>`_
     - Ultrasonic sensor
   * - 2
     - 0
     - 2
     - `JST **PH** cable 6 pins, double head, 20cm <https://nl.aliexpress.com/item/1005006188790994.html>`_
     - DC front motors
   * - 2
     - 0
     - 2
     - `JST **PH** cable 6 pins, double head, 30cm <https://nl.aliexpress.com/item/1005006188790994.html>`_
     - DC rear motors


Mounting
--------

.. list-table::
   :widths: 5 5 5 35 50
   :header-rows: 1

   * - base
     - arm
     - both
     - component
     - usage
   * - 2
     - 2
     - 2
     - `standoff 10mm M2.5 female-female <https://nl.rs-online.com/web/p/standoffs/1842689>`_
     - Orange Pi 3B
   * - 0
     - 0
     - 4
     - `standoff 20mm M4 female-female <https://nl.rs-online.com/web/p/standoffs/1058094>`_
     - Middle and Top plate
   * - 4
     - 4
     - 4 
     - `standoff 25mm M4 female-female <https://nl.rs-online.com/web/p/standoffs/1058101>`_
     - MIRTE PCB
   * - 0
     - 3
     - 3
     - `standoff 40mm M3 male-female <https://nl.rs-online.com/web/p/standoffs/0221184>`_
     - Arm base
   * - 2
     - 0
     - 2
     - M2 x 20 screws
     - Orbbec Astra mount
   * - 2
     - 0
     - 2
     - M2 nut
     - Orbbec Astra mount
   * - 4
     - 4
     - 4
     - M2.5 x 6 screws
     - Orange Pi 3B
   * - ?
     - ?
     - 6
     - M2.5 x 12 screws
     - 
   * - ?
     - ?
     - 8
     - M2.5 locking washer
     - 
   * - ?
     - ?
     - 6
     - M2.5 washer (form a)
     - 
   * - ?
     - ?
     - 35
     - M3 x 12 screws
     - 
   * - ?
     - ?
     - 13
     - M3 x 16 screws
     - 
   * - ( 4 )
     - ( 0 )
     - ( 4 )
     - ,,
     - battery mount
   * - ?
     - ?
     - 6
     - M3 x 18 screws
     -
   * - ?
     - ?
     - 2
     - M3 x 20 screws
     -
   * - ?
     - ?
     - 4
     - M3 x 24 screws
     -  
   * - ?
     - ?
     - 2
     - M3 x 30 screws
     - 
   * - ?
     - ?
     - 23
     - M3 lock nut
     - 
   * - ?
     - ?
     - 3
     - M3 locking washer
     -
   * - ?
     - ?
     - 3
     - M3 washer (form a)
     - 
   * - ?
     - ?
     - 42
     - M4 x 12 screws
     - 
   * - ( 16 )
     - ( 0 )
     - ( 16 )
     - 
     - Base side panels
   * - ( 8 )
     - ( 8 )
     - ( 8 )
     - 
     - MIRTE PCB    
   * - ( 3 )
     - ( 0 )
     - ( 3 )
     - 
     - Lidar mount
   * - ( 0 )
     - ( 0 )
     - ( 8 )
     - 
     - Middle and Top plate standoffs   
   * - 19
     - 0
     - 19
     - M4 U-clip captive nut
     - 
   * - ( 16 )
     - ( 0 )
     - ( 16 )
     - 
     - Base side panels
   * - ( 3 )
     - ( 0 )
     - ( 3 )
     - 
     - Lidar mount  
   * - ?
     - ?
     - 8
     - M4 lock nut
     - 
   * - ?
     - ?
     - 8
     - M4 locking washer
     -
   * - ?
     - ?
     - 8
     - M4 washer (form a)
     -    



Lasercut parts
--------------

.. list-table::
   :widths: 5 5 5 85
   :header-rows: 1

   * - base
     - arm
     - both
     - component
   * - 1
     - 1
     - 1
     - `Bottom plate (3mm PMMA) <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Cut%20Files/Bottom_plate.DXF>`_
   * - 1
     - 0
     - 1
     - `Middle plate (3mm PMMA) <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Cut%20Files/Middle_plate.DXF>`_
   * - 1
     - 0
     - 1
     - `Top plate (3mm stainless steel) <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Cut%20Files/Top_plate.DXF>`_
   * - 0
     - 1
     - 1
     - `Arm Inner Bottom plate (3mm stainless steel) <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Cut%20Files/Arm_Inner_Bottom_Plate.DXF>`_
   * - 0
     - 1
     - 1
     - `Arm Inner Top plate (3mm stainless steel) <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Cut%20Files/Arm_Inner_Top_Plate.DXF>`_
   * - 0
     - 1
     - 1
     - `Arm Outer Bottom plate (3mm stainless steel) <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Cut%20Files/Arm_Outer_Bottom_Plate.DXF>`_
   * - 0
     - 1
     - 1
     - `Arm Outer Top plate (3mm stainless steel) <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Cut%20Files/Arm_Outer_Top_Plate.DXF>`_


3D printed parts
----------------

The original 3D printed parts are based on the components menstioned above. Since you might
want to modify your MIRTE Master based on our needs (or capability of stocking the components), 
you might need to (slightly) modify these.

These designs do not need support. The total amount of PLA needed for a mpobile manipulator
is roughly 1 kg.

.. list-table::
   :widths: 5 5 5 35 50
   :header-rows: 1

   * - base
     - arm
     - both
     - component
     - instructions
   * -
     -
     -
     - Base
     -
   * - 4
     - 4
     - 4
     - `Motor module <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Frame/motor_module.STEP>`_
     - 
   * - 1
     - 1
     - 1
     - `Left panel <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Frame/Left-Sidepanel-Module-OPI3Bv2.1.STEP>`_
     -   
   * - 1
     - 1
     - 1
     - `Right panel <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Frame/Right-Sidepanel-Module.STEP>`_
     -   
   * - 1
     - 1
     - 1
     - `Front panel <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Frame/Camera-Module%Astra.STEP>`_
     -   
   * - 1
     - 0
     - 1
     - `Left Sonar module <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Frame/Left-Sonar-Module.STEP>`_
     -   
   * - 1
     - 0
     - 1
     - `Right Sonar module <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Frame/Right-Sonar-Module.STEP>`_
     -   
   * - 1
     - 0
     - 1
     - `Battery module <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Frame/Battery-Module.STEP>`_
     -   
   * - 1
     - 0
     - 1
     - `Lidar module <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Frame/LiDar-Module.STEP>`_
     -   
   * - 1
     - 0
     - 1
     - `Battery mount <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Frame/Battery-Mount.STEP>`_
     -   
   * - 0
     - 0
     - 2
     - `Cable tube <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Frame/Cable-Tube.STEP>`_
     -   
   * -
     -
     -
     - Arm
     -
   * - 0
     - 1
     - 1
     - `Rotation Servo Mount <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Arm/ZRotation-Servo-Mount.STEP>`_
     - 
   * - 0
     - 1
     - 1
     - `Shoulder <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Arm/Shoulder.STEP>`_
     - 
   * - 0
     - 1
     - 1
     - `Forearm <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Arm/Forearm.STEP>`_
     - 
   * - 0
     - 1
     - 1
     - `Upperarm <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Arm/Upperarm.STEP>`_
     - 
   * - 0
     - 1
     - 1
     - `Wrist <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Arm/Wrist.STEP>`_
     - 
   * - 0
     - 1
     - 1
     - `Camera mount <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Arm/Camera-Mount.STEP>`_
     - 
   * -
     -
     -
     - Gripper
     -
   * - 0
     - 1
     - 1
     - `Top plate <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Gripper/plate_top_plate.STEP>`_
     - 
   * - 0
     - 1
     - 1
     - `Bottom plate <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Gripper/plate_bottom_plate.STEP>`_
     - 
   * - 0
     - 2
     - 2
     - `Link <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Gripper/link.STEP>`_
     - 
   * - 0
     - 1
     - 1
     - `Geared link <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Gripper/gearer%actuator%link.STEP>`_
     - 
   * - 0
     - 1
     - 1
     - `Geared actuated link <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Gripper/gearer%actuated%link.STEP>`_
     - 
   * - 0
     - 4
     - 4
     - `Spacer <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Gripper/front_spacer.STEP>`_
     - 
   * - 0
     - 1
     - 1
     - `Actuating link left <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Gripper/actuating%link%left%actuation%link.STEP>`_
     - 
   * - 0
     - 1
     - 1
     - `Actuating link right <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Gripper/actuating%link%right%actualtion_link.STEP>`_
     - 
   * - 0
     - 1
     - 1
     - `Left tip <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Gripper/tip_left_tip.STEP>`_
     - 
   * - 0
     - 1
     - 1
     - `Right tip <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Gripper/tip_right_tip.STEP>`_
     - 


.. [#f1] Although branded as 6mm, you still need to drill the adapter hole to 6mm for the motor shafts.

.. [#f2] Please check the actual USB type. Both the Raspberry Pi Pico and the RPLidar also have versions with USB-C.    
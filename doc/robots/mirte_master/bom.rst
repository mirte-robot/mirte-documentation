Bill of Materials
#################

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


.. tabs::

   .. group-tab:: Mobile base

      .. list-table::
        :widths: 5 45 50
        :header-rows: 1

        * - #
          - component
          - type
        * - 1
          - Computer
          - `Orange Pi 3B v2.1 <http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-3B.html>`_
        * - 1
          - eMMC (optional)
          - 32GB eMMC
        * - 1
          - micro SD card
          - Intenso 16Gb (class 10) micro SD card
        * - 1
          - Microcontroller
          - `Raspberry Pi Pico H (RP2040) <https://www.raspberrypi.com/products/raspberry-pi-pico/>`_
        * - 1
          - MIRTE Master PCB
          - `MIRTE Master main control PCB <https://github.com/ArendJan/mirte-pcb/tree/v3_mirte_master>`_   
        * - 1
          - OLED Screen
          - `white SSD1306 128x64 I2C <https://nl.aliexpress.com/item/1005007755490093.html>`_
        * - 4
          - DC motors (incl encoders)
          - `12V 107RPM JGB37-520 <https://nl.aliexpress.com/item/1005005021902364.html>`_
        * - 1
          - Mecanum wheel (set of 4)
          - `97mm (2 left, 2 right) <https://nl.aliexpress.com/item/1005007533099560.html>`_ [#f1]_
        * - 1
          - Depth Camera
          - `Orbbec Astra Mini Pro <https://www.orbbec.com/products/structured-light-camera/astra-series/>`_
        * - 1
          - 2D Lidar
          - `Slamtec rplidar C1 <https://www.seeedstudio.com/RPLiDAR-C1M1-R2-Portable-ToF-Laser-Scanner-Kit-12M-Range-p-5840.html>`_
        * - 2 
          - Ultrasonic sensor
          - `HC-SR04 <https://nl.aliexpress.com/item/32283526790.html>`_
        * - 1
          - IMU
          - `MPU-9250 <https://nl.aliexpress.com/item/1005009122504274.html>`_
        * - 1
          - Ethernet Extension cable
          - `Delock 25 cm <https://www.reichelt.com/nl/nl/shop/product/cat_6a_verlengkabel_s_ftp_zwart_0_25_m-317744>`_
        * - \-
          - 12KG.CM Servo
          - `HX-12H (12KG.CM) Servo <https://www.hiwonder.com/products/hx-12h>`_ [#f2]_
        * - \-
          - 35KG.CM Servo
          - `HTD-35H (35KG.CM) Servo <https://www.hiwonder.com/products/htd-35h>`_
        * - \-
          - 45KG.CM Servo
          - `HTD-45H (45KG.CM) Servo <https://www.hiwonder.com/products/htd-45h>`_ 
        * - \-
          - Ball bearing
          - `6812 2RS <https://nl.aliexpress.com/item/1005007420073930.html>`_
        * - \-
          - USB camera
          - `OV9726 <https://nl.aliexpress.com/item/1005008554975902.html>`_

   .. group-tab:: Mobile manipulator

     .. list-table::
        :widths: 5 45 50
        :header-rows: 1

        * - #
          - component
          - type
        * - 1
          - Computer
          - `Orange Pi 3B v2.1 <http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-3B.html>`_
        * - 1
          - eMMC (optional)
          - 32GB eMMC
        * - 1
          - micro SD card
          - Intenso 16Gb (class 10) micro SD card
        * - 1
          - Microcontroller
          - `Raspberry Pi Pico H (RP2040) <https://www.raspberrypi.com/products/raspberry-pi-pico/>`_
        * - 1
          - MIRTE Master PCB
          - `MIRTE Master main control PCB <https://github.com/ArendJan/mirte-pcb/tree/v3_mirte_master>`_   
        * - 1
          - OLED Screen
          - `white SSD1306 128x64 I2C <https://nl.aliexpress.com/item/1005007755490093.html>`_
        * - 4
          - DC motors (incl encoders)
          - `12V 107RPM JGB37-520 <https://nl.aliexpress.com/item/1005005021902364.html>`_
        * - 1
          - Mecanum wheel (set of 4)
          - `97mm (2 left, 2 right) <https://nl.aliexpress.com/item/1005007533099560.html>`_ [#f1]_
        * - 1
          - Depth Camera
          - `Orbbec Astra Mini Pro <https://www.orbbec.com/products/structured-light-camera/astra-series/>`_
        * - 1
          - 2D Lidar
          - `Slamtec rplidar C1 <https://www.seeedstudio.com/RPLiDAR-C1M1-R2-Portable-ToF-Laser-Scanner-Kit-12M-Range-p-5840.html>`_
        * - 2 
          - Ultrasonic sensor
          - `HC-SR04 <https://nl.aliexpress.com/item/32283526790.html>`_
        * - 1
          - IMU
          - `MPU-9250 <https://nl.aliexpress.com/item/1005009122504274.html>`_
        * - 1
          - Ethernet Extension cable
          - `Delock 25 cm <https://www.reichelt.com/nl/nl/shop/product/cat_6a_verlengkabel_s_ftp_zwart_0_25_m-317744>`_
        * - 3
          - 12KG.CM Servo
          - `HX-12H (12KG.CM) Servo <https://www.hiwonder.com/products/hx-12h>`_ [#f2]_
        * - 1
          - 35KG.CM Servo
          - `HTD-35H (35KG.CM) Servo <https://www.hiwonder.com/products/htd-35h>`_
        * - 1
          - 45KG.CM Servo
          - `HTD-45H (45KG.CM) Servo <https://www.hiwonder.com/products/htd-45h>`_ 
        * - 1
          - Ball bearing
          - `6812 2RS <https://nl.aliexpress.com/item/1005007420073930.html>`_
        * - 1
          - USB camera
          - `OV9726 <https://nl.aliexpress.com/item/1005008554975902.html>`_


Electronic components
---------------------

.. tabs::

   .. group-tab:: Mobile base

      .. list-table::
        :widths: 5 45 50
        :header-rows: 1

        * - #
          - component
          - type
        * - 1
          - switch
          - `switch <https://www.tinytronics.nl/nl/schakelaars/manuele-schakelaars/drukknoppen-en-schakelaars/metalen-drukknop-16mm-reset-met-3v-blauwe-led-verlichting>`_
        * - 1
          - 12-5V step down
          - `12-5V step down <https://nl.aliexpress.com/item/1005006721587257.html>`_
        * - 1
          - 5A Blade fuse
          - `5A Blade fuse <https://nl.rs-online.com/web/p/car-fuses/7874108>`_
        * - 1
          - battery
          - `Parkside Performance 12V, 5Ah <https://www.lidl.nl/p/parkside-performance-accu-12-v-5-ah/p100396693>`_
        * - 1
          - Spring contact
          - `Spring contact <https://nl.rs-online.com/web/p/grounding-contacts/7884880>`_
        * - 1
          - 20cm wire
          -

   .. group-tab:: Mobile manipulator

      .. list-table::
        :widths: 5 45 50
        :header-rows: 1

        * - #
          - component
          - type
        * - 1
          - switch
          - `switch <https://www.tinytronics.nl/nl/schakelaars/manuele-schakelaars/drukknoppen-en-schakelaars/metalen-drukknop-16mm-reset-met-3v-blauwe-led-verlichting>`_
        * - 1
          - 12-5V step down
          - `12-5V step down <https://nl.aliexpress.com/item/1005006721587257.html>`_
        * - 1
          - 5A Blade fuse
          - `5A Blade fuse <https://nl.rs-online.com/web/p/car-fuses/7874108>`_
        * - 1
          - battery
          - `Parkside Performance 12V, 5Ah <https://www.lidl.nl/p/parkside-performance-accu-12-v-5-ah/p100396693>`_

        * - 1
          - Spring contact
          - `Spring contact <https://nl.rs-online.com/web/p/grounding-contacts/7884880>`_
        * - 1
          - 20cm wire
          -


Cables
------

.. tabs::

   .. group-tab:: Mobile base

      .. list-table::
        :widths: 5 45 50
        :header-rows: 1

        * - #
          - component
          - usage
        * - 1
          - `JST XH cables 4 pins, double head, 10-20cm <https://nl.aliexpress.com/item/1005002179605258.html>`_
          - OLED screen
        * - 2
          - micro USB cable (USB A - USB B micro) 15 cm [#f3]_
          - Pico & RPLidar 
        * - 1
          - USB-C cable (USB A - USB C) 20 cm
          - Orange Pi 3B Power  
        * - 2
          - `JST XH cables 4 pins, double head, 30cm <https://nl.aliexpress.com/item/1005002179605258.html>`_
          - Ultrasonic sensor
        * - 2
          - `JST **PH** cable 6 pins, double head, 20cm <https://nl.aliexpress.com/item/1005006188790994.html>`_
          - DC front motors
        * - 2
          - `JST **PH** cable 6 pins, double head, 30cm <https://nl.aliexpress.com/item/1005006188790994.html>`_
          - DC rear motors

   .. group-tab:: Mobile manipulator

      .. list-table::
        :widths: 5 45 50
        :header-rows: 1

        * - #
          - component
          - usage
        * - 1
          - `JST XH cables 4 pins, double head, 10-20cm <https://nl.aliexpress.com/item/1005002179605258.html>`_
          - OLED screen
        * - 2
          - micro USB cable (USB A - USB B micro) 15 cm [#f3]_
          - Pico & RPLidar 
        * - 1
          - USB-C cable (USB A - USB C) 20 cm
          - Orange Pi 3B Power  
        * - 2
          - `JST XH cables 4 pins, double head, 30cm <https://nl.aliexpress.com/item/1005002179605258.html>`_
          - Ultrasonic sensor
        * - 2
          - `JST **PH** cable 6 pins, double head, 20cm <https://nl.aliexpress.com/item/1005006188790994.html>`_
          - DC front motors
        * - 2
          - `JST **PH** cable 6 pins, double head, 30cm <https://nl.aliexpress.com/item/1005006188790994.html>`_
          - DC rear motors

Mounting
--------

.. tabs::

   .. group-tab:: Mobile base

      .. list-table::
        :widths: 5 40 5 50
        :header-rows: 1

        * - #
          - component
          - #
          - usage
        * - 2
          - `standoff 10mm M2.5 female-female <https://nl.rs-online.com/web/p/standoffs/1842689>`_
          -
          - Orange Pi 3B to bottom plate
        * - 4
          - `standoff 25mm M4 female-female <https://nl.rs-online.com/web/p/standoffs/1058101>`_
          -
          - MIRTE PCB to bottom plate
        * - \-
          - `standoff 20mm M4 female-female <https://nl.rs-online.com/web/p/standoffs/1058094>`_
          -
          - Middle to top plate
        * - \-
          - `standoff 40mm M3 male-female <https://nl.rs-online.com/web/p/standoffs/0221184>`_
          -
          - Arm base to top plate
        * - 2
          - M2 x 20 screws
          -
          - Orbbec Astra Mini Pro to camera module
        * - 2
          - M2 nut
          -
          - Orbbec Astra Mini Pro to camera module
        * - 8
          - M2.5 x 6 screws
          -
          - 
        * - 
          - ,,
          - 4
          - Orange Pi 3B to bottom plate
        * - 
          - ,,
          - 4
          - Lidar to lidar mount
        * - \-
          - M2.5 x 12 screws
          -
          - Shoulder print to inner arm plate
        * - 4
          - M2.5 spring washer
          -
          - Orange Pi 3B to bottom plate
        * - 4
          - M2.5 washer (form a)
          -
          - Orange Pi 3B to bottom plate
        * - \-
          - M3 x 6 screws
          -
          - 
        * -
          - ,,
          - \-
          - Horn to rotation Servo
        * -
          - ,,
          - \-
          - USB camera to camera module
        * - 14
          - M3 x 12 screws
          -
          - 
        * - 
          - ,,
          - 2
          - Ethernet port to side panel
        * - 
          - ,,
          - 12
          - DC motor to motor module (3 per motor)
        * - \-
          - M3 x 14 screws
          -
          - Gripper
        * - 4
          - M3 x 16 screws
          -
          - 
        * -
          - ,,
          - 4
          - Battery to battery module
        * - 
          - ,,
          - \-
          - Gripper
        * - \-
          - M3 x 18 screws
          -
          - Arm plates to bearing
        * - 4
          - M3 x 20 screws
          -
          - 
        * -
          - ,,
          - \-
          - Gripper
        * -
          - ,,
          - 4
          - Wheels to motor
        * - \-
          - M3 x 30 screws
          -
          - Gripper
        * - \-
          - M3 locknut
          -
          - 
        * -
          - ,,
          - \-
          - Inner arm plates to bearing
        * -
          - ,,
          - \-
          - Gripper
        * - 
          - ,,
          - \-
          - Arm to top plate
        * - 4
          - M3 washer (form a)
          -
          - Wheels to motor
        * - 35
          - M4 x 12 screws
          -
          - 
        * - 
          - ,,
          - 16
          - Base side panels to plates
        * - 
          - ,,
          - 4
          - Depth camera module to plates
        * - 
          - ,,
          - 4
          - Sonar modules to plates
        * - 
          - ,,
          - 8
          - MIRTE PCB to bottom plate   
        * -
          - ,,
          - 3
          - Lidar mount to middle plate
        * - 
          - ,,
          - \-
          - Middle to Top plate
        * - 8
          - M4 x 16 screws 
          -
          - Motor module to bottom plate
        * - 8
          - M4 locknut
          -
          - Motor module to bottom plate
        * - 19
          - M4 U-clip captive nut
          -
          - 
        * - 
          - ,,
          - 8
          - Base side panels to plates
        * -
          - ,,
          - 4
          - Depth camera module to plates
        * - 
          - ,,
          - 4
          - Sonar modules to plates
        * - 
          - ,,
          - 3
          - Lidar mount to middle plate 
        * - 8
          - M4 spring washer
          -
          - MIRTE PCB to bottom plate   
        * - 4
          - M4 washer (form a)
          - 
          - MIRTE PCB to bottom plate

   .. group-tab:: Mobile manipulator

      .. list-table::
        :widths: 5 40 5 50
        :header-rows: 1

        * - #
          - component
          - #
          - usage
        * - 2
          - `standoff 10mm M2.5 female-female <https://nl.rs-online.com/web/p/standoffs/1842689>`_
          -
          - Orange Pi 3B to bottom plate
        * - 4*
          - `standoff 25mm M4 female-female <https://nl.rs-online.com/web/p/standoffs/1058101>`_
          -
          - MIRTE PCB to bottom plate
        * - 4
          - `standoff 20mm M4 female-female <https://nl.rs-online.com/web/p/standoffs/1058094>`_
          -
          - Middle to top plate
        * - 3*
          - `standoff 40mm M3 male-female <https://nl.rs-online.com/web/p/standoffs/0221184>`_
          -
          - Arm base to top plate
        * - 2
          - M2 x 20 screws
          -
          - Orbbec Astra Mini Pro to camera module
        * - 2
          - M2 nut
          -
          - Orbbec Astra Mini Pro to camera module
        * - 8
          - M2.5 x 6 screws
          -
          - 
        * - 
          - ,,
          - 4
          - Orange Pi 3B to bottom plate
        * - 
          - ,,
          - 4
          - Lidar to lidar mount
        * - 4*
          - M2.5 x 12 screws
          -
          - Shoulder print to inner arm plate
        * - 4
          - M2.5 spring washer
          -
          - Orange Pi 3B to bottom plate
        * - 4
          - M2.5 washer (form a)
          -
          - Orange Pi 3B to bottom plate
        * - 5
          - M3 x 6 screws
          -
          - 
        * -
          - ,,
          - 1
          - Horn to rotation Servo
        * -
          - ,,
          - 4
          - USB camera to camera module
        * - 14*
          - M3 x 12 screws
          -
          - 
        * - 
          - ,,
          - 2
          - Ethernet port to side panel
        * - 
          - ,,
          - 12
          - DC motor to motor module (3 per motor)
        * - 2*
          - M3 x 14 screws
          -
          - Gripper
        * - 8
          - M3 x 16 screws
          -
          - 
        * -
          - ,,
          - 4
          - Battery to battery module
        * - 
          - ,,
          - 4
          - Gripper
        * - 6*
          - M3 x 18 screws
          -
          - Arm plates to bearing
        * - 9
          - M3 x 20 screws
          -
          - 
        * -
          - ,,
          - 5
          - Gripper
        * -
          - ,,
          - 4
          - Wheels to motor
        * - 2
          - M3 x 30 screws
          -
          - Gripper
        * - 16
          - M3 locknut
          -
          - 
        * -
          - ,,
          - 3
          - Inner arm plates to bearing
        * -
          - ,,
          - 10
          - Gripper
        * - 
          - ,,
          - 3
          - Arm to top plate
        * - 4
          - M3 washer (form a)
          -
          - Wheels to motor
        * - 43
          - M4 x 12 screws
          -
          - 
        * - 
          - ,,
          - 16
          - Base side panels to plates
        * - 
          - ,,
          - 4
          - Depth camera module to plates
        * - 
          - ,,
          - 4
          - Sonar modules to plates
        * - 
          - ,,
          - 8
          - MIRTE PCB to bottom plate   
        * -
          - ,,
          - 3
          - Lidar mount to middle plate
        * - 
          - ,,
          - 8
          - Middle to Top plate
        * - 8*
          - M4 x 16 screws 
          -
          - Motor module to bottom plate
        * - 8*
          - M4 locknut
          -
          - Motor module to bottom plate
        * - 19
          - M4 U-clip captive nut
          -
          - 
        * - 
          - ,,
          - 8
          - Base side panels to plates
        * -
          - ,,
          - 4
          - Depth camera module to plates
        * - 
          - ,,
          - 4
          - Sonar modules to plates
        * - 
          - ,,
          - 3
          - Lidar mount to middle plate 
        * - 8
          - M4 spring washer
          -
          - MIRTE PCB to bottom plate   
        * - 4
          - M4 washer (form a)
          - 
          - MIRTE PCB to bottom plate

Lasercut parts
--------------

.. tabs::

   .. group-tab:: Mobile base

      .. list-table::
        :widths: 5 95
        :header-rows: 1

        * - #
          - component
        * - 1
          - `Bottom plate (3mm PMMA) <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Cut%20Files/Bottom_plate.DXF>`_
        * - 1
          - `Middle plate (3mm PMMA) <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Cut%20Files/Middle_plate.DXF>`_
        * - 1
          - `Top plate (3mm stainless steel) <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Cut%20Files/Top_plate.DXF>`_
        * - \-
          - `Arm Inner Bottom plate (1.5mm stainless steel) <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Cut%20Files/Arm_Inner_Bottom_Plate.DXF>`_
        * - \-
          - `Arm Inner Top plate (1.5mm stainless steel) <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Cut%20Files/Arm_Inner_Top_Plate.DXF>`_
        * - \-
          - `Arm Outer Bottom plate (1.5mm stainless steel) <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Cut%20Files/Arm_Outer_Bottom_Plate.DXF>`_
        * - \-
          - `Arm Outer Top plate (1.5mm stainless steel) <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Cut%20Files/Arm_Outer_Top_Plate.DXF>`_

   .. group-tab:: Mobile manipulator

      .. list-table::
        :widths: 5 95
        :header-rows: 1

        * - #
          - component
        * - 1
          - `Bottom plate (3mm PMMA) <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Cut%20Files/Bottom_plate.DXF>`_
        * - 1
          - `Middle plate (3mm PMMA) <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Cut%20Files/Middle_plate.DXF>`_
        * - 1
          - `Top plate (3mm stainless steel) <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Cut%20Files/Top_plate.DXF>`_
        * - 1
          - `Arm Inner Bottom plate (1.5mm stainless steel) <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Cut%20Files/Arm_Inner_Bottom_Plate.DXF>`_
        * - 1
          - `Arm Inner Top plate (1.5mm stainless steel) <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Cut%20Files/Arm_Inner_Top_Plate.DXF>`_
        * - 1
          - `Arm Outer Bottom plate (1.5mm stainless steel) <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Cut%20Files/Arm_Outer_Bottom_Plate.DXF>`_
        * - 1
          - `Arm Outer Top plate (1.5mm stainless steel) <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Cut%20Files/Arm_Outer_Top_Plate.DXF>`_


3D printed parts
----------------

The original 3D printed parts are based on the components menstioned above. Since you might
want to modify your MIRTE Master based on our needs (or capability of stocking the components), 
you might need to (slightly) modify these.

These designs do not need support. The total amount of PLA needed for a mpobile manipulator
is roughly 1 kg.

.. tabs::

   .. group-tab:: Mobile base

      .. list-table::
        :widths: 5 45 50
        :header-rows: 1

        * - #
          - component
          - instructions
        * -
          - Base
          -
        * - 4
          - `Motor module <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Frame/motor_module.STEP>`_
          - 
        * - 1
          - `Left panel <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Frame/Left-Sidepanel-Module-OPI3Bv2.1.STEP>`_
          -   
        * - 1
          - `Right panel <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Frame/Right-Sidepanel-Module-Ethernet.STEP>`_
          -   
        * - 1
          - `Front panel <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Frame/Camera-Module%20Astra.STEP>`_
          -   
        * - 1
          - `Left Sonar module <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Frame/Left-Sonar-Module.STEP>`_
          -   
        * - 1
          - `Right Sonar module <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Frame/Right-Sonar-Module.STEP>`_
          -   
        * - 1
          - `Battery module <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Frame/Battery-Module.STEP>`_
          -   
        * - 1
          - `Lidar module <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Frame/LiDar-Module.STEP>`_
          -   
        * - 1
          - `Battery mount <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Frame/Battery-Mount.STEP>`_
          -   
        * - \-
          - `Cable tube <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Internal/Cable-Tube.STEP>`_
          -   
        * -
          - Arm
          -
        * - \-
          - `Rotation Servo Mount <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Arm/ZRotation-Servo-Mount.STEP>`_
          - 
        * - \-
          - `Shoulder <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Arm/Shoulder.STEP>`_
          - 
        * - \-
          - `Forearm <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Arm/Forearm.STEP>`_
          - 
        * - \-
          - `Upperarm <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Arm/Upperarm.STEP>`_
          - 
        * - \-
          - `Wrist <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Arm/Wrist.STEP>`_
          - 
        * - \-
          - `Camera mount <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Arm/Camera-Mount.STEP>`_
          - 
        * -
          - Gripper
          -
        * - \-
          - `Top plate <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Gripper/plate_top_plate.STEP>`_
          - 
        * - \-
          - `Bottom plate <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Gripper/plate_bottom_plate.STEP>`_
          - 
        * - \-
          - `Link <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Gripper/link.STEP>`_
          - 
        * - \-
          - `Geared link <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Gripper/geared%20actuator%20link.STEP>`_
          - 
        * - \-
          - `Geared actuated link <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Gripper/geared%20actuated%20link.STEP>`_
          - 
        * - \-
          - `Spacer <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Gripper/front_spacer.STEP>`_
          - 
        * - \-
          - `Actuating link left <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Gripper/actuating%20link_left_actuation_link.STEP>`_
          - 
        * - \-
          - `Actuating link right <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Gripper/actuating%20link_right_actualtion_link.STEP>`_
          - 
        * - \-
          - `Left tip <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Gripper/tip_left_tip.STEP>`_
          - 
        * - \-
          - `Right tip <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Gripper/tip_right_tip.STEP>`_
          - 

   .. group-tab:: Mobile manipulator

      .. list-table::
        :widths: 5 45 50
        :header-rows: 1

        * - #
          - component
          - instructions
        * -
          - Base
          -
        * - 4
          - `Motor module <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Frame/motor_module.STEP>`_
          - 
        * - 1
          - `Left panel <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Frame/Left-Sidepanel-Module-OPI3Bv2.1.STEP>`_
          -   
        * - 1
          - `Right panel <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Frame/Right-Sidepanel-Module-Ethernet.STEP>`_
          -   
        * - 1
          - `Front panel <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Frame/Camera-Module%20Astra.STEP>`_
          -   
        * - 1
          - `Left Sonar module <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Frame/Left-Sonar-Module.STEP>`_
          -   
        * - 1
          - `Right Sonar module <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Frame/Right-Sonar-Module.STEP>`_
          -   
        * - 1
          - `Battery module <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Frame/Battery-Module.STEP>`_
          -   
        * - 1
          - `Lidar module <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Frame/LiDar-Module.STEP>`_
          -   
        * - 1
          - `Battery mount <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Frame/Battery-Mount.STEP>`_
          -   
        * - 2
          - `Cable tube <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Internal/Cable-Tube.STEP>`_
          -   
        * -
          - Arm
          -
        * - 1
          - `Rotation Servo Mount <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Arm/ZRotation-Servo-Mount.STEP>`_
          - 
        * - 1
          - `Shoulder <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Arm/Shoulder.STEP>`_
          - 
        * - 1
          - `Forearm <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Arm/Forearm.STEP>`_
          - 
        * - 1
          - `Upperarm <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Arm/Upperarm.STEP>`_
          - 
        * - 1
          - `Wrist <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Arm/Wrist.STEP>`_
          - 
        * - 1
          - `Camera mount <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Arm/Camera-Mount.STEP>`_
          - 
        * -
          - Gripper
          -
        * - 1
          - `Top plate <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Gripper/plate_top_plate.STEP>`_
          - 
        * - 1
          - `Bottom plate <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Gripper/plate_bottom_plate.STEP>`_
          - 
        * - 2
          - `Link <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Gripper/link.STEP>`_
          - 
        * - 1
          - `Geared link <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Gripper/geared%20actuator%20link.STEP>`_
          - 
        * - 1
          - `Geared actuated link <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Gripper/geared%20actuated%20link.STEP>`_
          - 
        * - 4
          - `Spacer <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Gripper/front_spacer.STEP>`_
          - 
        * - 1
          - `Actuating link left <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Gripper/actuating%20link_left_actuation_link.STEP>`_
          - 
        * - 1
          - `Actuating link right <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Gripper/actuating%20link_right_actualtion_link.STEP>`_
          - 
        * - 1
          - `Left tip <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Gripper/tip_left_tip.STEP>`_
          - 
        * - 1
          - `Right tip <https://surfdrive.surf.nl/public.php/dav/files/Aj4w3wwbfrmnSmb/Print%20Files/Step/Gripper/tip_right_tip.STEP>`_
          - 



.. [#f1] Although branded as 6mm, you still need to drill the adapter hole to 6mm for the motor shafts. This hole should be 12.5 mm deep.

.. [#f2] There is no need to order the HiWonder ttl-us debugging board. With the MIRTE PCB, you are able to set the servos.

.. [#f3] Please check the actual USB type. Both the Raspberry Pi Pico and the RPLidar also have versions with USB-C.    
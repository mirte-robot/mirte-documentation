Hardware specs
##############

The MIRTE Master was designed to be the upgraded bigger brother of the MIRTE Pioneer. With
this the students can focus more on realiastis robot applications. Like with the MIRTE
Pioneer, we tried to minimize the number of custom components. 

.. warning::

   Please note that this is the first version (v0.1) of the MIRTE Master. We are currently
   redesigning the PCBs and part of the frame to account for a better assembly experience,
   and reduce the number of parts.


.. list-table::
   :widths: 5 35 60
   :header-rows: 1

   * - #
     - component
     - type
   * - 1
     - Computer
     - `Orange Pi 3B <http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-3B.html>`_
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
     - Main control PCB
     - `MIRTE Master main control PCB <https://github.com/mirte-robot/mirte-pcb/tree/main/mirte-master>`_   
   * - 1
     - Base control PCB
     - `MIRTE Master base control PCB <https://github.com/mirte-robot/mirte-pcb/tree/main/mirte-master-bottom>`_
   * - 1
     - Depth camera switch PCB [#f1]_
     - `MIRTE Master switcher PCB <https://github.com/mirte-robot/mirte-pcb/tree/main/mirte-usb-switcher>`_
   * - 1
     - Depth Camera
     - `Orbbec Astra Pro Plus <https://store.orbbec.com/products/astra-pro-plus>`__
   * - 1
     - 2D Lidar
     - `Slamtec rplidar C1 <https://www.seeedstudio.com/RPLiDAR-C1M1-R2-Portable-ToF-Laser-Scanner-Kit-12M-Range-p-5840.html>`_
   * - 1
     - Power sensor
     - `INA226 <https://nl.aliexpress.com/item/1005007162223972.html>`_
   * - 1
     - OLED
     - `white SSD1306 128x64 I2C <https://nl.aliexpress.com/item/1005007755490093.html>`_
   * - 1
     - IMU
     - `MPU9250 module <https://nl.aliexpress.com/item/1005007196461566.html>`_
   * - 1
     - 16 PWM servo module
     - `PCA9685 servo module <https://nl.aliexpress.com/item/1005007039294615.html>`_ [#f5]_
   * - 4 
     - Ultrasonic sensor
     - `HCSR-04 <https://nl.aliexpress.com/item/32283526790.html>`_
   * - 4 
     - DC motors (incl encoders)
     - `12V 200 RPM <https://nl.aliexpress.com/item/1005005021902364.html>`_
   * - 2
     - dual H-brigde module
     - `L298N <https://nl.aliexpress.com/item/1005006794464360.html>`_
   * - 1
     - Mecanum wheel (set of 4)
     - `100mm (2 left, 2 right) <https://nl.aliexpress.com/item/1005007533099560.html>`_ [#f2]_


.. list-table::
   :widths: 5 35 60
   :header-rows: 1

   * - #
     - electronics component
     - type
   * - 1
     - switch
     - `SPDT rocker switch <https://nl.aliexpress.com/item/1005004694368770.html>`_
   * - 1
     - Battery with XT90
     - `5000 mAh, 3S, min 5C <https://hobbyking.com/en_us/turnigy-5000mah-3s-20c-lipo-pack-xt-90.html>`_
   * - 1
     - 12-5V step down
     - `12-5V step down <https://nl.aliexpress.com/item/1005006721587257.html>`_
   * - 1
     - USB-C charger
     - USB-C charger [#f3]_
   * - 1
     - male XT90 connector
     - 
   * - 1
     - Fuse and holder
     - Fuse and holder
   * - 2
     - diodes
     - `DO201 <https://www.reichelt.com/nl/nl/shop/product/schottkydiode_5_a_40_v_do-201-216>`_ [#f4]_
   * - 36
     - wire ferrules
     - `red 1mm^2 <https://www.reichelt.com/nl/nl/shop/product/adereindhulzen_-_strips_1_mm_rood-164822>`_


.. list-table::
   :widths: 5 35 60
   :header-rows: 1

   * - #
     - cables
     - usage
   * - 2
     - `JST XH cables 4 pins 10cm <https://nl.aliexpress.com/item/1005002179605258.html>`_
     - INA226 and OLED
   * - 6
     - `JST XH cables 4 pins 30cm <https://nl.aliexpress.com/item/1005002179605258.html>`_
     - 
   * - 1
     - `JST XH cable 3 pins 30cm <https://nl.aliexpress.com/item/1005002179605258.html>`_
     - power between PCBs
   * - 2
     - `JST XH cable 8 pins 30cm <https://nl.aliexpress.com/item/1005002179605258.html>`_
     - data between PCBs
   * - 1
     - `JST XH cable 6 pins 30cm <https://nl.aliexpress.com/item/1005002179605258.html>`_
     - PCA9685
   * - 4
     - `JST **PH** cable 6 pins 20cm <https://nl.aliexpress.com/item/1005006188790994.html>`_
     - DC motors to PCB
   * - 2
     - micro USB cable 15 cm
     - Pico and switch PCB
   * - 1
     - USB-C cable
     - Orange Pi 3B Power  

.. list-table::
   :widths: 5 95
   :header-rows: 1

   * - #
     - mechanical components
   * - 1 
     - 3D printed covers
   * - 1
     - Sheet metal base frame
   * - 1
     - Sheet metal arm elements
   * - 1
     - `Ball bearing 6812 2RS <https://nl.aliexpress.com/item/1005007420073930.html>`_
   * - 40
     - M3 square nuts
   * - 3
     - `HX-12H (12KG.CM) Servo <https://www.hiwonder.com/products/htd-45h?variant=39969169440855>`_
   * - 1
     - `HTD-35H () Servo <https://www.hiwonder.com/products/htd-35h>`_
   * - 1
     - `HTD-45H (45KG.CM) Servo <(https://www.hiwonder.com/products/htd-45h>`_ 
   * - 3
     - `standoff 40mm M3 <https://nl.rs-online.com/web/p/standoffs/1768193>`_
   * - 3
     - `standoff 20mm M3 <https://nl.rs-online.com/web/p/standoffs/1768417>`_
   * - 4
     - `standoff 10mm M3 <https://nl.rs-online.com/web/p/standoffs/2052959>`_
   * - 2 
     - `standoff 25mm M2.5 <https://nl.rs-online.com/web/p/standoffs/1768379>`_
   * - 3
     - M3 x 20 screws
   * - 8 
     - M3 x 16 screws      
   * - 82
     - M3 x 6 screws
   * - 23
     - M3 nuts
   * - 19 
     - M2.5 screws
   * - 12
     - M2.5 nuts
   * - 4
     - `faston connectors <https://www.conrad.nl/nl/p/vogt-verbindungstechnik-3970-platte-stekker-male-insteekbreedte-6-3-mm-insteekdikte-0-8-mm-180-volledig-geisoleer-736986.html>`_ 


.. [#f1] The Orbbec Astra Pro Plus will draw a lot of current when powered from start. This is why it will
         need to be powered 'manually'.

.. [#f2] Need to drill the adapter hole to 6mm for the motor shafts.

.. [#f3] Needs to be a dumb chager.

.. [#f4] Flyback diodes for the motor driver.

.. [#f5] Bridge A0 for address 0x41 as INA226 is on the same I2C bus.
        
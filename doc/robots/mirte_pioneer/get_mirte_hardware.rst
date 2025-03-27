Get Mirte Hardware
##################

One of the goals of Mirte is to be modular and extendable. Therefore Mirte has a minimal amount
of custom designed components, and mostly uses frequently used hardware. Two exceptions are
the `base <https://github.com/mirte-robot/mirte-frame>`_ (which can be lasercut, 3D printed, or 
any existing base you already have) and the `PCB <https://github.com/mirte-robot/mirte-pcb>`_ 
(which is optional and can be replaced by a breadboard as well). 

Below you will find the components that are used in the Mirte Pioneer kit, which gives you a basic
mobile platform, and can be extended with optional sensors and actuators. Or you could use
alternatives/upgrades for certain parts.

Currently it is only possible to order all the parts yourself. In the future we will make it easier
to buy a full Mirte Pioneer Box with all the listed components.

.. mdinclude:: mirte_hardware_table.md

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - 
     - Mirte Pioneer
     - Alternatives/Upgrades
   * - Computer
     - `Orange Pi Zero 2 <http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-Zero-2.html>`_
     - Raspberry Pi 3/4, Orange Pi 3B
   * - micro SD card
     - Intenso 16Gb (class 10) micro SD card
     - Any 16Gb+ micro SD card 
   * - Microcontroller
     - Raspberry Pi Pico H (RP2040)
     - Arduino Nano/Uno | SMT32 
   * - Electrical circuit
     - `Mirte PCB <https://github.com/mirte-robot/mirte-pcb>`_
     - Breadboard [#f1]_ + `MB102 <https://www.aliexpress.com/item/1005001863057390.html>`_ + `splitter <https://www.aliexpress.com/item/4001025724405.html>`_
   * - 3 pin cable
     - 4x JST XH
     - 4x female-female dupont
   * - 4 pin cable
     - 4x JST XH
     - 4x female-female dupont
   * - Micro USB cable short
     - 1x
     - Dupont Cables
   * - Battery
     - `Intenso XS10000 <https://www.intenso.de/en/products/powerbanks/xs5000-xs10000-xs20000>`_
     - Any stable powerbank [#f2]_
   * - Chassis
     - `Mirte diff drive wood <https://github.com/mirte-robot/mirte-frame>`_
     - Mirte diff drive 3D print
   * - Nuts and bolts
     - 15x M3 15mm
     -
   * - Ball caster
     - `W420 (thin shape) <https://www.aliexpress.com/item/32734869856.html>`_
     -
   * - Wheels
     - `2x Yellow TT motor wheel <https://www.aliexpress.com/item/4000122298687.html>`_
     -
   * - Motors
     - `2x TT motor male dupont <https://www.aliexpress.com/item/32918824820.html>`_
     -
   * - Motor driver
     - `L9110s <https://www.aliexpress.com/item/32679413836.html>`_
     - `L298N <https://www.aliexpress.com/1005001621936295.html>`_ [#f3]_,  `MX1919 <https://www.aliexpress.com/item/32954393390.html>`_
   * - **Optional**
     -
     -
   * - Distance sensors
     - `2x HC-SR04 <https://www.aliexpress.com/item/4000232170787.html>`_
     -
   * - Line follow sensors
     - `2x TCRT5000 <https://www.aliexpress.com/item/32968870340.html>`_
     -
   * - Keypad
     - `5 button keypad <https://www.aliexpress.com/item/2044851328.html>`_
     -
   * - Displays
     - `2x 128x64 I2C OLED <https://www.aliexpress.com/item/1005001621806398.html>`_
     -
   * - Servo
     - `SG90 <https://www.aliexpress.com/item/1005001621918352.html>`_
     - Any servo supported by Arduino
   * - USB Camera
     - `OV9726 <https://www.aliexpress.com/item/1005005093538299.html>`_
     - Any USB camera

.. rubric:: Footnotes

.. [#f1] With a breadboard, the JST and USB cables need to be replaced by dupont cables.
.. [#f2] This power bank will fit the wooden frame. Any powerbank with a stable 5V will work.
.. [#f3] Due to the voltage drop of the L298N this will not work nicely with a 5V powerbank.


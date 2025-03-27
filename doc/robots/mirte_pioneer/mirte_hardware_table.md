| | MIRTE Pioneer | Alternatives/Upgrades |
| --- | --- | --- |
| Computer | [Orange Pi Zero 2](http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-Zero-2.html) | | 
| SD card | Intenso 8Gb | Any 8Gb+ SD card | 
| Microcontroller | Raspberry Pi Pico (RP2040) | Arduino Nano/Uno or SMT32
| Electrical | [MIRTE PCB](https://github.com/mirte-robot/mirte-pcb) | Breadboard [^1] + circuit [MB102](https://www.aliexpress.com/item/1005001863057390.html) + [splitter](https://www.aliexpress.com/item/4001025724405.html) | 
| 3 pin cable | 4x JST XH | 4 x female-female dupont | 
| 4 pin cable | 4x JST XH | 4 x female-female dupont | 
| Micro USB cable short | 1x | Dupont Cables | 
 | Battery | [Intenso XS10000](https://www.intenso.de/en/products/powerbanks/xs5000-xs10000-xs20000/) | Any stable powerbank [^2] | 
 | Chassis | [MIRTE diff drive wood](https://github.com/mirte-robot/mirte-frame) | MIRTE diff drive 3D print | 
 | Nuts and bolts | 15x M3 | | 
 | Ball caster | [W420 (thin shape)](https://www.aliexpress.com/item/32734869856.html) | | 
 | Wheels | [2x Yellow TT motor wheel](https://www.aliexpress.com/item/4000122298687.html) | | 
 | Motors | [2x TT motor male dupont](https://www.aliexpress.com/item/32918824820.html) | | 
 | Motor driver | [L9110s](https://www.aliexpress.com/item/32679413836.html) | [L298N](https://www.aliexpress.com/item/1005001621936295.html) [^3] or [MX1919](https://www.aliexpress.com/item/32954393390.html) | 
 | **Optional** | | 
 | Distance sensors | [2x HC-SR04](https://www.aliexpress.com/item/4000232170787.html) | | 
 | Line follow sensors | [2x TCRT5000](https://www.aliexpress.com/item/32968870340.html) | | 
 | Keypad | [5 button keypad](https://www.aliexpress.com/item/2044851328.html) | | 
 | Displays | [2x 128x64 I2C OLED](https://www.aliexpress.com/item/1005001621806398.html) | | 
 | Servo | [SG90](https://www.aliexpress.com/item/1005001621918352.html) | Any servo supported by Arduino | 
 | USB Camera | [OV9726](https://www.aliexpress.com/item/1005005093538299.html) | Any USB camera | 
----------------------

**Footnotes**

[^1]: With a breadboard, the JST and USB cables need to be replaced by dupont cables.

[^2]: This power bank will fit the wooden frame. Any powerbank with a stable 5V will work.

[^3]: Due to the voltage drop of the L298N this will not work nicely with a 5V powerbank.

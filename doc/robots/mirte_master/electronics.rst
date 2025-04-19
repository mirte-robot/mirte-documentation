Electronics
###########

The MIRTE Master is built to be as easy to work with as possible, there should be no need to change anything in the electronics.

The MIRTE Master has 4 PCBs:
- MIRTE compute (main pcb), with a Pico
- MIRTE Sense and Control, connecting the motor drivers, encoders, main PCB and the sonars together
- ~~BMS board, converting the JST-XH connector of the LiPo battery to the JST-PH connector of the 3s BMS~~
- USB switch board, switching the power of the Orbbec Astra depth camera

Assembly instructions:

[Instructions](../_static/Assembly_electro.pdf)

[Rough overview schematic](../_static/mirteMasterSchema.pdf)

### MIRTE compute
[mirte-pcb:mirte-master/mirte-master](https://github.com/ArendJan/mirte-pcb/tree/mirte-master/mirte-master)

Errata (v0.2):
- 5v and GND labels(bottom) for the 12v->5v screw terminal are inverted
- power switch cable to pcb must be removed to disable the light in the switch.
- relay system doesn't work.
![main pcb](../../_images/master/pcb_main.png)

### MIRTE sense&Control
[mirte-pcb:mirte-master/mirte-master-bottom](https://github.com/ArendJan/mirte-pcb/tree/mirte-master/mirte-master-bottom)

![bottom pcb](../../_images/master/pcb_bottom.png)
### Usb switcher
[mirte-pcb:mirte-master/mirte-usb-switcher](https://github.com/ArendJan/mirte-pcb/tree/mirte-master/mirte-usb-switcher)

Leds:
- D2: GPIO4_B4, used for blinking SOC
- D1: GPIO4_B5, unused
- D4: GPIO0_D1, unused
- D3: GPIO4_C3, used for USB power switch

J4, unsoldered header for any use:
- 3v3
- D2: GPIO4_B4
- D1: GPIO4_B5
- D3: GPIO0_D1
- D4: GPIO4_C3
- GND
![usb switch pcb](../../_images/master/pcb_usb_switch.png)
Image shows 2x4 header on top, must be soldered on the bottom.

Errata:
- GPIO4_D4 label(bottom side) should be GPIO4_C3 due to faulty Orange Pi pinout diagrams. 

### BMS board
[mirte-pcb:mirte-master/mirte-bms-breakout](https://github.com/ArendJan/mirte-pcb/tree/mirte-master/mirte-bms-breakout)

![bms board](../../_images/master/pcb_bms.png)


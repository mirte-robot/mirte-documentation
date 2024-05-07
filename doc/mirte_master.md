# Mirte Master


The Mirte Master is one of the possible upgrades of the Mirte robot.

<!-- .. plaatje -->

## Frame


The frame is built using 1mm aluminium and 3D printed parts. 
Building instructions:
- [Base](../_static/Assembly_BASE.pdf)
- [Top and arm](../_static/Assembly_TOP_ARM.pdf)


### Base

The base:

<!-- .. plaatje -->


### Arm

The arm has 4 servos for movement and one for the gripper. The ranges are stored in the servo together with a deviation to keep the config the same, while the servos can be mounted differently. The user should never have to deal with the centidegrees ranges, only the range and angles in radians.

| Servo    | ID  | Range(centidegrees) | Range (Bus servo terminal) | Range (rad) | Home  |
| -------- | --- | ------------ | ----------- | ----- | --- |
| Rotation | 2   | 3400-21000*  | 141-875 | [-1.6, 1.5] | 12000 |
| Shoulder | 3   | 2832-20000* | 118-833 |  [-1.5, 1.5]   | 11450 |
| Elbow    | 4   | 120-21000   | 5-875 |  [-2,	1.6] | 11750 |
| Wrist    | 5   | 1128-21672*  | 47-903 |  [-1.7,	1.9]  | 12200 |
| Gripper  | 6   | 6168-11224 **         | 257-468  | [-0.7,	0.2]          | 9984     |
-------
`*`: inverted rotation, range has taken care of this

`**`: Longer range than the gripper can reach

The services for the servos use the radian ranges. Getting the ranges is possible by calling the `/mirte/get_<name>_servo_range`.

The home position of the arm is forward pointing up:
- Arm is rotated forward:
- ![Rotation forward](images/master/mirte_master_arm_home_rot.jpg) 
- Arm is pointing up:
- ![Arm up](images/master/mirte_master_arm_home_side.jpg) 
- The Gripper has the servo-driven beams horizontal:
- ![Gripper horizontal beams](images/master/mirte_master_arm_home_grip.jpg) 
#### Moveit

TODO!

<!-- .. TODO: @mklomp -->


## Software
The Mirte-master is using the same base software as any other Mirte robot, with some extras.

### Computer

The computer is a Orange Pi 3B with 4gb RAM and 16/32 eMMC. It is running a Armbian 23.11 Focal image with ROS Noetic. You can download a fresh image from `here <https://github.com/ArendJan/mirte-sd-image-tools/actions/workflows/buildFork.yaml>`_. Click on the latest action and then download the ```mirte_master_mirte_orangepi3b``` or ```mirte_master_installer_orangepi3b``` artifact. The ```..._installer_...``` can be used to flash the eMMC. At boot it will copy the image (same as the normal one) to the eMMC, setup bootloader to be sure and shut down. This can take around 20 minutes. 

It works the same as the normal Mirte robot. Move the base with publishing to ```/mobile_base_controller/cmd_vel``` with a geometry_msgs/Twist message. 

### Master Mirte-install-scripts
[mirte-install-scripts:mirte-master2](https://github.com/ArendJan/mirte-install-scripts/tree/mirte-master2)

Changes from default:
- Password system:
  - After changing the pw (first login):
    - the user password changes
    - the website login changes
    - after the next boot: the Wi-Fi password is changed
- Website:
  - different urls:
    - video server: http://mirte.local/ros-video/
    - jupyter (if enabled?): http://mirte.local/jupyter/
    - docs: http://mirte.local/docs/
    - visual studio code (browser): http://mirte.local/code/
  - Login:
    - When accessing any of the sites from any IP other 192.168.40.1-47.255 (Wi-Fi hotspot) or 192.168.137.1-255 (Windows hotspot), youlll need to log in. This is the same user and password as when logging in with SSH
    - To allow more IP ranges, edit ```/etc/nginx/nginx_login.conf``` 
- extra ROS packages:
  - https://github.com/Slamtec/rplidar_ros.git: lidar node
  - https://github.com/orbbec/ros_astra_camera.git: depth camera node
  - https://github.com/arendjan/ridgeback.git: mecanum wheel support with custom fix.
- Picotool installed to easily flash the Raspberry Pi Pico
- more ZSH support
- Support for @chris-pek his chat-gpt ROS node
- USB-switch systemctl module:
  - after boot, this module will turn on a GPIO pin (GPIO4_C3) to turn on the USB switch IC on the small board on top of the Orange Pi. This is to fix a power bug of the Orbbec Astra camera (pulling 1A+ when plugged in at boot)

### Mirte-ros-packages
[mirte-ros-packages:mirte-master](https://github.com/ArendJan/mirte-ros-packages/tree/mirte-master)

Changes:
- Added extra launch files (mirte_bringup)
- added omniwheels (ridgeback) support (mirte_control)
  - TODO: encoder and odometry
  - TODO: speeds don't match
- Telemetrix:
  - Extra config for mirte-master
    - TODO: check arm and gripper angles, GPIO SOC led
    - TODO: IMU
  - Oled: shows SOC, IP, hostname and Wi-Fi host
  - Hiwonder UART servos:
    - Added servo support, services/topics:
      - ```/mirte/set_{servo_name}_servo_angle``` SetServoAngle service, in radians from home
      - ```/mirte/set_{servo_name}_servo_enable``` SetBool service, enable or disable servo. After sending a new angle, it is enabled again
      - ```/mirte/servos/{servo_name}/position``` ServoPosition topic, radians from home
      - ```/mirte/set_{bus_name}_all_servos_enable``` SetBool service, enable or disable all servos on this bus.
  - Neopixel support (WS2811)
    - ```/mirte/set_{name}_color_all``` SetLedValue service, uint32_t color, with ```0xRRGGBB``` or ```0xRRBBGG``` value (0-255)
    - ```/mirte/set_{name}_color_single``` SetSingleLedValue service, same color setup with a 0-indexed pixel id
  - PCA9685 (pwm driver):
    - For servos:
      - When any servo is added, frequency will be set to 50Hz. 
      - ```/mirte/set_{name}_servo_angle``` SetServoAngle service, with angle [0, 180]
    - Motors (2x PWM channel):
      - Normal motor service and topics
      - Range is [-100, 100]
  - INA226 (power watcher)
    - used to measure current and voltage. Can trigger a shutdown if the LiPo voltage is too low. The current state of charge(SOC) can be shown with a LED and the OLED screen.
      <!-- Also detects the power switch to safely shut down the robot. Not working bc hardware issues with relay -->


### Telemetrix4RpiPico:
[Repo](https://github.com/ArendJan/Telemetrix4RpiPico/tree/modules2)
- Added support for multiple devices:
  - Hiwonder servos
  - PCA9685
  - INA226
  - MPU9250 IMU, however, it might crash i2c comms.
  
  Not yet added to ROS:
  - HX711 load cell
  - VL93L0 distance sensor
  - ADXL345 accelerometer
  - VEML6040 color sensor

### Flashing the Pico
go to ```/usr/local/src/mirte/mirte-install-scripts/``` and run ```./upload_arduino.sh upload_pico Telemetrix4rpipico```. This will stop ROS, flash the Pico and restart ROS again. If flashing failed or something else, it will tell you how to restart ROS again.

## Electronics
The Mirte-master is built to be as easy to work with as possible, there should be no need to change anything in the electronics.

The Mirte-master has 4 PCBs:
- Mirte compute (main pcb), with a Pico
- Mirte Sense and Control, connecting the motor drivers, encoders, main PCB and the sonars together
- BMS board, converting the JST-XH connector of the LiPo battery to the JST-PH connector of the 3s BMS
- USB switch board, switching the power of the Orbbec Astra depth camera

Assembly instructions:

[Instructions](../_static/Assembly_electro.pdf)

### Mirte compute
[mirte-pcb:mirte-master/mirte-master](https://github.com/ArendJan/mirte-pcb/tree/mirte-master/mirte-master)

Errata (v0.2):
- 5v and GND labels for the 12v->5v screw terminal are inverted
![main pcb](images/master/pcb_main.png)
- power switch cable to pcb must be removed to disable the light in the switch.

### Mirte sense&Control
[mirte-pcb:mirte-master/mirte-master-bottom](https://github.com/ArendJan/mirte-pcb/tree/mirte-master/mirte-master-bottom)

![bottom pcb](images/master/pcb_bottom.png)
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
![usb switch pcb](images/master/pcb_usb_switch.png)
Errata:
- GPIO4_D4 label should be GPIO4_C3 due to faulty Orange Pi pinout diagrams. 

### BMS board
[mirte-pcb:mirte-master/mirte-bms-breakout](https://github.com/ArendJan/mirte-pcb/tree/mirte-master/mirte-bms-breakout)

![bms board](images/master/pcb_bms.png)


# WIP:
- calibrate arm and fix forgetting ID
- IMU
- odometry
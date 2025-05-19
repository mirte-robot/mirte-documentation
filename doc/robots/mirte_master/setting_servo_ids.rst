Setting servo IDs
#################

The arm has 4 servos for movement and one for the gripper. The ranges are stored in the servo together with a
deviation to keep the config the same, while the servos can be mounted differently. The user should never
have to deal with the centidegrees ranges, only the range and angles in radians. The "Bus Servo Serminal"
ranges are only when you have a new arm without ranges set. You can set the ranges and IDs
with [Bus Servo Terminal](https://www.hiwonder.com.cn/store/learn/43.html) and
a [Buslinker](https://www.hiwonder.com/collections/servo-controller/products/hiwonder-ttl-usb-debugging-board).

.. list-table::
   :widths: 15 10 10 5 20 20 20
   :header-rows: 1

   * - Servo
     - type
     - ID
     - range (centidegrees)
     - range (bus servo terminal)
     - range (rad)
     - home
   * - shoulder_pan
     - HX-12H
     - 2 [#f0]_
     - 3400-21000 [#f1]_
     - 141-875
     - [-1.6, 1.5]
     - 12000
   * - shoulder_lift
     - HTD-45H
     - 3
     - 2832-20000 [#f1]_
     - 118-833
     - [-1.5, 1.5]
     - 11450
   * - elbow
     - HTD-35H
     - 4
     - 120-21000
     - 5-875
     - [-2, 1.6]
     - 11750
   * - wrist
     - HX-12H
     - 5
     - 1128-21672 [#f1]_
     - 47-903
     - [-1.7, 1.9]
     - 12200
   * - gripper
     - HX-12H
     - 6
     - 6168-11224 [#f2]_
     - 257-468
     - [-0.7, 0.2]
     - 9984

.. [#f0] The default ID for a new servo is 1. This is why we start at 2.

.. [#f1] Inverted rotation, range has taken care of this.

.. [#f2] Longer range than the gripper can reach.

The home position of the arm is forward pointing up:

- Arm is rotated forward:
- ![Rotation forward](./_images/master/mirte_master_arm_home_rot.jpg)
- Arm is pointing up:
- ![Arm up](./_images/master/mirte_master_arm_home_side.jpg)
- The Gripper has the servo-driven beams horizontal:
- ![Gripper horizontal beams](./_images/master/mirte_master_arm_home_grip.jpg)


Setting servo IDs
=================

### Moving cable to front of shoulder servo
In the original design, the cable going from the rotation servo to the shoulder servo is connected to the bottom of the shoulder servo. This makes it impossible to set the IDs for the shoulder and rotation>
- Unscrew the 3&4 screws on the side of the shoulder servo.
- Disconnect the cable from the bottom of the shoulder servo.
- plug it in on the front of that servo
- screw back in the 7 screws.

Connector on underside of shoulder, must go to the front one:
![shoulder connector](./_images/arm_servos/shoulder_wrong.jpg)

### Setup:
- Download and install the Bus Servo Terminal application: [Bus Servo Terminal](https://drive.google.com/drive/folders/1wIIIccKKmrLX4EyswIkunIs-A_SKX1Nq)
- Grab the BusLinker and the powerbank from the toolbox:
![buslinker](./_images/arm_servos/buslinker.jpg)
- Connect white usb connector to the powerbank and the black one to your computer
- open Bus Servo Terminal, set the COM port(left side, should be only one) and press open port:
![bus terminal](./_images/arm_servos/terminal_com.png)

### Setting the servos:
- Unplug some cables to isolate each servo. You can only connect one servo at a time, otherwise it will write the same ID to multiple servos.

  - Unplug the cable from the gripper
  - Unplug the cable going to the wrist from the elbow(green servo)
  - Unplug both cables from the shoulder(orange servo)

- Go to the ```parameters``` tab
- For every servo:
  - Connect the buslinker board to a servo
  - Click ```read``` to download the range and the other settings that somehow don't get messed up
  - Check that ID is on 0, if it isn't on 0, then your robot has another problem.
  - Set the ID to the ID it should be (2-6, counted from rotation -> gripper)
  - Press ```apply```
  - Click ```read``` again to check that the data is written to the servo
- Reconnect all the cables to the servos. It does not matter in which connector they are.
- Calibrate the arm again:
  - ```cd /usr/local/src/mirte/mirte-tmx-pico-aio/```
  - ```git pull```
  - ```pip install .```
  - ```pip install aioconsole```
  - ```cd examples/```
  - ```python3 mirte_master_reset_offset.py```
  - ```python3 mirte_master_set_ranges_volt.py```
  - ```python3 mirte_master_check_home.py```

Parameters tab:
![parameters tab](_images/arm_servos/terminal_parameters.png)

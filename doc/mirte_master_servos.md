# Setting servo IDs

Sometimes the servos forget their ID. Why this happens isn't yet known. We are in contact with HiWonder to figure it out.

## Moving cable to front of shoulder servo
In the original design, the cable going from the rotation servo to the shoulder servo is connected to the bottom of the shoulder servo. This makes it impossible to set the IDs for the shoulder and rotation servo. 
- Unscrew the 3&4 screws on the side of the shoulder servo.
- Disconnect the cable from the bottom of the shoulder servo.
- plug it in on the front of that servo
- screw back in the 7 screws.
  
Connector on underside of shoulder, must go to the front one:
![shoulder connector](./images/master/arm_servos/shoulder_wrong.jpg)

## Setup:
- Download and install the Bus Servo Terminal application: [Bus Servo Terminal](https://drive.google.com/drive/folders/1wIIIccKKmrLX4EyswIkunIs-A_SKX1Nq)
- Grab the BusLinker and the powerbank from the toolbox: ![buslinker](./images/master/arm_servos/buslinker.jpg)
- Connect white usb connector to the powerbank and the black one to your computer
- open Bus Servo Terminal, set the COM port(left side, should be only one) and press open port:
  ![bus terminal](./images/master/arm_servos/terminal_com.png)

## Setting the servos:
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
![parameters tab](images/master/arm_servos/terminal_parameters.png)
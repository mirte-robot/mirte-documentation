
Motors
^^^^^^
.. tabs::

    .. group-tab:: Config
    
        .. code-block:: yaml
    
            motor:
                NAME:
                    name: NAME
                    device: mirte
                    type: pp
                    pins:
                        p1: GP18
                        p2: GP19
                NAME2:
                    name: NAME2
                    device: mirte
                    type: pp
                    connector: MC1-A

        Required: ``name``, ``device``, ``type``, ``pins`` or ``connector``

        - ``name``: Name of the motor. This is the name that will be used in the ROS topic. Name of the yaml block must be the same as in the name key.

        - ``device``: The device that the motor is connected to. This is always ``mirte``.

        - ``type``: The type of motor. This can be ``pp``, ``dp`` or ``ddp``. 

            - ``pp``: dual pwm
            - ``dp``: pwm with digital pin. The digital pin is used to control the direction, pwm is inverted when driving backwards. 'Smart' motor drivers don't work yet with those.
            - ``ddp``: dual digital pin, single pwm. Digital pins for direction and enable, pwm pin for speed, often connected to the enable pin of the motor driver.

        - ``pins``: The pins that the motor is connected to. This is a dictionary with the keys ``p1`` and ``p2`` for pwm, ``d1`` and ``d2`` if using digital pins (type). The values are the pin names or number.

        - ``connector``: The connector that the motor is connected to. This is a string. See the PCB for what name to use. Either pins or connector is required.
        
        Optional:

        - ``inverted``: If the motor is rotating the wrong way. Default is ``False``.
    .. group-tab:: Topics & Services

        Only new speeds can be published to motors. The value is in range [-100, 100].

        - Topic:
            - ``/HOSTNAME/io/motor/NAME/speed``: `std_msgs/msg/Int32 <https://docs.ros.org/en/humble/p/std_msgs/interfaces/msg/Int32.html>`_
            .. code-block:: bash
                
                ros2 topic pub /$HOSTNAME/io/motor/NAME/speed std_msgs/msg/Int32 "data: 50"
               
        - Services:
            - ``/mirte_6e3c89/io/motor/NAME/set_speed`` (mirte_msgs/srv/SetMotorSpeed)
            .. TODO: service html auto maken

            .. code-block:: bash

                ros2 service call /$HOSTNAME/io/motor/NAME/set_speed mirte_msgs/srv/SetMotorSpeed "speed: 50"
    

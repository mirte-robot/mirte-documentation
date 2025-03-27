
Oled
^^^^
SSD1306 OLED display. Only the 128x64 version is supported. Up to 2 oleds are supported on most mcus. The oleds are connected via I2C and cannot share a bus.

.. tabs::

    .. group-tab:: Config
    
        .. code-block:: yaml
    
                oled: # type
                    NAME:
                        device: mirte
                        connector: I2C1

                oled:
                  NAME:
                    device: mirte
                    pins:
                      scl: A5
                      sda: A4
                    addr: 0x3C
                    legacy: False
                    default_image_path: /path/to/image.png
                    default_screen_script: /path/to/script.sh



        Required: ``device``, ``pins`` or ``connector``

        - ``device``: The device that the motor is connected to. This is always ``mirte``.

        - ``pins``: The pins that the motor is connected to. This is a dictionary with the keys ``sda`` and ``scl`` for I2C. The values are the pin names or number.

        - ``connector``: The connector that the motor is connected to. This is a string. See the PCB for what name to use. Either pins or connector is required.
        
        Optional:

        - ``legacy``: Enable/disable legacy oled service.
        - ``default_image_path``: Path to the default image that is shown on the oled screen.
        - ``default_screen_script``: Path to the script that is executed to show the default screen. Either default_image_path or default_screen_script can be used. If the ``default_screen_script`` is not executable, then it will be tried as an image. Images must be in the format of 128x64 pixels. The script must output to stdout. ``pkg://``, ``packages://`` are supported. If not starting with that or a slash, it is assumed to be in the ``mirte_telemetrix_cpp`` package. Default is ``pkg://mirte_telemetrix_cpp/scripts/default_screen.sh``.
        - ``addr``: The I2C address of the oled. Default is 0x3C.

        
    .. group-tab:: Topics & Services

        Only new speeds can be published to motors. The value is in range [-100, 100].

        - Topic:
            - None
               
        - Services:
            - ``/mirte_6e3c89/io/motor/NAME/set_speed`` (mirte_msgs/srv/SetMotorSpeed)
            .. TODO: service html auto maken

            .. code-block:: bash

                ros2 service call /$HOSTNAME/io/motor/NAME/set_speed mirte_msgs/srv/SetMotorSpeed "speed: 50"
    

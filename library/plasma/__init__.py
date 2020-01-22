__version__ = '1.0.0'


def get_device(descriptor):
    """Return a Plasma device class and arguments.

    :param descriptor: String describing device and arguments.

    This function accepts descriptors in the form:

    DEVICE:arg:arg

    IE: A serial connection would be described as:

    SERIAL:/dev/ttyACM0

    And GPIO as:

    GPIO:14:15

    And WS281X pixels as:

    WS281X:WS2812_RGB:13:1

    """
    dsc = descriptor.split(":")
    if dsc[0] == "GPIO":
        from .gpio import PlasmaGPIO
        return PlasmaGPIO, {'gpio_data': int(dsc[1]), 'gpio_clock': int(dsc[2])}
    if dsc[0] == "SERIAL":
        from .usb import PlasmaSerial
        return PlasmaSerial, {'port': dsc[1]}
    if dsc[0] == "WS281X":
        from .ws281x import PlasmaWS281X
        # TODO: Add (optional) support for variable frequency, DMA, brightness and invert
        return PlasmaWS281X, {'strip_type': dsc[1], 'gpio_pin': int(dsc[2]), 'channel': int(dsc[3])}

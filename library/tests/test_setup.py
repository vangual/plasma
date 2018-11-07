"""Test Plasma basic initialisation."""
import mock
import sys
from tools import GPIO


def test_setup():
    """Test init succeeds and GPIO pins are setup."""
    gpio = GPIO()
    sys.modules['RPi'] = mock.Mock()
    sys.modules['RPi'].GPIO = gpio
    sys.modules['RPi.GPIO'] = gpio
    import plasma
    plasma.show()

    assert gpio.pin_modes[plasma.DAT] == gpio.OUT
    assert gpio.pin_modes[plasma.CLK] == gpio.OUT

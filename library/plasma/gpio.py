from .core import Plasma

class PlasmaGPIO(Plasma):
    def __init__(self, light_count, gpio_data=15, gpio_clock=14):
        self._gpio_data = gpio_data
        self._gpio_clock = gpio_clock
        self._gpio_is_setup = False
        self.__init__(self, light_count)

    def use_pins(self, gpio_data, gpio_clock):
        raise NotImplementedError

    def _write_byte(self, byte):
        for x in range(8):
            GPIO.output(self._gpio_data, byte & 0b10000000)
            GPIO.output(self._gpio_clock, 1)
            time.sleep(0.0000005)
            byte <<= 1
            GPIO.output(self._gpio_clock, 0)
            time.sleep(0.0000005)

    def _eof(self):
        # Emit exactly enough clock pulses to latch the small dark die APA102s which are weird
        # for some reason it takes 36 clocks, the other IC takes just 4 (number of pixels/2)
        GPIO.output(self._gpio_data, 0)
        for x in range(36):
            GPIO.output(self._gpio_clock, 1)
            time.sleep(0.0000005)
            GPIO.output(self._gpio_clock, 0)
            time.sleep(0.0000005)

    def _sof(self):
        GPIO.output(self._gpio_data, 0)
        for x in range(32):
            GPIO.output(self._gpio_clock, 1)
            time.sleep(0.0000005)
            GPIO.output(self._gpio_clock, 0)
            time.sleep(0.0000005)

    def show(self):
        """Output the buffer."""
        if not self._gpio_is_setup:
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setup(self._gpio_data, GPIO.OUT)
            GPIO.setup(self._gpio_clock, GPIO.OUT)
            self._gpio_is_setup = True

        self._sof()

        for pixel in self._pixels:
            r, g, b, brightness = pixel
            self._write_byte(0b11100000 | brightness)
            self._write_byte(b)
            self._write_byte(g)
            self._write_byte(r)

        self._eof()
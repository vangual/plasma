import atexit
import colorsys

PIXELS_PER_LIGHT = 4
DEFAULT_BRIGHTNESS = 3
MAX_BRIGHTNESS = 3


class Plasma():
    def __init__(self, light_count):
        self._light_count = light_count
        self._pixels = [[0, 0, 0, DEFAULT_BRIGHTNESS]] * light_count * PIXELS_PER_LIGHT
        self._clear_on_exit = False

        atexit.register(self.atexit)

    def get_pixel_count(self):
        return self._light_count * PIXELS_PER_LIGHT

    def get_light_count(self):
        return self._light_count

    def show(self):
        raise NotImplementedError

    def atexit(self):
        if not self._clear_on_exit:
            return
        self.clear()
        self.show()

    def set_light_count(self, light_count):
        raise NotImplementedError

    def set_light_hsv(self, index, h, s, v):
        (rf, gf, bf) = colorsys.hsv_to_rgb(h / 255, s / 255, v / 255)
        self.set_light(index, int(rf * 255), int(gf * 255), int(bf * 255))

    def set_pixel_hsv(self, index, h, s, v):
        (rf, gf, bf) = colorsys.hsv_to_rgb(h / 255, s / 255, v / 255)
        self.set_pixel(index, int(rf * 255), int(gf * 255), int(bf * 255))

    def set_clear_on_exit(self, status=True):
        self._clear_on_exit = status

    def set_light(self, index, r, g, b, brightness=None):
        """Set the RGB colour of an individual light in your Plasma chain.

        This will set all four LEDs on the Plasma light to the same colour.

        :param index: Index of the light in your chain (starting at 0)
        :param r: Amount of red: 0 to 255
        :param g: Amount of green: 0 to 255
        :param b: Amount of blue: 0 to 255

        """
        offset = index * PIXELS_PER_LIGHT
        for x in range(PIXELS_PER_LIGHT):
            self.set_pixel(offset + x, r, g, b, brightness)

    def set_all(self, r, g, b, brightness=None):
        """Set the RGB value and optionally brightness of all pixels.

        If you don't supply a brightness value, the last value set for each pixel be kept.

        :param r: Amount of red: 0 to 255
        :param g: Amount of green: 0 to 255
        :param b: Amount of blue: 0 to 255
        :param brightness: Brightness: 0.0 to 1.0 (default is 1.0)

        """
        for x in range(self._light_count * PIXELS_PER_LIGHT):
            self.set_pixel(x, r, g, b, brightness)

    def get_pixel(self, x):
        """Get the RGB and brightness value of a specific pixel.

        :param x: The horizontal position of the pixel: 0 to 7

        """
        r, g, b, brightness = self._pixels[x]
        brightness /= float(MAX_BRIGHTNESS)

        return r, g, b, round(brightness, 3)

    def set_pixel(self, x, r, g, b, brightness=None):
        """Set the RGB value, and optionally brightness, of a single pixel.

        If you don't supply a brightness value, the last value will be kept.

        :param x: The horizontal position of the pixel: 0 to 7
        :param r: Amount of red: 0 to 255
        :param g: Amount of green: 0 to 255
        :param b: Amount of blue: 0 to 255
        :param brightness: Brightness: 0.0 to 1.0 (default around 0.2)

        """
        if brightness is None:
            brightness = self._pixels[x][3]
        else:
            brightness = int(float(MAX_BRIGHTNESS) * brightness) & 0b11111

        self._pixels[x] = [int(r) & 0xff, int(g) & 0xff, int(b) & 0xff, brightness]

    def clear(self):
        """Clear the pixel buffer."""
        for x in range(self._light_count * PIXELS_PER_LIGHT):
            self._pixels[x][0:3] = [0, 0, 0]

    def set_brightness(self, brightness):
        """Set the brightness of all pixels.

        :param brightness: Brightness: 0.0 to 1.0

        """
        if brightness < 0 or brightness > 1:
            raise ValueError('Brightness should be between 0.0 and 1.0')

        for x in range(self._light_count * PIXELS_PER_LIGHT):
            self._pixels[x][3] = int(float(MAX_BRIGHTNESS) * brightness) & 0b11111

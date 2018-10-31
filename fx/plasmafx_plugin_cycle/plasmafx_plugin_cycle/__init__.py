from plasmafx import Plugin
from colorsys import hsv_to_rgb

class Cycle(Plugin):
    def __init__(self, speed=1.0, spread=1.0, offset=0, saturation=1.0, value=1.0):
        Plugin.__init__(self)
        self._speed = float(speed)
        self._saturation = float(saturation)
        self._value = float(value)
        self._spread = float(spread)
        self._offset = offset

    def get_values(self, delta):
        delta *= self._speed
        values = []
        for x in range(4):
            hue = (delta / 10.0) + (x / 100.0 * self._spread) + (self._offset/360.0)
            r, g, b = hsv_to_rgb(hue, self._saturation, self._value)
            r, g, b = [int(c * 255) for c in (r, g, b)]
            values += [r, g, b]
        return values

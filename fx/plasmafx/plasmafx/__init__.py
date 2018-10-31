import time

ELEMENT_LED_COUNT = 4

class Plugin(object):
    """PlasmaFX Plugin.

    A PlasmaFX plugin is responsible for the 4 lights on
    a single Plasma light board.

    """
    def get_values(self):
        return

class Sequence(object):
    """PlasmaFX Sequence.

    A PlasmaFX sequence is responsible for a sequence of
    Plasma light boards.

    """
    def __init__(self, element_count):
        self.element_count = element_count
        self.elements = [None for x in range(element_count)]

    def set_plugin(self, element_index, plugin):
        self.elements[element_index] = plugin

    def get_raw(self):
        delta = time.time()
        values = []
        for element in range(self.element_count):
            values += self.elements[element].get_values(delta)
        return values

    def get_leds(self):
        values = []
        raw_values = self.get_raw()
        for x in range(0, self.element_count * ELEMENT_LED_COUNT * 3, 3):
            values.append(tuple(raw_values[x:x+3]))
        return values

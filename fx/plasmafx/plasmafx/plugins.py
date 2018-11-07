import pkg_resources
from plasmafx import Plugin

plasma_fx_plugins = {}

for entry_point in pkg_resources.iter_entry_points('plasmafx.effect_plugins'):
    effect_handle = entry_point.name
    plasma_fx_plugins[effect_handle] =  entry_point.load()
    globals()['FX{}'.format(effect_handle)] = entry_point.load()


class Solid(Plugin):
    def __init__(self, r, g, b):
        self.set_colour(r, g, b)

    def set_colour(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def get_values(self, delta):
        return [self.r, self.g, self.b] * 4


class Pulse(Plugin):
    def __init__(self, sequence, speed=1):
        self.sequence = sequence
        self.speed = speed

    def c(self, index, channel):
        return self.sequence[index][channel]

    def blend(self, channel, first, second, blend):
        result = (self.c(second, channel) - self.c(first, channel)) * float(blend)
        result += self.c(first, channel)
        return int(result)

    def get_values(self, delta):
        length = len(self.sequence)
        position = (delta % self.speed) / float(self.speed)
        colour = length * position
        blend = colour - int(colour)
        first_colour = int(colour) % length
        second_colour = (first_colour + 1) % length

        r = self.blend(0, first_colour, second_colour, blend)
        g = self.blend(1, first_colour, second_colour, blend)
        b = self.blend(2, first_colour, second_colour, blend)
        return [r, g, b] * 4

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

#!/usr/bin/env python

import colorsys
import time

import plasma

spacing = 360.0 / 16.0
hue = 0

plasma.set_clear_on_exit()
plasma.set_light_count(10)

while True:
    hue = int(time.time() * 100) % 360
    for x in range(plasma.NUM_PIXELS):
        offset = x * spacing
        h = ((hue + offset) % 360) / 360.0
        r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(h, 1.0, 1.0)]
        plasma.set_pixel(x, r, g, b)

    plasma.show()
    time.sleep(0.001)

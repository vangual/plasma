import plasma
import plasmafx
from plasmafx import plugins
import time

FPS = 60
NUM_LIGHTS = 10

plasma.set_light_count(10)

sequence = plasmafx.Sequence(NUM_LIGHTS)

for x in range(NUM_LIGHTS):
    sequence.set_plugin(x, plugins.FXCycle(
        speed=2,
        spread=5,
        offset=(360.0/NUM_LIGHTS) * x
    ))

sequence.set_plugin(0, plugins.Pulse([
	(0, 0, 0),
	(255, 0, 255)
]))

sequence.set_plugin(1, plugins.Pulse([
        (255, 0, 0),
        (0, 0, 255),
        (0, 0, 0)
], speed=0.5))

while True:
    values = sequence.get_leds()

    for index, rgb in enumerate(values):
        # print("Setting pixel: {} to {}:{}:{}".format(index, *rgb))
        plasma.set_pixel(index, *rgb)
    plasma.show()
    time.sleep(1.0 / FPS)

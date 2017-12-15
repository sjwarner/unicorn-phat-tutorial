# This is the first thing I have made using a pHAT!
# It's a super basic rainbow thing, inspired by pimoroni's
# 'getting started with unicorn phat' post.

import unicornhat as uh
import time
import colorsys

uh.set_layout(uh.PHAT)
uh.brightness(0.5)

spacing = 360.0 / 16.0
hue = 0

while True:
    hue = int(time.time() * 100) % 360
    for x in range(8):
        offset = x * spacing
        h = ((hue + offset) % 360) / 360.0
        r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(h, 1.0, 1.0)]
        for y in range(4):
            uh.set_pixel(x, y, r, g, b)
    uh.show()
    time.sleep(0.05)

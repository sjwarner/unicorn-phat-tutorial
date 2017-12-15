# This is a binary clock using the unicorn phat
# You can change your timezone below, I chose London

# View from non-cable side:
# hh : mm : ss
# 12 : 00 : 00
# For example, where each colon column is left blank

import time
from datetime import datetime as dt
from itertools import izip_longest as zl
from pytz import timezone as tz

london = tz('Europe/London')

def main():
    return(vertical_strings(bcd(Now)))

def bcd(digits):
    def bcdigit(d):
        return bin(d)[2:].rjust(4,'0')
    return (bcdigit(int(d)) for d in digits)

def vertical_strings(strings):
    iters = [iter(s) for s in strings]
    concat = ''.join
    return '\n'.join(map(concat, zl(*iters, fillvalue='')))

import unicornhat as uh

uh.set_layout(uh.PHAT)
uh.brightness(0.3)
uh.rotation(180)

binaryDict = {'1': (255, 255, 255), '0': (0,0,0)}
hours = {'1': (255,0,0), '0': (0,0,0)}
mins = {'1': (255,0,0), '0': (0,0,0)}
secs= {'1': (255,0,0), '0': (0,0,0)}
white = (0,0,0)

while True:
    Now = dt.now(london).strftime('%H%M%S')
    Time = main()

    matrix = [
            [hours[Time.split()[0][0]], hours[Time.split()[0][1]], white, mins[Time.split()[0][2]], mins[Time.split()[0][3]], white, secs[Time.split()[0][4]], secs[Time.split()[0][5]]],
            [hours[Time.split()[1][0]], hours[Time.split()[1][1]], white, mins[Time.split()[1][2]], mins[Time.split()[1][3]], white, secs[Time.split()[1][4]], secs[Time.split()[1][5]]],
            [hours[Time.split()[2][0]], hours[Time.split()[2][1]], white, mins[Time.split()[2][2]], mins[Time.split()[2][3]], white, secs[Time.split()[2][4]], secs[Time.split()[2][5]]],
            [hours[Time.split()[3][0]], hours[Time.split()[3][1]], white, mins[Time.split()[3][2]], mins[Time.split()[3][3]], white, secs[Time.split()[3][4]], secs[Time.split()[3][5]]],
            [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
            [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
            [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
            [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]
                                                                        ]
    uh.set_pixels(matrix)
    uh.show()

    time.sleep(1)

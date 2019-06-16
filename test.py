import RPi.GPIO as gp
import time

print('Start')
bulb = [26, 19, 13]
gp.setmode(gp.BCM)
for i in range(4):
    for b in bulb:
        gp.setup(b, gp.OUT)
        gp.output(b, True)
        time.sleep(0.3)
        gp.output(b, False)
print('End')
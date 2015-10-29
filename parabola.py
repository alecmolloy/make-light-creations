import math
for x in range(0, WIDTH):
    for y in range(0, HEIGHT):
        if (y > .75 * math.pow(x - (WIDTH / 2),2)):
            light.on((x,y), 7 * y / HEIGHT + 2)

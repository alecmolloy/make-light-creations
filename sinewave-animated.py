import math
sx = 0
while True:
    for x in range(0, WIDTH):
        for y in range(0, HEIGHT):
            ay = y - HEIGHT / 2
            if ay >= (math.sin((x + sx)) * 3):
                light.on((x, y), 7 * y / HEIGHT)
            else:
                light.off((x,y))
    sx += 1

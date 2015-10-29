import math
for x in range(0, WIDTH):
    for y in range(0, HEIGHT):
        ay = y + HEIGHT / 2
        if (math.sin(ay / 2) * 3) <= y:
            light.on((x, y), int(y / HEIGHT))

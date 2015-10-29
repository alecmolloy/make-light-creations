x = 0
dx = 1
while True:
    light.off((x - (dx * 3),7))
    light.on((x - (dx * 2),7), 2)
    light.on((x - dx,7), 4)
    x+=dx
    light.on((x,7))
    if x == WIDTH + 2 or x == -3:
        dx *= -1

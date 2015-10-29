for x in range(0, WIDTH):
    for y in range(0, HEIGHT):
        light.on((x,y), 7 * y / HEIGHT)

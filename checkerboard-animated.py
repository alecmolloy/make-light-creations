i = 0
while True:
    for x in range(0, WIDTH):
        for y in range(0, HEIGHT):
            if ((i+ y + x) % 2):
                light.on((x,y))
            else:
                light.off((x,y))
    i+=1

x = 0
dx = 1
while True:
    light.line(
        (x - (dx * 5),0),
        (x - (dx * 5),HEIGHT - 1 ),
        off)
    light.line(
        (x - (dx * 4), 0),
        (x - (dx * 4), HEIGHT - 1 ),
        2)
    light.line(
        (x - (dx * 3), 0),
        (x - (dx * 3), HEIGHT - 1 ),
        3)
    light.line(
        (x - (dx * 2), 0),
        (x - (dx * 2), HEIGHT - 1 ),
        4)
    light.line(
        (x - (dx * 1), 0),
        (x - (dx * 1), HEIGHT - 1 ),
        5)
    light.line(
        (x, 0),
        (x, HEIGHT - 1 ),
        7)
    x+=dx
    if x == WIDTH + 5 or x == -6:
        dx *= -1

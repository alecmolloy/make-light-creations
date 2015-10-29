x = 0
y = 0
dx = 0
dy = 0
brightness = 7
while True:
    light.line(E8,(x,y), brightness)
    if x is WIDTH - 1 and y is 0:
        dx = 0
        dy = 1
    if x is WIDTH -1 and y is HEIGHT - 1:
        dx = -1
        dy = 0
    if x is 0 and y is HEIGHT - 1:
        dx = 0
        dy = -1
    if x is 0 and y is 0:
        dx = 1
        dy = 0
    if x is 0 and y is 0:
        brightness -= 1
    if brightness <= -1:
	     brightness = 7
    x += dx
    y += dy

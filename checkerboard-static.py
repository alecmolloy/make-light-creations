for x in range(0, WIDTH):
	for y in range(0, HEIGHT):
		if ((y + x) % 2):
			light.on((x,y))

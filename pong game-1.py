import pygame as pg

pg.init()

# variables
WIDTH = 800
HEIGHT = 600
TITLE = "The C2 Pong"

# colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# Base setup
screen = pg.display.set_mode((WIDTH, HEIGHT))                # screen setup
pg.display.set_caption(TITLE)                                # title setup

# game loop
game_running = True
while game_running:
	# process section
	for event in pg.event.get():
		if event.type == pg.QUIT:
			game_running = False

	# draw section
	screen.fill(BLUE)

	# update section
	pg.display.update()
	
pg.quit()


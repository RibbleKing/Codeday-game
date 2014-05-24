#!/usr/bin/env python
import random
import os, sys
import pygame
from pygame.locals import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image


pygame.init()
screen = pygame.display.set_mode((720, 480))
pygame.display.set_caption('A Game')
pygame.mouse.set_visible(0)

clock = pygame.time.Clock()

def main():
	img = load_image("game.jpg")

	pos_x = random.randint(0,100) 
	pos_y = random.randint(0,100)

	pos_dx = random.randint(1,2)
	pos_dy = random.randint(1,2)
	while 1:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == QUIT:
				return
			elif event.type == KEYDOWN and event.key == K_ESCAPE:
				return

		pos_x = pos_x + pos_dx
		pos_y = pos_y + pos_dy
	
		if pos_x < 0 or pos_x > 100:
			pos_dx = -pos_dx

		if pos_y < 0 or pos_y > 100:
			pos_dy = -pos_dy


		screen.blit(img, (pos_x, pos_y))
		#render frame!
	
		pygame.display.flip()


if __name__ == "__main__":
	main()

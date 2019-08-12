import pygame
from pygame import * 

PLATFORM_WIDTH = 60
PLATFORM_HEIGHT = 60
PLATFORM_COLOR = "#FF6262"

class Platform(sprite.Sprite):
	def __init__(self, x, y , numb):
		sprite.Sprite.__init__(self)
		#self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
		#self.image.fill(Color(PLATFORM_COLOR))
		witch = (pygame.image.load("bg.png"), pygame.image.load("bg2.png"))
		self.image =witch[numb] 
		self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
import pygame
from pygame import *

S_SPEED = 4
PR_WIDTH = 37 
PR_HEIGHT = 60


class Player(sprite.Sprite):
	def __init__(self, x , y):
		sprite.Sprite.__init__(self)
		self.xvel = 0 
		self.yvel = 0 
		self.startX = x 
		self.startY = y
		#self.image = Surface((PR_WIDTH , PR_HEIGHT))
		self.image = pygame.image.load("im1.png")
		#p_av = pygame.image.load("im1.png")
		#self.image.blit(p_av , (x ,y))
		self.rect = Rect(x, y , PR_WIDTH , PR_HEIGHT)

	def update(self, left, right, up, down, platforms):
		if left and up:
			print("left up") 
			self.xvel = -S_SPEED//2
			self.yvel = -S_SPEED//2
		if right and up:
			print("right up")
			self.xvel = S_SPEED//2
			self.yvel = -S_SPEED//2
		if left and down:
			print("left down")
			self.xvel = -S_SPEED//2
			self.yvel = S_SPEED//2
		if right and down:
			print("right down") 
			self.xvel = S_SPEED//2
			self.yvel = S_SPEED//2
		if left:
			print("left")
			self.xvel = -S_SPEED
		if right:
			print("right")
			self.xvel = S_SPEED
		if up:
			print("up")
			self.yvel = -S_SPEED
		if down:
			print("down")
			self.yvel = S_SPEED
		if not(left or right or up or down): # стоим, когда нет указаний идти
			self.xvel = 0
			self.yvel = 0

		self.rect.y += self.yvel
		self.collide(0 , self.yvel , platforms)

		self.rect.x += self.xvel
		self.collide(self.xvel , 0 , platforms)


	def draw(self , screen):
		screen.blit(self.image , (self.rect.x , self.rect.y))

	def collide(self , xvel , yvel , platforms):
		for p in platforms: 
			if sprite.collide_rect(self,p):
				if xvel > 0:
					self.rect.right = p.rect.left
				if xvel < 0:
					self.rect.left = p.rect.right
				if yvel > 0:
					self.rect.bottom = p.rect.top
				if yvel < 0:
					self.rect.top = p.rect.bottom



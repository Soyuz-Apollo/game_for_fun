import pygame 
from pygame import *
import player
import blocks

WinWidth = 1200
WinHeight = 600
DISPLAY = (WinWidth, WinHeight)
BACKGROUND_COLOR = "#004400"
PL_WIDTH = 60 
PL_HEIGHT = 60

class Camera(object):
	"""docstring for Camera"""
	def __init__(self, camera_func , width , height):
		self.camera_func  = camera_func
		self.state = Rect(0,0,width , height)
		
	def apply(self , target):
		return target.rect.move(self.state.topleft)

	def update(self , target):
		self.state = self.camera_func(self.state , target.rect)

def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l+WinWidth / 2, -t+WinHeight / 2

    l = min(0, l)                           # Не движемся дальше левой границы
    l = max(-(camera.width- WinWidth), l)   # Не движемся дальше правой границы
    t = max(-(camera.height- WinHeight), t) # Не движемся дальше нижней границы
    t = min(0, t)                           # Не движемся дальше верхней границы

    return Rect(l, t, w, h)




def main(): 
	pygame.init()
	screen = pygame.display.set_mode(DISPLAY)
	pygame.display.set_caption("PAOWL'S TRIP")
	bg = Surface(DISPLAY)
	hero = player.Player(75 , 75)
	entities = pygame.sprite.Group()
	platforms = []
	level = [
       "----------------------------------",
       "-                                -",
       "-                       --       -",
       "-                                -",
       "-            --                  -",
       "-                                -",
       "--                               -",
       "-                                -",
       "-                   ----     --- -",
       "-                                -",
       "--                               -",
       "-                                -",
       "-                            --- -",
       "-                                -",
       "-                                -",
       "-      ---                       -",
       "-                                -",
       "-   -------         ----         -",
       "-                                -",
       "-                         -      -",
       "-                            --  -",
       "-                                -",
       "-                                -",
       "----------------------------------"]  
	
	timer = pygame.time.Clock()
	bcgd_im = pygame.image.load("bg.png")
	bcgd_im_2 = pygame.image.load("bg2.png")
	x = y = 0
	for row in level:
		for col in row:
			if col == "-":
				pl = blocks.Platform(x, y, 0)
				entities.add(pl)
				platforms.append(pl)
				#bg.blit(bcgd_im_2 , (x , y))
			else:
				pl = blocks.Platform(x, y , 1)
				entities.add(pl)
				#bg.blit(bcgd_im_2 , (x , y))
			x += PL_WIDTH
		y += PL_HEIGHT
		x = 0

	entities.add(hero)
	total_level_width  = len(level[0])*PL_WIDTH # Высчитываем фактическую ширину уровня
	total_level_height = len(level)*PL_HEIGHT   # высоту

	camera = Camera(camera_configure, total_level_width, total_level_height)

	run = True
	left = right = up = down = False
	while run:
		timer.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == KEYDOWN and event.key == K_LEFT:
				left = True
				right = False
				up = False
				down = False
			if event.type == KEYDOWN and event.key == K_RIGHT:
				right = True
				left = False
				up = False
				down = False
			if event.type == KEYUP and event.key == K_RIGHT:
				right = False
				left = False
				up = False
				down = False
			if event.type == KEYUP and event.key == K_LEFT:
				left = False
				right = False
				up = False
				down = False
			if event.type == KEYDOWN and event.key == K_UP:
				up = True
				left = False
				right = False
				down = False
			if event.type == KEYUP and event.key == K_UP:
				up = False
				left = False
				right = False
				down = False
			if event.type == KEYDOWN and event.key == K_DOWN:
				down = True
				left = False
				right = False
				up = False
			if event.type == KEYUP and event.key == K_DOWN:
				down = False	
				left = False
				right = False
				up = False
					

		#screen.blit(bg,camera.apply(blocks.Platform(0,0)))###########################################
		#entities.draw(screen)
		for event in entities:
			screen.blit(event.image, camera.apply(event))
		#hero.draw(screen)
		camera.update(hero)
		hero.update(left , right , up, down, platforms)

		pygame.display.update()

if __name__ == "__main__":
	main()		
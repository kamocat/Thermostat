import pygame
import time

screen = pygame.display.set_mode((160,160))
icons = pygame.image.load('icons-small.png').convert_alpha()
dims = (icons.get_width()/5, icons.get_height()/5)

def weather( index ):
	x = (index % 5) * dims[0]
	y = int(index / 5) * dims[1]
#	print("x = ",x , "y = ", y)
	sunny = icons.subsurface(((x,y),dims))
	sunny = sunny.subsurface(sunny.get_bounding_rect())
	centered = (80 - sunny.get_width()/2, 150-sunny.get_height())
	screen.fill((200,200,255))
	screen.blit(sunny, centered)
	pygame.display.flip()
	
for i in range(24):
	weather( i )
	time.sleep(1)
	
pygame.quit()
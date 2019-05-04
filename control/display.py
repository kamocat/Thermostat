import pygame
from datetime import datetime
import os

os.putenv('SDL_FBDEV', '/dev/fb1')

pygame.init()
size = [320,240]
screen = pygame.display.set_mode(size)
pygame.mouse.set_visible(False)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 0, 0)
GREEN = (0,255,0)
BLUE = (0,0,255)
screen.fill(WHITE)
pygame.display.flip()

#bigfont = pygame.font.Font(None, 100)
bigfont = pygame.font.SysFont("Dejavusans", 100)
medfont = pygame.font.SysFont("Dejavusans", 32)
smallfont = pygame.font.SysFont("Dejavusans", 24)
time_rect = (0,0,160,50)
dt_rect = (210,0,100,50)
ct_rect = (10,100,140,140)
weather_rect = (160,60,160,180)

def update( desired_temp, actual_temp ):
	time_text = datetime.now().strftime('%I:%M %p')
	b = smallfont.render(time_text, True, BLACK)
	screen.fill(WHITE, time_rect)
	screen.blit(b, [10,2])

	b = smallfont.render(desired_temp, True, BLACK)
	screen.fill(WHITE, dt_rect)
	screen.blit(b, [210,2])

	btarget = bigfont.render(actual_temp, True, BLACK)
	screen.fill(WHITE, ct_rect)
	screen.blit(btarget, [10,100])
	
	pygame.display.update((time_rect, dt_rect, ct_rect))

def weather():
	bweather = medfont.render("sunny", True, BLACK)
	screen.fill(WHITE, weather_rect)
	screen.blit(bweather, [170,60])
	pygame.display.update(weather_rect)


#update('50', '60')

import pygame
from datetime import datetime
import os

try:
	fh = open('/dev/fb1')
	# Use framebuffer 1, instead of the default
	os.putenv('SDL_FBDEV', '/dev/fb1')
except FileNotFoundError:
	# Not using fb1. Keep default settings
	print("Using default video settings")
except PermissionError:
	print("Please fix permissions on /dev/fb1")

pygame.init()
size = [320,240]
screen = pygame.display.set_mode(size)
pygame.mouse.set_visible(False)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 0, 0)
GREEN = (0,255,0)
BLUE = (0,0,255)
DARK = (50,50,50)
screen.fill(WHITE)
pygame.display.flip()
import weather

bigfont = pygame.font.SysFont("Dejavusans", 100)
medfont = pygame.font.SysFont("Dejavusans", 72)
smallfont = pygame.font.SysFont("Dejavusans", 36)
time_rect = (0,0,240,50)
dt_rect = (260,0,60,50)
ct_rect = (10,100,140,140)
weather_rect = (160,60,160,180)

def update( desired_temp, actual_temp ):
	time_text = datetime.now().strftime('%I:%M %p')
	b = medfont.render(time_text, True, BLACK)
	screen.fill(WHITE, time_rect)
	screen.blit(b, [10,2])

	b = smallfont.render(desired_temp, True, BLACK)
	screen.fill(WHITE, dt_rect)
	screen.blit(b, [260,2])

	btarget = bigfont.render(actual_temp, True, BLACK)
	screen.fill(WHITE, ct_rect)
	screen.blit(btarget, [10,100])
	
	pygame.display.update((time_rect, dt_rect, ct_rect))

def outside():
	w = screen.subsurface(weather_rect)
	weather.icon(w, 3)
	latest = weather.text()
	bweather = smallfont.render(latest["text"], True, DARK)
	w.blit(bweather, [10,0])
	bweather = smallfont.render(latest["temperature"], True, DARK)
	w.blit(bweather, [10,40])
	pygame.display.update(weather_rect)

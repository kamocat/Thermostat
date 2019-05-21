import pygame
if( pygame.display.get_init() ):
	icons = pygame.image.load('icons-small.png').convert_alpha()
	dims = (icons.get_width()/5, icons.get_height()/5)

import urllib.request
import json

city = "Corvallis,us"
# Note: this is using my personal key from openweathermap. Please use your own key.
key = "e7ff1922140bf0166a2a54cdcb445e78"
url = "http://api.openweathermap.org/data/2.5/weather"
req = "?q="+city+"&APPID="+key
req=urllib.request.Request(url+req)

def KtoF( x ):
	return str(round(((float(x)-273.15) * 1.8 + 32), 1))

def text():
	f = urllib.request.urlopen(req)
	t = "(url error)"
	contents = json.loads(f.read().decode('utf-8'))
	t = contents["main"]["temp"]
	t = KtoF(t) # Convert to Farenheight
	desc = contents["weather"][0]["description"]
	result = {"temperature" : t, "text" : desc}
	return( result )

def icon( w, index ):
	x = (index % 5) * dims[0]
	y = int(index / 5) * dims[1]
	sky = icons.subsurface(((x,y),dims))
	sky = sky.subsurface(sky.get_bounding_rect())
	centered = (w.get_width()/2 - sky.get_width()/2, w.get_height()-10-sky.get_height())
	w.fill((255,255,255))
	w.blit(sky, centered)

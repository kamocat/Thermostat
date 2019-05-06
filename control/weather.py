import pygame

icons = pygame.image.load('icons-small.png').convert_alpha()
dims = (icons.get_width()/5, icons.get_height()/5)

import urllib.request
import json

# This gets the latest Corvallis weather. Change the station to
# your nearest airport for local weather
# https://www.weather.gov/arh/stationlist
req = urllib.request.Request("https://api.weather.gov/stations/CRVO/observations/latest")

def text():
	contents = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))
	t = contents["properties"]["temperature"]["value"]
	# Converting to Farenheight
	t = str(round((float(t) * 9.0/5 + 32), 1))
	desc = contents["properties"]["textDescription"]
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

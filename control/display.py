import pygame
import time

pygame.init()
size = [320,240]
screen = pygame.display.set_mode(size)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 0, 0)
GREEN = (0,255,0)
BLUE = (0,0,255)
screen.fill(WHITE)

#bigfont = pygame.font.Font(None, 100)
bigfont = pygame.font.SysFont("Dejavusans", 100)
medfont = pygame.font.SysFont("Dejavusans", 32)
smallfont = pygame.font.SysFont("Dejavusans", 24)

btime = smallfont.render("10:00 AM", False, BLACK)
screen.blit(btime, [10,2])

bcurrent = smallfont.render("70", False, BLACK)
screen.blit(bcurrent, [210,2])

btarget = bigfont.render("55", False, BLACK)
screen.blit(btarget, [10,100])

bweather = medfont.render("sunny", False, BLACK)
screen.blit(bweather, [170,100])

pygame.display.flip()

# Loop until the user clicks the close button
done = False
clock = pygame.time.Clock()
while not done:
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)
     
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

pygame.quit()
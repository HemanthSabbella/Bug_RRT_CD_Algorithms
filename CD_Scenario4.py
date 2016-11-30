import pygame
import sys
from pygame.locals import *
white = (255,255,255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
black = (0, 0, 0)
yellow = (255, 255, 0)
frame = pygame.display.set_mode((200, 200)) #scaled by 10
pygame.display.set_caption('Trapezoidal decomposition')
frame.fill(white)

x = 0;
y = 0;

while True:
	pygame.draw.line(frame,red,[40, 120], [100, 50],2)
	pygame.draw.line(frame,red,[100, 50], [150, 120],2)
	pygame.draw.line(frame,red,[40, 120], [90, 90],2)
	pygame.draw.line(frame,red,[90, 90], [150, 120],2)
	pygame.draw.line(frame,red,[100, 50], [60, 30],2)
	pygame.draw.line(frame,red,[60, 30], [30, 60],2)
	pygame.draw.line(frame,red,[30, 60], [70, 80],2)
	pygame.draw.rect(frame, white, [x, 0, 2, 200])
	x = x + 0.001
	pygame.draw.rect(frame, blue, [x, 0, 2, 200])
	#print x
	if(x > 30):
		pygame.draw.rect(frame, yellow, [30, 0, 2, 200])
	if(x > 60):
		pygame.draw.rect(frame, yellow, [60, 0, 2, 30])
	if(x > 40):
		pygame.draw.rect(frame, yellow, [40, 65, 2, 200])
	if(x > 90):
		pygame.draw.rect(frame, yellow, [90, 90, 2, 200])
	if(x > 100):
		pygame.draw.rect(frame, yellow, [100, 0, 2, 50])
	if(x >150):
		pygame.draw.rect(frame, yellow, [150, 0, 2, 200])
	#pygame.draw.Rect(frame,red,[200, 300], [450, 600],5)
	for event in pygame.event.get():
		print event
		if event.type == QUIT: 
			pygame.quit()
			sys.exit()
	pygame.display.update()

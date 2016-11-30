#Assignment 1
# Group Members:
# Diljyot Singh Jaura
# Hemanth Sabbella 
import pygame
import sys
import math
from pygame.locals import *
#imgx = int(input('Start x:'))
#imgy = int(input('Start y:'))
#imgp = int(input('End x:'))
#imgq = int(input('End y:'))
imgx = 1	#initial point x
init_x = imgx
imgy = 1	#initial point y
init_y = imgy
imgp = 251	#end points x

imgq = 301	#end point y



pygame.init()
white = (255,255,255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
black = (0, 0, 0)
setDisplay = pygame.display.set_mode((1200,800))
pygame.display.set_caption('Bug0')
setDisplay.fill(white)
#pygame.draw.line(setDisplay, blue, (389,200),(300,70),4)
pygame.draw.rect(setDisplay, black, [50, 130, 100, 40])
img = pygame.image.load('dot2.png')
img1 = pygame.image.load('dot1.png')

pygame.draw.rect(setDisplay, black, [150, 190, 100, 40])
pixObj = pygame.PixelArray(setDisplay)
FPS =30
pixObj[100][130] = black
pixObj[200][130] = black
pixObj[200][170] = black
pixObj[100][170] = black
del pixObj
fpsTime = pygame.time.Clock()
setDisplay.blit(img1, (imgp, imgq))

slope = float(float(imgq - imgy)/(imgp - imgx))
print slope
a = abs(40*float(float(math.cos(slope))/float(math.sin(slope))))
count = 0;
#print a
while True:


	if(imgx < imgp):
			imgx = imgx + 1

	if(imgy < imgq ):
			imgy = imgy + slope

	if( 50 < imgx < 150 and 130 < imgy < 170):
		imgx1 = imgx
		imgy1 = imgy
		imgx2 = imgx
		imgy2 = imgy
		#print imgx
		g=50
		for b in range(imgx,150):
			#count = count + 1
			imgx = imgx + 1
			setDisplay.blit(img, (imgx, imgy))

		for c in range(int(imgy), 170):
			imgy = imgy + 1
			setDisplay.blit(img, (imgx, imgy))

		for d in range(imgx1, 125):
			imgx = imgx - 1
			setDisplay.blit(img, (imgx, imgy))

	if( 150 < imgx < 250 and 190 < imgy < 230):
		imgx1 = imgx
		imgy1 = imgy
		for b in range(imgx,250):
			imgx = imgx + 1
			setDisplay.blit(img, (imgx, imgy))

		for c in range(int(imgy), 230):
			imgy = imgy + 1
			setDisplay.blit(img, (int(imgx), imgy))

		for d in range(imgx1, 125):
			imgx = imgx - 1
			setDisplay.blit(img, (imgx, imgy))
		
	setDisplay.blit(img1, (imgp, imgq))

	setDisplay.blit(img, (imgx, imgy))
	
	for event in pygame.event.get():
		print event
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
	fpsTime.tick(FPS)


#Assignment 2
#Group Members
#Hemanth Sabbella 2013152
#Aneesh Kumar - 2013126

import pygame, sys, random
import math 
from pygame.locals import *
pygame.init()
white = (255,255,255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
black = (0, 0, 0)
yellow = (255, 255, 0)
start_pointx = 30
start_pointy = 20
end_pointx = 600
end_pointy = 400
delta = 7
small_rect = 5 
frame = pygame.display.set_mode((700, 500))
pygame.display.set_caption('RRT algorithm')
frame.fill(black)
rect1 = pygame.Rect(200, 30, 80, 300)
rect2 = pygame.Rect(400, 250, 80, 80)
rect3 = pygame.Rect(400, 100, 140, 80)
rect4 = pygame.Rect(80, 250, 80, 140)
start = pygame.Rect(start_pointx, start_pointy, small_rect, small_rect)
end = pygame.Rect(end_pointx, end_pointy, small_rect, small_rect)

pygame.draw.rect(frame, white, [200, 30, 80, 300])
pygame.draw.rect(frame, white, [400, 250, 80, 80])
pygame.draw.rect(frame, white, [400, 100, 140, 80])
pygame.draw.rect(frame, white, [80, 250, 80, 140])
pygame.draw.rect(frame, red, [start_pointx, start_pointy, 10, 10])
pygame.draw.rect(frame, blue, [end_pointx, end_pointy, 10, 10])
#Function colliderect() is used to check whether two rectangles overlapping or not.

old_point = []
new_point = []	
points = []
points.append((start_pointx, start_pointy))
#points.append((end_pointx, end_pointy))

def distance(randx, randy):
	count = 0
	for i in points:
		count = count + 1
		if(count == 1):
			smallest = (randx - i[0])**2 + (randy - i[1])**2
			a = i
		elif(count > 1):
			if(smallest > (randx - i[0])**2 + (randy - i[1])**2):
				smallest = (randx - i[0])**2 + (randy - i[1])**2
				a = i
	return a

def newnode(randx, randy, nearest_point):
	angle = math.atan((randy - nearest_point[1])/(randx - nearest_point[0]))
	new_point.append((nearest_point[0] + delta*math.cos(angle), nearest_point[1] + delta*math.sin(angle)))
	return new_point 
x_old = start_pointx
y_old = start_pointy

while True:
	randx = random.random()*700
	randy = random.random()*500
	nearest_point = distance(randx, randy)
	
	new_point = []
	new_point = newnode(randx, randy, nearest_point)
	x = int(new_point[0][0])
	y = int(new_point[0][1])
	objects = pygame.Rect(x, y, small_rect, small_rect)
	if not objects.colliderect(rect1) and not objects.colliderect(rect2) and not objects.colliderect(rect3)  and not objects.colliderect(rect4):
		pygame.draw.rect(frame, green, [int(new_point[0][0]), int(new_point[0][1]), small_rect, small_rect])
		points.append((new_point[0]))
		#pygame.draw.line(frame, yellow,(x_old, y_old),(x,y),2)
	if objects.colliderect(end):
		pygame.display.update()
		break
	#pygame.draw.line(frame, green, (int(old_point[0][0]), int(old_point[0][1])), (int(new_point[0][0]), int(new_point[0][1])), 1)
	for event in pygame.event.get():
		if event.type == QUIT: 
			pygame.quit()
			sys.exit()

	pygame.display.update()
	x_old = new_point[0][0]
	y_old = new_point[0][1]

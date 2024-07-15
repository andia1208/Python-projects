from math import *
from random import random

numberofpoints_circle = 0
total_numberpoints = 0

while True:
	A_x = random()*2-1  #Generates a random x-coordinate in the range [-1, 1[
	A_y = random()*2-1
	if sqrt(A_x**2+A_y**2)<=1:	# Checks if the distance of the point A from the origin is less than or equal to 1. If yes, the point IS inside the unit circle.
		numberofpoints_circle += 1
	total_numberpoints += 1
	#calculates and print an estimate number of pi
	#pproximates the ratio of the area of the unit circle to the area of the enclosing square
	#area circle/area square= pi*r*r/ 4*r*r=pi/4
	print(4*numberofpoints_circle /total_numberpoints)

input(':')



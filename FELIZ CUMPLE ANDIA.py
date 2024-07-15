

# depends on graphics lib
# URL: https://pypi.org/project/graphics.py/

# The winsound dependency makes it only work in windows

# the keyboard dependency is useless


import graphics
from time import sleep
# import keyboard
from winsound import *
from math import cos
import threading
def song():
	Beep(262,750)
	Beep(262,250)
	Beep(294,1000)
	Beep(262,1000)
	
	Beep(349,1000)
	Beep(330,2000)
	
	
	Beep(262,750)
	Beep(262,250)
	Beep(294,1000)
	Beep(262,1000)
	
	Beep(392,1000)
	Beep(349,2000)
	
	
	Beep(262,750)
	Beep(262,250)
	Beep(523,1000)
	Beep(440,1000)
	Beep(349,1000)
	Beep(330,1000)
	Beep(294,1000)
	
	Beep(466,750)
	Beep(466,250)
	Beep(440,1000)
	Beep(349,1000)
	
	Beep(392,1000)
	Beep(349,2000)

win = graphics.GraphWin('',300,185)
fel=[
graphics.Text(graphics.Point(50,100),'H'),
graphics.Text(graphics.Point(60,100),'A'),
graphics.Text(graphics.Point(70,100),'P'),
graphics.Text(graphics.Point(77,100),'P'),#
graphics.Text(graphics.Point(85,100),'Y'),
graphics.Text(graphics.Point(90,100),' '),
graphics.Text(graphics.Point(100,100),'B'),
graphics.Text(graphics.Point(110,100),'-'),#
graphics.Text(graphics.Point(122,100),'D'),
graphics.Text(graphics.Point(133,100),'A'),
graphics.Text(graphics.Point(142,100),'Y'),
#graphics.Text(graphics.Point(151,100),'A'),

graphics.Text(graphics.Point(160,100),' '),
graphics.Text(graphics.Point(170,100),'A'),
graphics.Text(graphics.Point(178,100),'N'),#
graphics.Text(graphics.Point(187,100),'D'),
graphics.Text(graphics.Point(197,100),'I'),
graphics.Text(graphics.Point(210,100),'A'),

]
borde1 = [
graphics.Text(graphics.Point(50,70),'_'),
graphics.Text(graphics.Point(60,70),'_'),
graphics.Text(graphics.Point(70,70),'_'),
graphics.Text(graphics.Point(77,70),'_'),#
graphics.Text(graphics.Point(85,70),'_'),
graphics.Text(graphics.Point(90,70),'_'),
graphics.Text(graphics.Point(100,70),'_'),
graphics.Text(graphics.Point(110,70),'_'),#
graphics.Text(graphics.Point(122,70),'_'),
graphics.Text(graphics.Point(133,70),'_'),
graphics.Text(graphics.Point(142,70),'_'),
graphics.Text(graphics.Point(151,70),'_'),
graphics.Text(graphics.Point(160,70),'_'),
graphics.Text(graphics.Point(170,70),'_'),
graphics.Text(graphics.Point(178,70),'_'),
graphics.Text(graphics.Point(187,70),'_'),
graphics.Text(graphics.Point(197,70),'_'),
graphics.Text(graphics.Point(210,70),'_')#,
#graphics.Text(graphics.Point(220,80),'|')
]

borde2 = [
graphics.Text(graphics.Point(50,130),'_'),
graphics.Text(graphics.Point(59,130),'_'),
graphics.Text(graphics.Point(68,130),'_'),
graphics.Text(graphics.Point(77,130),'_'),#
graphics.Text(graphics.Point(86,130),'_'),
graphics.Text(graphics.Point(95,130),'_'),
graphics.Text(graphics.Point(104,130),'_'),
graphics.Text(graphics.Point(113,130),'_'),#
graphics.Text(graphics.Point(122,130),'_'),
graphics.Text(graphics.Point(131,130),'_'),
graphics.Text(graphics.Point(140,130),'_'),
graphics.Text(graphics.Point(149,130),'_'),
graphics.Text(graphics.Point(158,130),'_'),
graphics.Text(graphics.Point(167,130),'_'),
graphics.Text(graphics.Point(176,130),'_'),
graphics.Text(graphics.Point(185,130),'_'),
graphics.Text(graphics.Point(194,130),'_'),
graphics.Text(graphics.Point(203,130),'_')#,
#graphics.Text(graphics.Point(220,130),'|')
]
lado = [


graphics.Text(graphics.Point(43,80),'|'),
graphics.Text(graphics.Point(43,95),'|'),
graphics.Text(graphics.Point(43,110),'|'),
graphics.Text(graphics.Point(43,125),'|'),
graphics.Text(graphics.Point(43,140),'|'),
graphics.Text(graphics.Point(43,155),'|'),
graphics.Text(graphics.Point(43,170),'|')
]
_song = threading.Thread(target=song, daemon=True)
for l in lado:
	l.draw(win)
for l in fel:
	l.draw(win)
for b in borde1:
	b.draw(win)
for b in borde2:
	b.draw(win)
_song.start()
t=0
while True:
	k=0
	for l in fel[1:]:
		if k+t/3>0:
			l.move(0,2*cos(k+t/3))
		k-=1
	k=0
	for b in borde1[1:]:
		if k+t/3>0:
			b.move(0,2*cos(k+t/3))
		k-=1
	k=0
	for b in borde2[1:]:
		if k+t/3>0:
			b.move(0,2*cos(k+t/3))
		k-=1
	sleep(0.02)
	if win.isClosed() or not _song.is_alive():
		break
	t +=1

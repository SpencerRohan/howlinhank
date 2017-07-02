import pygame
import sys
from time import sleep
import subprocess

from omxplayer import OMXPlayer
global player
global screen
pygame.joystick.init()

# print pygame.joystick.get_count()

_joystick_right = pygame.joystick.Joystick(0)
_joystick_right.init()
_joystick_left = pygame.joystick.Joystick(1)
_joystick_left.init()
# print _joystick_right.get_init()
# print _joystick_right.get_id()
# print _joystick_right.get_name()
# print _joystick_right.get_numaxes()
# print _joystick_right.get_numballs()
# print _joystick_right.get_numbuttons()
# print _joystick_right.get_numhats()
# print '--------------------'
# print _joystick_left.get_init()
# print _joystick_left.get_id()
# print _joystick_left.get_name()
# print _joystick_left.get_numaxes()
# print _joystick_left.get_numballs()
# print _joystick_left.get_numbuttons()
# print _joystick_left.get_numhats()
pygame.init()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.mouse.set_visible(False)
background=pygame.image.load('/home/pi/Desktop/howlinhank/hankvids/faces/blink.jpg')
screen.fill((255,255,255))
pygame.display.flip()
player = False
done = False
button = ''
controller = ''
path = '/home/pi/Desktop/howlinhank/hankvids/'

movies = [[
			#LEFT
	    False, #FALSE, #QUIT!
	    'madandangry.mp4', #1R --- Top Back Left - Red 1
	    False, #FALSE,
	    False, #FALSE,
	    False, #FALSE,
	    False, #FALSE,
	    'sad.mp4', 					#6R ---- Bottom Back Left - Red 6
	    'happy.mp4', 				#2R --- Left Middle - Red 7 ##
	    'smile-brow.mp4', 	#FLY -- Bottom Front Left - Yellow 8
	    'wink-right.mp4', #s1Y --- Left Small - Yellow 9
	    'sunglasses.mp4', #s2R --- Left Small - Red 10
	    'round1.mp4', #TL -- Top Yellow Left 11
	    False, #FALSE,
    ],[

    	#RIGHT
	    'howard.mp4', 			#1R --- Top Back Right - Red 0
	    'weird.mp4', 				#6R --- Bottom Back Right - Red 1
	    'free-bird.mp4', 		#2Y --- back row top - Yellow 2
	    'hanktest.mp4', 		#7Y
	    'heart.mp4', 				#5R --- Front row - red 4
	    'sleep.mp4', 				#4R --- Back row - red 5
	    'conman.mp4', 				#3Y --- Top front row right - yellow 6 ##
	    'shock.mp4', 	#8Y --- bottom front row right - yellow 7
	    'round2.mp4',				#TR --- Top Right - Yellow 8 -- ROUND 2!
	    '3dglasses.mp4', 		#s2R -- Right Small - red 9
	    'mustache.mp4', 		#FRY --- Bottom Front Right - yellow 10
	    'wink-left.mp4', 		#s1Y --- Small right yellow 11 ##
	    False, #FALSE, #12
    ]
	]

	#shock.mp4
	#over-it.mp4
	#moon




#LEFT
	# Top(TL)            (1R)
	#  (s1Y)   (X)
	# (s2R)   (2R)
	# (FLY)     (X)       (3R)

#RIGHT
	# (1R)          TOP: (TR)
	#      (2Y) (X) (3Y)  (s1Y)
	#    (X) (4R)  (5R)  (X)   (s2R)
	# (6R)    (7Y) (X) (8Y)     (FRY)


#con-man
#sleep
#sad
#over-it
#hanktest


quit_video = False

while done==False:
  for event in pygame.event.get():
		if event.type == pygame.JOYBUTTONDOWN:
			button = event.button
			controller = event.joy
			movie_file = movies[controller][button]
			if quit_video == True:
				if button == 0 and controller == 0:
					if player != False:
						player.quit()
					quit()
				else:
					if player.is_playing() and movie_file != False:
						try:
							player.load(path + movie_file, pause=False)
						except SystemError:
							player.quit()
							player = OMXPlayer(path + movie_file, ['--aspect-mode', 'fill'], pause=False)
			else:
				quit_video = True
				if movie_file != False:
					player = OMXPlayer(path + movie_file, ['--aspect-mode', 'fill'], pause=False)

import pygame
import time
import random

pygame.init() # this will be ended with pygame.quit() later

display_width = 600   
display_height = 400  

gameDisplay = pygame.display.set_mode((display_width,display_width)) # set width and height. 
pygame.display.set_caption('Going down Boulevard East')
pygame.mixer.music.load("Ducktales.wav") # background music 

#define colors in r,g,b format
black = (0,0,0)  #black is absence of any color
white = (255,255,255) #white has all colors
red = (255,0,0)
block_color = (49,121,255)
car_width = 80 # in pixels
clock = pygame.time.Clock() # set clock for fps settings

dogimg = pygame.image.load('dogtrp.png') # dogimg is a surface object with image drawn on it.

def things_dodged(count):
	dodge_text = pygame.font.SysFont(None,25)  # text font, text size
	dodge_surface = dodge_text.render(" Dodged: " + str(count),True, black)
	dodge_rect = dodge_surface.get_rect() 
	dodge_rect.center = ((display_width/10), (display_height/10)) 
	gameDisplay.blit(dodge_surface,dodge_rect)

def new_speed(speed):
	ns_text = pygame.font.SysFont(None,20) 
	ns_surface = ns_text.render("Speed(fps): " + str(speed),True, red)
	ns_rect = ns_surface.get_rect()
	ns_rect.center = ((display_width/10*9), (display_height/10))
	gameDisplay.blit(ns_surface,ns_rect)	

def things(thingx,thingy,thingw,thingh,color):   #stuff that car will avoid
	pygame.draw.rect(gameDisplay,block_color,[thingx,thingy,thingw,thingh]) # draws a box

def car(x,y):
	gameDisplay.blit(dogimg,(x,y)) 
# To "blit" is to copy bits from one part of a computer's graphical memory to another part. 
# This technique deals directly with the pixels of an image, and draws them directly to the screen,
# which makes it a very fast rendering technique that's often perfect for fast-paced 2D action games.
# see : https://gamedevelopment.tutsplus.com/articles/gamedev-glossary-what-is-blitting--gamedev-2247

def crash():
	pygame.mixer.music.stop()
	message_display('You Crashed') # calling another function here

def text_objects(text, font):
	textSurface = font.render(text, True, black) # render is Pygame object
	return textSurface, textSurface.get_rect() # get rect is Pygame method

def message_display(text):
	largeText = pygame.font.Font('freesansbold.ttf',90) 
	TextSurf,TextRect = text_objects(text,largeText) 
	TextRect.center = ((display_width/2), (display_height/2)) 
	gameDisplay.blit(TextSurf,TextRect)
	pygame.display.update() 
	time.sleep(2)
	game_loop() # .. and start the game again!

def game_loop():
	x = (display_width*.45) 
	y = (display_width*.80)
	x_change = 0
	thing_startx = random.randrange(0,display_width)
	thing_starty = -600 # starts 600 pixel off the screen
	thing_speed = 7 
	thing_width = 100
	thing_height = 100 # 100 by 100 box
	gameExit = False  # we have not crashed at the start of game
	dodged = 0
	speed = 30
	pygame.mixer.music.play(-1,0.0)

	while not gameExit:

		for event in pygame.event.get():  # event is any event 
		  
			if event.type == pygame.QUIT:  # if you press the 'x' on window
				pygame.quit()  # end the pygame.init()  method
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -5
				elif event.key == pygame.K_RIGHT:
					x_change = 5
	            
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0
	    
		x += x_change

		gameDisplay.fill(white)  # whatever was before gets filled with White

		things(thing_startx,thing_starty,thing_width,thing_height,black)
		thing_starty += thing_speed # every time we update a frame, we move it down by thing_speed

		car(x,y) 
		new_speed(speed)
		things_dodged(dodged)

		if x > (display_width - car_width)  or x < 0:
			crash()

		if thing_starty > display_height+thing_height+50: 
			thing_starty = 0 - thing_height 
			thing_startx = random.randrange(0,display_width) 
			dodged += 1
			speed += 2
			print(" new speed is {}".format(speed))

		if y < thing_starty+thing_height:
			if x > thing_startx and x < (thing_startx + thing_width) or (x+car_width) > thing_startx and (x+car_width) < (thing_startx + thing_width):
				crash()
			
		pygame.display.update()  
		clock.tick(speed)  

game_loop()
pygame.quit()  # end the pygame.init()  method
quit()
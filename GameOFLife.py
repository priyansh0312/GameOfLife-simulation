import pygame
import grid  #file that has all the logic code
import os 


os.environ["SDL_VIDEO_CENTERED"] = "1"

running = True
BACKGROUND = (42,21,13) # background color 
WIDHT,HEIGHT = 1440,900 # screen resolution 
resolution  = (WIDHT,HEIGHT)
FPS = 30 #frames per second

# initializing pygame
pygame.init()
pygame.display.set_caption("GAME OF LIFE") # sets the heading of the screen 

# setting up display
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()

# colors 
black = (0,0,0)
blue = (0,14,71)
white = (255,255,255)

scaler = 20

# creating a grid object
Grid = grid.Grid(WIDHT, HEIGHT, scaler) # making an object of type Grid 
Grid.create2DArray()


# while the game is runnnig 
def gameRunning():
	running = True
	while running:
		clock.tick(FPS)
		screen.fill(white)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running =  False 
	
		Grid.color(dead_color = white, live_color = black, surface = screen )

		pygame.display.update()
	pygame.quit()

gameRunning()




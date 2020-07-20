import pygame
import grid  #file that has all the logic code
import os 


os.environ["SDL_VIDEO_CENTERED"] = "1"

running = True
BACKGROUND = (42,21,13) # background color 
WIDHT,HEIGHT = 1440,900 #screen resolution 
resolution  = (WIDHT,HEIGHT)
FPS = 30 # frames per second

pygame.init()
pygame.display.set_caption("GAME OF LIFE") # sets the heading of the screen 

screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()

black = (0,0,0)
#blue = (0,14,71)
white = (255,255,255)

scaler = 20

# creating a gridr
Grid = grid.Grid(WIDHT, HEIGHT, scaler) # making an object of type Grid 
Grid.create2DArray()

# # mouse_on_grid():
# def mouse_on_grid(pos):
# 	pass

# def click_cell(pos):
# 	grid_pos = [pos[0]-100pos[1]-180] 
# 	grid_pos[0] = grid_pos[0]//20
# 	grid_pos[1] = grid_pos[1]//20  

# while the game is runnnig 
def gameRunning():
	running = True
	while running:
		clock.tick(FPS)
		screen.fill(white)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running =  False 
			# if event.type == pygame.MOUSEBUTTONDOWN:
			# 	mouse_pos = pygame.mouse.get_pos()
			# 	if mouse_on_grid(mouse_pos):
			# 		click_cell()

		Grid.color(dead_color = white, live_color = black, surface = screen )

		pygame.display.update()
	pygame.quit()
	# sys.exit()

gameRunning()




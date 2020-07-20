import pygame 
import numpy as np
from random import randint


class Grid:
	def __init__(self, width, height, resolution):
		self.resolution = resolution 
		self.cols = int(height/resolution)
		self.rows = int(width/resolution)
		self.size = (self.rows,self.cols)
		self.arr = np.ndarray(shape=(self.size))

	# creating a 2D array that hold random values - (0 and 1)
	def create2DArray(self):
		for i in range(self.rows):
			for j in range(self.cols):
				self.arr[i][j] = randint(0,1)

	
	# getting the number of the neighbours of a particular cell 
	def getNeighbours(self,i,j):
		count = 0
		for n in range(-1,2):
			for m in range(-1,2):

				#calculating the wrap around position of the next(+1,-1) cell
				row = (i+n+self.rows) % self.rows 
				col = (j+m+self.cols) % self.cols
				count+=self.arr[row][col]
		count-= self.arr[i][j] # we do not want to include the cell itself. 
		return count


	# making the next generation of the array : implementing rules to the cells 
	def next(self):
		next = np.ndarray(shape=(self.size))
		for i in range(self.rows):
			for j in range(self.cols):
				state = self.arr[i][j]
				neighbours = self.getNeighbours(i,j)

				# implementing the rules to the cell and assiging values to the current cell in another array.
				if state == 0 and neighbours == 3:
					next[i][j] = 1
				elif state == 1 and (neighbours<2 or neighbours>3):
					next[i][j] = 0
				else:
					next[i][j] = self.arr[i][j]
		self.arr = next 


	# assigning colors to the cells
	def color(self,dead_color,live_color,surface):
		for i in range(self.rows): 
			for j in range(self.cols):
				x_pos = i*self.resolution 
				y_pos = j*self.resolution

				# assigning the color to the cells based on their current values (1-live,0-dead)
				if self.arr[i][j] == 1:
					pygame.draw.rect(surface,live_color,[x_pos,y_pos,self.resolution-3,self.resolution-3])
				else:
					pygame.draw.rect(surface,dead_color,[x_pos,y_pos,self.resolution-3,self.resolution-3])

		self.next()

 

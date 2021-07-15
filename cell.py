import pygame
from const import *

class Cell:
    def __init__(self, x, y):
        """Initialize cell"""
        self.x = x
        self.y = y
        self.is_alive = False
        self.neighbours = []
        
    def set_neighbours(self, grid):
        """Set neighbours of the cell"""
        # get indexes of the cell on the grid
        x = self.x // CELL_SIZE
        y = self.y // CELL_SIZE
        
        # algorithm to append all neighbours to neighbours list
        if x-1 >= 0:
            self.neighbours.append(grid[y][x-1])
            if y-1 >= 0:
                self.neighbours.append(grid[y-1][x-1])
            if y+1 <= len(grid)-1:
                self.neighbours.append(grid[y+1][x-1])
        if x+1 <= len(grid[0])-1:
            self.neighbours.append(grid[y][x+1])
            if y-1 >= 0:
                self.neighbours.append(grid[y-1][x+1])
            if y+1 <= len(grid)-1:
                self.neighbours.append(grid[y+1][x+1])
        if y-1 >= 0:
            self.neighbours.append(grid[y-1][x])
        if y+1 <= len(grid)-1:
            self.neighbours.append(grid[y+1][x])

    def draw(self):
        """Draw the cell"""
        rect = pygame.Rect(self.x, self.y, CELL_SIZE, CELL_SIZE)    # get rectangle shape
        if not self.is_alive:                                       # if cell is not alive
            pygame.draw.rect(SCREEN, WHITE, rect, 0)                # draw a white rectangle
            pygame.draw.rect(SCREEN, GREY, rect, 1)                 # draw a grey border
        else:                                                       # if cell is alive
            pygame.draw.rect(SCREEN, BLACK, rect, 0)                # draw a black rectangle
            pygame.draw.rect(SCREEN, GREY, rect, 1)                 # draw a grey border
            
    def __repr__(self):
        """String representation of cell object"""
        return '(' + str(self.x // CELL_SIZE) + ', ' + str(self.y // CELL_SIZE) + ')'

from const import CELL_SIZE
import pygame
from pygame.constants import WINDOWHITTEST
from cell import Cell

class Grid:
    def __init__(self, width, height):
        """Initialize grid"""
        self.width = width
        self.height = height
        self.grid = self.initialize_grid()
        self.alive = []
        
    def initialize_grid(self):
        """Initialize grid 2d list"""
        grid = []
        for y in range(0, self.height, CELL_SIZE):
            grid.append([])
            for x in range(0, self.width, CELL_SIZE):
                grid[y // CELL_SIZE].append(Cell(x, y))

        # set neighbours of each cell
        for row in grid:
            for cell in row:
                cell.set_neighbours(grid)
        
        return grid
    
    def set_alive(self, idx_x, idx_y):
        """Set a cell to alive"""
        cell = self.grid[idx_y][idx_x]  # get cell
        if cell not in self.alive:      # if cell not already on list of alive
            cell.is_alive = True        # set cell to alive
            cell.draw()                 # draw cell
            self.alive.append(cell)     # add cell to list
        
    def set_dead(self, idx_x, idx_y):
        """Set a cell to dead"""
        cell = self.grid[idx_y][idx_x]  # get cell
        if cell in self.alive:          # if cell is in list of alive
            cell.is_alive = False       # set cell to dead
            cell.draw()                 # draw cell
            self.alive.remove(cell)     # remove cell from list

    def draw(self):
        """Draw grid"""
        for y in range(0, self.height, CELL_SIZE):
            for x in range(0, self.width, CELL_SIZE):
                self.grid[y // CELL_SIZE][x // CELL_SIZE].draw()

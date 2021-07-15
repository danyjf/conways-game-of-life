from const import CELL_SIZE
import pygame
from pygame.constants import WINDOWHITTEST
from cell import Cell

class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = self.initialize_grid()
        
    def initialize_grid(self):
        grid = [[]]
        for y in range(0, self.height, CELL_SIZE):
            for x in range(0, self.width, CELL_SIZE):
                grid[y // CELL_SIZE].append(Cell(x, y))
            grid.append([])
        
        return grid
    
    def set_alive(self, idx_x, idx_y):
        cell = self.grid[idx_y][idx_x]
        cell.is_alive = True
        cell.draw()

    def draw(self):
        for y in range(0, self.height, CELL_SIZE):
            for x in range(0, self.width, CELL_SIZE):
                self.grid[y // CELL_SIZE][x // CELL_SIZE].draw()

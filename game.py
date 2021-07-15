from os import kill
from pygame.constants import MOUSEBUTTONDOWN
from grid import Grid
from const import *
import pygame

class Game:    
    def __init__(self):
        """Game initialization"""
        pygame.init()
        self.grid = Grid(SCREEN_SIZE[0], SCREEN_SIZE[1])
        self.clock = pygame.time.Clock()
        
    def mouse_click_event(self):
        """Called when mouse is clicked and game is not running"""
        pos = pygame.mouse.get_pos()    # get position of the mouse click
        
        # calculate indexes from the mouse position
        idx_x = pos[0] // CELL_SIZE
        idx_y = pos[1] // CELL_SIZE
        
        # if clicked cell is alive kill it otherwise make it alive
        if self.grid.grid[idx_y][idx_x].is_alive:
            self.grid.set_dead(idx_x, idx_y)
        else:
            self.grid.set_alive(idx_x, idx_y)
        
    def live_neighbours(self, cell):
        """Get number of alive neighbours"""
        n = 0
        for neighbour in cell.neighbours:
            if neighbour.is_alive:
                n += 1
                
        return n
        
    def algorithm(self):
        """Conways game of life algorithm"""
        alive = []              # initialize list of cells that will be alive
        dead = []               # initialize list of cells that will be dead
        for cell in self.grid.alive:
            # get indexes of the cell position
            idx_x = cell.x // CELL_SIZE
            idx_y = cell.y // CELL_SIZE
            
            n_live = self.live_neighbours(cell)     # get number of neighbours alive
            if n_live < 2 or n_live > 3:            # if has less than 2 or more than 3 neighbours alive
                dead.append((idx_x, idx_y))         # add the cell to the kill list
            
            # for each of the dead neighbours of the alive cell
            for nb in cell.neighbours:
                if not nb.is_alive:
                    n_live = self.live_neighbours(nb)   # get number of neighbours of the neighbour alive
                    # if neighbour has 3 neighbours alive and isn't yet on the list of cells that will live
                    if n_live == 3 and (nb.x // CELL_SIZE, nb.y // CELL_SIZE) not in alive:
                        alive.append((nb.x // CELL_SIZE, nb.y // CELL_SIZE))    # add cell to list of cells to live

        # set cells to alive and dead
        for t in alive:
            self.grid.set_alive(t[0], t[1])
        for t in dead:
            self.grid.set_dead(t[0], t[1])
        
    def game_loop(self):
        """Game loop until exits the game"""
        running = True      # true while the app is running
        interactive = True  # true when allowed to interact with the grid
        while running:
            self.grid.draw()    # draw all the grid
            
            # check for events
            for event in pygame.event.get():
                # quit event
                if event.type == pygame.QUIT:
                    running = False
                    
                # only check for this events if is in interactive mode
                if interactive:
                    if event.type == pygame.MOUSEBUTTONDOWN:                            # mouse click event
                        self.mouse_click_event()
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  # space click event
                        interactive = False # remove interactive mode
                elif not interactive:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:    # space click event
                        interactive = True  # set interactive mode

            # when not in interactive mode
            if not interactive:
                self.algorithm()        # run game algorithm
                self.clock.tick(2.5)    # run on 2.5 frames per second

            pygame.display.update()
            
        pygame.quit()

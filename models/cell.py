import numpy
from models.grid2D import Grid2D
class Cell():
    def __init__(self, pos, color, grid):
        self.pos = pos
        self.color = color
        self.agents = [] 
        self.grid = grid
        self.neighbours = []
    def add_agent(self, agent):
        self.agents.append(agent)

    def remove_agent(self, agent):
        self.agents.remove(agent)

    def is_empty(self):
        return len(self.agents) == 0

    @property
    def neighbours(self):
        return self.grid.get_neighbours(self.pos)

    @neighbours.setter
    def neighbours(self, value):
        self.neighbours = value



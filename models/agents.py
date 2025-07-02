import random

class Agent():
    """The base agent class"""
    def __init__(self, cell, grid):
        """Initialize an agent.
        Args:
            energy: Starting amount of energy
            p_reproduce: Probability of reproduction
            cell: Cell in which the animal starts 
        """
        self.cell = cell
        self.grid = grid
        self.alive = True


    @property 
    def cell(self):
        """Returns the cell that the agent is currently standing on, based on its
        coordinates.
        """
        return self._cell
    
    @cell.setter
    def cell(self, value):
        self._cell = value



    def destroy(self):
        
        pass

    def jump_to(self, pos):
        """ Move the agent to a specified point.
        Args:
            x - Destination x-coordinate
            y - Destination y-coordinate """
        pass

    
    def feed(self):
        pass

    def spawn_offspring(self):
        """Create offspring by splitting energy and creating new instance."""
        #if random.random() < self.p_reproduce:
        #    self.energy /=2
        #    return self.__class__(self.energy, self.p_reproduce)
        #else: 
        #    return None

    def move(self):
        """Find a random neighboring cell and move there"""
        #neighbours = self.grid.get_neighbours(self.pos)
        #if neighbours:
        #    self.grid.move_agent

    def remove(self):
        """The agent is removed (dead) from the model"""
            

    def step(self):
        """Execute one step of the animal's behavior."""


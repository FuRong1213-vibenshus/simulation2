import random
import numpy as np
class Agent():
    """The base agent class"""
    def __init__(self, x,y):
        """Initialize an agent.
        Args:
            energy: Starting amount of energy
            p_reproduce: Probability of reproduction
            cell: Cell in which the animal starts 
        """
        self.position = np.array([x,y])
        self.alive = True


    @property 
    def position(self):
        """Returns the cell that the agent is currently standing on, based on its
        coordinates.
        """
        return self._position 
    
    @position.setter
    def position(self, x,y):
        self._position = np.array([x,y])


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

        pass

    def step(self):
        """Execute one step of the animal's behavior."""
        pass


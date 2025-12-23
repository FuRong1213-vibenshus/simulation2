import random
import numpy as np
class Agent():
    """The base agent class"""
    def __init__(self, x,y,speed,world_size):
        """Initialize an agent.
        Args:
            energy: Starting amount of energy
            p_reproduce: Probability of reproduction
            cell: Cell in which the animal starts 
        """
        self._x = x
        self._y = y
        self.speed = speed
        self.world_size = world_size
        self.alive = True
        self._pos = np.array([self._x, self._y])
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        # wrap around (toroidal world)
        self._x = value % self.world_size

    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, value):
        # wrap around (toroidal world)
        self._y = value % self.world_size

    @property 
    def pos(self):
        """Returns the cell that the agent is currently standing on, based on its
        coordinates.
        """
        return self._pos 
    

    def move(self):
        
        angle = random.random()*2*np.pi
        delta_x = np.cos(angle)*self.speed
        delta_y = np.sin(angle)*self.speed
        self.x = self.x + delta_x
        self.y = self.y + delta_y


    
    def feed(self):
        pass

    def spawn_offspring(self):
        """Create offspring by splitting energy and creating new instance."""
        self.energy /=2

        return self.__class__(self.x+random.uniform(-5,5),
                            self.y+random.uniform(-5, 5),
                            self.speed,
                            self.world_size
                            )
                        


    def step(self):
        """Execute one step of the animal's behavior."""
        pass


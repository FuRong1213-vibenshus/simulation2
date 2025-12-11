import numpy as np
import copy
import random
import math
import models 


class WolfSheep(models.model):
    """Wolf-sheep Predation Model.
    A model for simulating wolf and sheep (predator-prey) ecosystem modelling.
    """

    def __init__(
        self,
        world_size,
        n_sheep=3,
        n_wolves=2,
        sheep_reproduce=0.4,
        wolf_reproduce=0.05,
        wolf_gain_from_food=20,
    ):
        """Create a wolf-Sheep model with the given parameters.

        Args:
            n_sheep: Number of sheep to start with
            n_wolves: Number of wolves to start with
            sheep_reproduce: Probability of each sheep reproducing each step
            wolf_reproduce: probability of each wolf reproducing each step
            wolf_gain_from_food: Energy a wolf gains from eating a sheep
        """
        super.__init__(world_size)
        self.time = 0
        self.sheep = []
        self.wolves = []
        self.new_sheep = []
        self.new_wolves = []
        self.sheep_to_remove = []
        self.wolves_to_remove = []


        # Populate world
                
        for _ in range(n_sheep):
            x, y = np.random.uniform(0, world_size, 2)
            self.sheep.append(models.Sheep(x,y))
        
        for _ in range(n_wolves):
            x, y = np.random.uniform(0, world_size, 2)
            self.wolves.append(models.Wolf(x,y))


        self.sheep_reproduce = sheep_reproduce
        self.wolf_reproduce = wolf_reproduce
        self.wolf_gain_from_food = wolf_gain_from_food


    def setup(self):
        # Add newborns, remove the dead
        pass

    def step(self):
        """
        Add newborns, remove the dead,

        """
        self.sheep = [s for s in self.sheep if s.alive]
        self.wolves = [w for w in self.wolves if w.alive] 
        
        self.sheep.extend(self.new_sheep)
        self.wolves.extend(self.new_wolves)

        self.new_sheep = []
        self.new_wolves = []
        
        for s in self.sheep:
            s.step()

        for w in self.wolves:
            w.step()
        
        self.time += 1
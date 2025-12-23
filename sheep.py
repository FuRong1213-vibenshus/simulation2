import random
import numpy as np
from models.agents import Agent

class Sheep(Agent):
    def __init__(self, 
                 x,y,
                 world_size, 
                 speed = 25,
                 p_reproduce = 0.2, 
                 energy_loss = 1.2,
                 energy = 10,
                 ):
        super().__init__(x,y,speed,world_size)
        self.p_reproduce = p_reproduce
        self.energy = energy
        self.energy_loss = energy_loss
        self.alive = True

    def step(self,model):

        self.energy -= self.energy_loss

        if self.energy <0:
            self.alive = False
        # Random walk
        self.move()

        # Reproduction
        if random.random()<self.p_reproduce:
            model.new_sheep.append(self.spawn_offspring())
        
    

    

         








import random
import numpy as np
from models.agents import Agent

class Wolf(Agent):

    def __init__(self, 
                 x,y,
                 world_size,
                 speed=40,
                 p_reproduce = 0.05, 
                 energy = 25,
                 energy_loss = 5,
                 energy_gain_from_food = 10,
                 ):
        super().__init__(x,y,speed,world_size)
        self.p_reproduce = p_reproduce
        self.energy = energy
        self.energy_loss = energy_loss
        self.energy_gain_from_food = energy_gain_from_food
        self.alive = True

    def step(self,model):
        self.energy -= self.energy_loss
        
        if not self.feed(model):
            self.move() 
        
        # Handle death and reproduction

        if self.energy < 0:
            self.alive = False
        elif random.random()< self.p_reproduce:
            model.new_wolves.append(self.spawn_offspring())
    
    
    def feed(self,model):
        """If possible, eat a sheep at nearby."""
        #print(self.pos)
        sheep_pos_list = np.array([s.pos for s in model.sheep])
        distance_list = np.linalg.norm(sheep_pos_list - self.pos, axis=1)
        target_idx = np.argmin(distance_list)
        d = distance_list[target_idx]

        if d < 110 and model.sheep[target_idx].alive:
            model.sheep[target_idx].alive = False
            self.energy += self.energy_gain_from_food
            self.x = model.sheep[target_idx].x
            self.y = model.sheep[target_idx].y
    
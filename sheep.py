import random
import numpy as np
from models.agents import Agent



class Sheep(Agent):
    def __init__(self, 
                 model,
                 x,y, 
                 p_reproduce, 
                 energy, 
                 speed):
        super.__init__(x,y)
        self.p_reproduce = p_reproduce
        self.energy = energy
        self.speed = speed
        self.alive = True

    def step(self):
        # Random walk
        self.move()
        self.spawn_offspring()
        
    
    def move(self):
        
        angle = random.random()*2*np.pi
        delta_x = np.cos(angle)*self.speed
        delta_y = np.sin(angle)*self.speed
        self.x = self.x + delta_x
        self.y = self.y + delta_y
        self.energy -= 1
    
    def spawn_offspring(self):

        # Handle reproduction
        if random.random()< self.p_reproduce:
            self.model.new_sheep.append(Sheep(self.x+random.uniform(-0.5,0.5),
                                              self.y+random.uniform(-0.5, 0.5)
                                              )
                                        )



class Wolf(Agent):

    def __init__(self, 
                 x,y,
                 p_reproduce, 
                 energy,
                 speed,
                 model):
        super.__init__(x,y)
        self.p_reproduce = p_reproduce
        self.energy = energy
        self.speed = speed
        self.alive = True
        self.model = model

    def step(self):
        self.energy -= 1
        self.feed()
        self.move() 
        # Handle death and reproduction
        self.spawn_offspring()
        if self.energy < 0:
            self.alive = False
        elif random.random()< self.p_reproduce:
            self.spawn_offspring()
    
    
    def feed(self):
        """If possible, eat a sheep at nearby."""


        condition = self.model.sheep






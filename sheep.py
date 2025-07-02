import random
from models.agents import Agent, Cell


class Sheep(Agent):
    def __init__(self, cell, p_reproduce, energy):
        super.__init__(cell):
        self.p_reproduce = p_reproduce
        self.energy = energy

    def step(self):
        self.move()
        # Handle death and reproduction
        if self.energy < 0:
            self.remove()
        elif random.random()< self.p_reproduce:
            self.spawn_offspring()
    
    def move(self):
        cell_without_wolves = list(cell for cell in self.cell.neighbours 
                                        if not any(isinstance(obj, Wolf)) 
                                        for obj in cell.agents)
        
        if cell_without_wolves:
            self.cell = random.choice(cell_without_wolves)
            self.energy -= 1
        
            
class Wolf(Agent):

    def __init__(self, p_reproduce, energy):
        super.__init__(cell):

    def feed(self):
        """If possible, eat a sheep at current location."""
        sheep_list = list(agent for agent in self.cell.agents
                         if isinstance(agent, Sheep))

        if sheep_list:
            eaten = random.choice(sheep_list)
            eaten.del
    def step(self):
        self.move()
        # Try to feed 
        self.feed()
        # Handle death and reproduction
        if self.energy < 0:
            self.remove()
        elif random.random()< self.p_reproduce:
            self.spawn_offspring()

    def move(self):
        cell_with_sheep = list(cell for cell in self.cell.neighbours
                                    if any(isinstance(obj, Sheep))
                                    for obj in cell.agents)





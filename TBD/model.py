import random

class Model:
    def __init__(self, width, height, seed=None):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive!")
        self.width = width
        self.height = height
        self.rng = random.Random(seed)
        self.agents = []
        self.time = 0
        self._next_uid = 0
    
    def random_position(self):
        return (self.rng.randrange(self.width), self.rng.randrange(self.height))
    
    def add_agent(self, agent):
        self.agents.append(agent)

    def remove_agent(self, agent):
        self.agent.remove(agent)

    def agents_at(self, pos):
        """
        TODO:
        return a list of agents who is occuppying the given position.
        """

    def next_uid(self):
        uid = self._next_uid
        self._next_uid +=1
        return uid 

    def step(self):
        """
        Random sequence for fairness
        
        """ 

        self.rng.shuffle(self.agent)
        """
        TODO:
        - all agents Move
        - all interact (eat)
        - all reproduce (if possible)
        - model cleanup the DEAD, remove dead agent from the agent list
        """
        
         
        
        
        self.time += 1
        
    def run(self, steps:int):
        for _ in range(steps):
            self.step()

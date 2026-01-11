from agent import Agent
class Prey(Agent):
    def __init__(self, 
                 model, 
                 uid, 
                 position = None, 
                 energy: int = 10):
        super().__init__(model, uid, position)
        self.energy = energy

    def move(self):
        # TODO :
        # 1) Move (random 4-neighborhood)
        # 2) energy -= 1
        # 3) die if energy <=0
        raise NotImplementedError
    
    def interact(self):
        pass

    def reproduce(self):


        # TODO :
        # If energy >= REPRODUCE_THRESHOLD:
        #       - (optional) at a certain possibility        
        #       - create a new Prey (baby) at same position (or neighbor)
        #       - call model.add_agent(baby) 
        #       - reduce parent's energy (e.g. energy //= 2)
        raise NotImplementedError
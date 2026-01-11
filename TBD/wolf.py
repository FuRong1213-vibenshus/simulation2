from agent import Agent

class Wolf(Agent):

    def __init__(self,
                 model,
                 uid,
                 position=None,
                 energy: int = 15):
        super().__init__(model, uid, position)
        self.energy = energy
        
    def move(self) -> None:
        # TODO :
        # - move randomly
        # - energy -= 1
        # - if energy <= 0: die()
        raise NotImplementedError

    def interact(self) -> None:
        # TODO :
        # - find prey on same cell and eat ONE:
        #     prey_here = self.model.agents_at(self.position) 
        # - mark eaten prey dead (prey.die())
        # - gain energy
        raise NotImplementedError 

    def reproduce(self) -> None:
        # TODO (Lesson 2) optional:
        # - if energy >= threshold (and at a certain possibility):
        #     spawn new Predator, reduce energy
        raise NotImplementedError
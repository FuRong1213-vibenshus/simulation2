from agent import Agent
from prey import Prey

class Predator(Agent):

    def __init__(self,
                 model,
                 uid,
                 start_energy,
                 energy_loss_per_move,
                 reproduce_prob_per_step, 
                 energy_gain_on_eat,
                 position=None,
                 ):
        super().__init__(
                        model, 
                        uid, 
                        start_energy,
                        energy_loss_per_move,
                        reproduce_prob_per_step, 
                        energy_gain_on_eat,
                        position=position)
        
    def move(self) -> None:
        # TODO :
        # - move randomly
        # - energy -= 1
        # - if energy <= 0: die()

        self.energy -= self.energy_loss_per_move 

        if self.energy <= 0:
            self.die()
        else:    
            self.random_walk()

    def interact(self) -> None:
        # TODO :
        # - find prey on same cell and eat ONE:
        #     prey_here = self.model.agents_at(self.position) 
        # - mark eaten prey dead (prey.die())
        # - gain energy
        agents_here = self.model.agents_at(self.position)
        prey_here = [a for a in agents_here if isinstance(a, Prey)]
        if len(prey_here) and self.model.rng.random()<0.9:
            prey_here[0].alive = False
            self.energy += self.energy_gain_on_eat 
            self.reproduce()
        

    def reproduce(self) -> None:
        # TODO (Lesson 2) optional:
        # - if energy >= threshold (and at a certain possibility):
        #     spawn new Predator, reduce energy
        p = self.model.rng.random()
        if  p < self.reproduce_prob_per_step:
            baby = self.__class__(
                        self.model,
                        uid=self.model.next_uid(),
                        start_energy= self.start_energy,
                        energy_loss_per_move=self.energy_loss_per_move,
                        reproduce_prob_per_step=self.reproduce_prob_per_step, 
                        energy_gain_on_eat=self.energy_gain_on_eat,
                        position=self.position,
                        )
            self.model.add_agent(baby)



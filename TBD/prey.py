from agent import Agent

class Prey(Agent):
    def __init__(self, 
                 model, 
                 uid, 
                 start_energy,
                 energy_loss_per_move,
                 reproduce_prob_per_step, 
                 energy_gain_on_eat,
                 position = None, 
                 ):
        super().__init__(
                        model, 
                        uid, 
                        start_energy,
                        energy_loss_per_move,
                        reproduce_prob_per_step, 
                        energy_gain_on_eat,
                        position = position)
                

    def move(self):
        # TODO :
        # 1) Move (random 4-neighborhood)
        # 2) energy -= 1
        # 3) die if energy <=0
        # raise NotImplementedError

        self.energy -= self.energy_loss_per_move 
        if self.energy <= 0:
            self.die() 
        else:    
            self.random_walk()
        
    def interact(self):
        if self.model.rng.random()<0.06:
            self.energy += self.energy_gain_on_eat

        self.reproduce()

    def reproduce(self):


        # TODO :
        # If energy >= REPRODUCE_THRESHOLD:
        #       - (optional) at a certain possibility        
        #       - create a new Prey (baby) at same position (or neighbor)
        #       - call model.add_agent(baby) 
        #       - reduce parent's energy (e.g. energy //= 2)
        # raise NotImplementedError
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
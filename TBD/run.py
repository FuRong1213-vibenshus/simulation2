
import numpy as np
import matplotlib.pyplot as plt

from model import Model
from prey import Prey
from predator import Predator
from toroidalposition import ToroidalPosition
from params import Params
def make_toroidal_classes(model):
    class ToroidalPrey(Prey):
        position = ToroidalPosition.from_model(model)

    class ToroidalPredator(Predator):
        position = ToroidalPosition.from_model(model)


    return ToroidalPrey, ToroidalPredator

def test_toroidal_wrap():

    model = Model(width=10, height=10, seed=2)
    ToroidalPrey, ToroidalPredator = make_toroidal_classes(model)
    p = ToroidalPrey(model, uid = 0, position=(9,5))

    p.move_by(1,0)
    assert p.position == (0,5)

def test_agent_dies():
    world = Model(5,5,seed=1)
    ToroidalPrey, _ = make_toroidal_classes(world)
    p = ToroidalPrey(world, uid = 0, energy=1)
    world.step()
    assert len(world.agents) == 0

def test_agent_interaction():
    world = Model(5,5,seed=1)
    ToroidalPrey, ToroidalPredator = make_toroidal_classes(world)
    sheep= ToroidalPrey(world, uid = 0, position=(2,2))
    wolf = ToroidalPredator(world, uid= 1, energy=10, position=(2,2))
    world.add_agent(sheep)
    world.add_agent(wolf)
    wolf.interact()
    assert wolf.energy == 20

if __name__ == "__main__":


    pparams = Params(width = 40,
                    height = 30,
                    initial_prey = 150,
                    initial_predator = 30,
                    prey_start_energy = 8,
                    predator_start_energy = 12,
                    prey_energy_loss_per_move = 1,  # hver move mister 1
                    predator_energy_loss_per_move = 1,
                    prey_energy_gain_on_eat = 2,
                    predator_energy_gain_on_eat = 10, # (predator får +12 når den spiser en prey)
                    prey_reproduce_prob = 0.08,
                    predator_reproduce_prob = 0.2,
                    seed = 2,
                    steps = 600,
                    )

    model = Model(width=pparams.width, height=pparams.height, seed=pparams.seed)
    ToroidalPrey, ToroidalPredator = make_toroidal_classes(model)
    for _ in range(pparams.initial_prey):
        model.add_agent(ToroidalPrey(model, 
                                     uid=model.next_uid,
                                     start_energy=pparams.prey_start_energy,
                                     energy_gain_on_eat=pparams.predator_energy_gain_on_eat,
                                     energy_loss_per_move=pparams.prey_energy_loss_per_move,
                                     reproduce_prob_per_step=pparams.prey_reproduce_prob))
    for _ in range(pparams.initial_predator):
        model.add_agent(ToroidalPredator(
                                    model, 
                                    uid=model.next_uid,
                                    start_energy=pparams.predator_start_energy,
                                    energy_loss_per_move = pparams.predator_energy_loss_per_move,
                                    reproduce_prob_per_step=pparams.predator_reproduce_prob, 
                                    energy_gain_on_eat=pparams.predator_energy_gain_on_eat,
                                    ))
    prey_count = []
    pred_count = []
    """for _ in range(num_step):
        prey_count = sum(isinstance(a, ToroidalPrey) for a in model.agents)
        pred_count = sum(isinstance(a, ToroidalPredator) for a in model.agents)
        print(f"t={model.time}, sheep = {prey_count}, wolf = {pred_count}")
        
        model.step()
    """
    for _ in range(pparams.steps):
        prey_per_step =sum(isinstance(a, ToroidalPrey) for a in model.agents) 
        prey_count.append(prey_per_step)
        pred_per_step =sum(isinstance(a, ToroidalPredator) for a in model.agents) 
        pred_count.append(pred_per_step)

        if  prey_per_step > 3000 or \
            pred_per_step > 3000 or \
            prey_per_step == 0 or \
            pred_per_step == 0: 
            break
        model.step()
    
    plt.plot(range(len(pred_count)), prey_count, label="sheep")
    plt.plot(range(len(pred_count)), pred_count, label="wolf")
    plt.legend(title='Parameter where:')
    plt.show()
from dataclasses import dataclass

@dataclass
class Params:
    width: int 
    height: int
    initial_prey: int
    initial_predator: int
    prey_start_energy: int
    predator_start_energy: int
    prey_energy_gain_on_eat: int
    prey_energy_loss_per_move: int  # hver move mister 1
    predator_energy_loss_per_move: int
    prey_reproduce_prob: float 
    predator_reproduce_prob: float
    predator_energy_gain_on_eat: int # (predator får +12 når den spiser en prey)
    seed: int
    steps: int


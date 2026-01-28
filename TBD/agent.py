
from abc import ABC, abstractmethod
import random

class Agent(ABC):

    """
    Abstract agent base class.
    subclasses MUST implement move(), interact(), reproduce().
    """
    def __init__(self, 
                 model, 
                 uid,
                 start_energy,
                 energy_loss_per_move,
                 reproduce_prob_per_step, 
                 energy_gain_on_eat,
                 position = None):
        self.model = model
        self.uid = uid
        self.energy = start_energy
        self.start_energy = start_energy
        self.energy_loss_per_move = energy_loss_per_move
        self.reproduce_prob_per_step = reproduce_prob_per_step
        self.energy_gain_on_eat = energy_gain_on_eat
        self.position = position if position is not None else model.random_position()
        self.alive = True        

    @property
    def x(self):
        return self.position[0]

    @property
    def y(self):
        return self.position[1]
    
    def die(self):
        self.alive = False

    def random_walk(self):
        """Von Neumann neighborhood random move using model RNG"""
        dx, dy = random.choice([(1,0), (-1,0), (0,1), (0,-1)])
        x, y = self.position
        self.position = (x+dx, y+dy)

    def move_by(self, dx, dy):
        x, y = self.position
        self.position = (x+dx, y+dy)

    @abstractmethod
    def move(self):
        raise NotImplementedError
    @abstractmethod
    def interact(self):
        raise NotImplementedError
    @abstractmethod
    def reproduce(self):
        raise NotImplementedError
    def __repr__(self):
        return f"this is id {self.uid} at {self.position}"
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt, animation
from matplotlib import colors 
from models.agents import Sheep, Wolf
from models import agents, cell, model
from wolf_sheep_model import WolfSheep

class App():
    def __init__(self, model):
        self.model = model

    def __map(self, obj):
        if isinstance(obj, Sheep): 
            val = 1
        elif isinstance(obj,Wolf):
            val = 2
        else:
            val = 0
        return val

    def display_grid(self):
        fig, ax = plt.subplots()
        self.fig = fig
        cmap = colors.ListedColormap(['green', 'yellow', 'red'])
        x = np.array(range(0, self.model.width+1))
        y = np.array(range(0, self.model.height+1))
        X, Y = np.meshgrid(x,y)
        
        map_class_to_color = np.vectorize(self.__map)
        self.normed_grid = map_class_to_color(self.model.grid)
        self.pcmesh = ax.pcolormesh(x, y, 
                                    self.normed_grid ,
                                    cmap=cmap, 
                                    edgecolors='k',
                                    linewidths=0.5)
    def cell_map(self):
        map_class_to_color = np.vectorize(self.__map)
        self.normed_grid = map_class_to_color(self.model.grid)
        self.pcmesh.set_array(self.normed_grid.flatten())
    def __animate(self, i):
        self.model.step()
        self.cell_map()

    def run(self):

        self.display_grid()
        anim = animation.FuncAnimation(self.fig, 
                                       self.__animate,
                                       interval=5, 
                                       frames=10)
        anim.save('tmp.gif')
        plt.show()

model = WolfSheep(10, 10, 50, 20)
model.setup()
app = App(model)
app.run()




from model import Model
from sheep import Sheep
from wolf import Wolf
from toroidalposition import ToroidalPosition

def make_toroidal_classes(model):
    class ToroidalSheep(Sheep):
        position = ToroidalPosition.from_model(model)

    class ToroidalWolf(Wolf):
        position = ToroidalPosition.from_model(model)


    return ToroidalSheep, ToroidalWolf

if __name__ == "__main__":
    model = Model(width=10, height=6, seed=2)
    ToroidalSheep, ToroidalWolf = make_toroidal_classes(model)

    for _ in range(12):
        model.add_agent(ToroidalSheep(model, uid=model.next_uid))
    for _ in range(4):
        model.add_agent(ToroidalWolf(model, uid=model.next_uid))

    for _ in range(10):
        prey_count = sum(isinstance(a, ToroidalSheep) for a in model.agents)
        pred_count = sum(isinstance(a, ToroidalWolf) for a in model.agents)
        print(f"t={model.time}, sheep = {prey_count}, wolf = {pred_count}")
        model.step()
from Utility.naming import produceName
from random import choices

diets = ["Planetary Atomic Material", "Photosynthesis", "Herbivore", "Carnivore", "Omnivore"]

class Flora:
    def __init__(self):

        self.name = produceName()

        selection = choices(diets, weights=[25, 75, 0, 0, 0])
        self.diet = selection[0]

class Fauna:
    def __init__(self, planet):

        self.name = produceName()

        if len(planet.flora) > 0 and len(planet.fauna) <= 1:
            selection = choices(diets, weights=[10, 30, 60, 0, 0])
        elif len(planet.flora) > 0 and len(planet.fauna) > 1:
            selection = choices(diets, weights=[5, 5, 30, 30, 30])
        else:
            selection = choices(diets, weights=[25, 75, 0, 0, 0])

        self.diet = selection[0]
from random import uniform
from Objects.galaxy import width, height, depth

def create_player(name):
    return Player(name)

class Player:
    location = []
    name = ""

    def __init__(self, name):
        self.name = name
        self.location = [uniform(-(width / 2), (width / 2)),
                         uniform(-(height / 2), (height / 2)),
                         uniform(-(depth / 2), (depth / 2))]

    def move(self, newPosition):
        self.location = [newPosition[0], newPosition[1], newPosition[2]]
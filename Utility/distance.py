from math import sqrt, pow


def get_distance(obj1, obj2):

    distance = (sqrt(pow((obj1.location[0] - obj2.location[0]), 2) +
                     pow((obj1.location[1] - obj2.location[1]), 2) +
                     pow((obj1.location[2] - obj2.location[2]), 2)))
    return distance

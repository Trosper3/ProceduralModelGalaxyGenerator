from random import randint, choices, uniform
from math import sqrt
from Utility.constants import sunRadii, solarMass, gravityConstant, gasConstant
from Utility.distance import get_distance
from Utility.atomic import createAtmosphere
from Objects.galaxy import width, height, depth
from Objects.planetary_objects import Flora, Fauna
import Objects.galaxy

starTypes = ['O','B','A','F','G','K','M']

class Star:

    def __init__(self):

        self.planets = []
        self.location = [uniform(-(width / 2), (width / 2)),
                         uniform(-(height / 2), (height / 2)),
                         uniform(-(depth / 2), (depth / 2))]

        starTypeSelection = choices(starTypes, weights=[3, 3000, 40000, 200000, 300000, 1100000, 7800000])
        self.type = starTypeSelection[0]

        match self.type:

            case 'O':
                Objects.galaxy.oStarCount += 1
                self.mass = uniform(15.0 * solarMass, 90.0 * solarMass)
                self.radius = uniform(8 * sunRadii, 15 * sunRadii)
                self.name = str(self.type) + str(Objects.galaxy.oStarCount)
                planetCountChoice = choices([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], weights=[100, 0, 0, 0, 0, 0, 0, 0, 0, 0])
                planet_count = planetCountChoice[0]

            case 'B':
                Objects.galaxy.bStarCount += 1
                self.mass = uniform(2.0 * solarMass, 16.0 * solarMass)
                self.radius = uniform(3 * sunRadii, 8 * sunRadii)
                self.name = str(self.type) + str(Objects.galaxy.bStarCount)
                planetCountChoice = choices([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], weights=[90, 10, 0, 0, 0, 0, 0, 0, 0, 0])
                planet_count = planetCountChoice[0]

            case 'A':
                Objects.galaxy.aStarCount += 1
                self.mass = uniform(1.4 * solarMass, 2.1 * solarMass)
                self.radius = uniform(1.5 * sunRadii, 2.5 * sunRadii)
                self.name = str(self.type) + str(Objects.galaxy.aStarCount)
                temp = choices([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], weights=[80, 15, 5, 0, 0, 0, 0, 0, 0, 0])
                planet_count = temp[0]

            case 'F':
                Objects.galaxy.fStarCount += 1
                self.mass = uniform(1.0 * solarMass, 1.5 * solarMass)
                self.radius = uniform(1.2 * sunRadii, 1.5 * sunRadii)
                self.name = str(self.type) + str(Objects.galaxy.fStarCount)
                temp = choices([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], weights=[50, 15, 10, 5, 5, 5, 4, 3, 2, 1])
                planet_count = temp[0]

            case 'G':
                Objects.galaxy.gStarCount += 1
                self.mass = uniform(0.84 * solarMass, 1.15 * solarMass)
                self.radius = uniform(0.9 * sunRadii, 1.1 * sunRadii)
                self.name = str(self.type) + str(Objects.galaxy.gStarCount)
                temp = choices([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], weights=[15, 15, 15, 15, 15, 10, 8, 4, 2, 1])
                planet_count = temp[0]

            case 'K':
                Objects.galaxy.kStarCount += 1
                self.mass = uniform(0.6 * solarMass, 0.9 * solarMass)
                self.radius = uniform(0.7 * sunRadii, 0.9 * sunRadii)
                self.name = str(self.type) + str(Objects.galaxy.kStarCount)
                temp = choices([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], weights=[15, 15, 15, 15, 15, 10, 8, 4, 2, 1])
                planet_count = temp[0]

            case 'M':
                Objects.galaxy.mStarCount += 1
                self.mass = uniform(0.08 * solarMass, 0.6 * solarMass)
                self.radius = uniform(0.15 * sunRadii, 0.6 * sunRadii)
                self.name = str(self.type) + str(Objects.galaxy.mStarCount)
                temp = choices([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], weights=[20, 20, 10, 10, 15, 10, 8, 4, 2, 1])
                planet_count = temp[0]

            case _:
                print("You're bad dude!")
                planet_count = None

        generateStarDetails(self)

        for i in range(planet_count):
            self.planets.append(Planet(self))


class Planet:

    def __init__(self, home_star):
        self.home_star = home_star

        generatePlanetDetails(self)

        """                     
        self.name = str(self.home_star.name) + "-" + str(len(self.home_star.planets) + 1)

# ******************** Location / Zone ******************** #

        rangeChanceX = uniform(0.1, 3)
        rangeChanceY = uniform(0.1, 3)
        rangeChanceZ = uniform(0.1, 3)
        offset = len(self.home_star.planets) + 1

        self.location = [
            self.home_star.location[0] + uniform(-(rangeChanceX * uniform(0.01, uniform(0, 3 * offset))),
                                                 rangeChanceX * uniform(0.01, uniform(0, 3 * offset))),  # X Pos
            self.home_star.location[1] + uniform(-(rangeChanceY * uniform(0.01, uniform(0, 3 * offset))),
                                                 rangeChanceY * uniform(0.01, uniform(0, 3 * offset))),  # Y Pos
            self.home_star.location[2] + uniform(-(rangeChanceZ * uniform(0.01, uniform(0, 3 * offset))),
                                                 rangeChanceZ * uniform(0.01, uniform(0, 3 * offset)))]  # Z Pos

        self.distance_from_star = get_distance(self.home_star, self)

        if (self.distance_from_star >= self.home_star.habitableZone[0]) and (self.distance_from_star <= self.home_star.habitableZone[1]):
            self.zone = "Green"
        elif (self.distance_from_star < self.home_star.habitableZone[0]):
            self.zone = "Red"
        elif (self.distance_from_star > self.home_star.habitableZone[1]):
            self.zone = "Blue"

# ******************** Mass / Radii / Gravity ******************** #

        chance = randint(1,1000)
        if chance == 1:
            self.mass = uniform(1.0 * pow(10, 22), self.home_star.mass)
            self.radius = uniform(1000000, self.home_star.radius)
        if 1 < chance <= 900:
            self.mass = uniform(1.0 * pow(10, 22), self.home_star.mass / 1000000)
            self.radius = uniform(1000000, self.home_star.radius / 100)
        if chance > 900:
            self.mass = uniform(1.0 * pow(10, 22), self.home_star.mass / 100)
            self.radius = uniform(1000000, self.home_star.radius / 1)

        self.gravity = (gravityConstant * self.mass) / (pow(self.radius, 2))

# ******************** Atmosphere / Temperature / Albedo ******************** #

        self.atmosphericMass = uniform(self.mass * 0.00000000000000000001, self.mass * 0.00001)
        self.atmosphereComponents = {}
        self.meanMolecularMass = 0
        
        atmosphereCompounds = createAtmosphere(self)
        
        self.meanMolecularMass = self.meanMolecularMass / len(atmosphereCompounds)

        remainingPercent = 100
        
        for i in range(len(atmosphereCompounds)):
            if i == len(atmosphereCompounds) - 1:
                self.atmosphereComponents[atmosphereCompounds[i]] = str(remainingPercent) + "%"
                #self.meanMolecularMass += atomicMasses[atmosphereCompounds[i]] * self.atmosphericMass
            else:
                percentValue = uniform(0.000001, remainingPercent)
                self.atmosphereComponents[atmosphereCompounds[i]] = str(percentValue) + "%"
                remainingPercent -= percentValue
                #self.meanMolecularMass += atomicMasses[atmosphereCompounds[i]] * self.atmosphericMass

        self.atmosphereRadius = uniform(1080, self.radius * 0.002)
        
        chance = randint(1,100)
        if chance == 1: self.albedo = uniform(0.01, 0.1)
        if 2 <= chance <= 90: self.albedo = uniform(0.1, 0.4)
        if 91 <= chance <= 100: self.albedo = uniform(0.4, 1)

        self.surf_temp = 325 * pow(1 - self.albedo, 0.25) * pow(get_distance(self, self.home_star), -0.5)
        self.meanMolecularMass = uniform(2.5, 45)
        self.atmosphericDensity = self.atmosphericMass / (4.1888 * (pow(self.radius + self.atmosphereRadius, 3) - pow(self.radius, 3)))
        self.atmosphericPressure = (self.atmosphericDensity * gasConstant * self.surf_temp) / self.meanMolecularMass

        if self.atmosphericPressure > 1000:
            self.type = "Gas Giant"
        else:
            self.type = "Terrestrial"

        #temp_rng = 0

        self.flora, self.fauna = [], []
        match self.type:
            case "Terrestrial":
                if self.zone == "Green":
                    count = randint(0,5)
                    for i in range(count):
                        self.flora.append(Flora())
                    count = randint(0, 5)
                    for i in range(count):
                        self.fauna.append(Fauna(self))
                else:
                    count = randint(0, 1)
                    for i in range(count):
                        self.flora.append(Flora())
                    count = randint(0, 1)
                    for i in range(count):
                        self.fauna.append(Fauna(self))

            case "Gas Giant":
                if self.zone == "Green":
                    count = randint(0,1)
                    for i in range(count):
                        self.fauna.append(Fauna(self))
                else:
                    pass
        """

def generateStarDetails(star: Star):
    star.core_temp = (((6.67408 * pow(10, -11)) * (1.7 * pow(10, -27)) * (star.mass)) / (
                star.radius * (3 / 2) * (1.3806485279 * pow(10, -23))))
    star.luminosity = (5.67 * pow(10, -8)) * star.core_temp
    star.habitableZone = [sqrt(star.luminosity / 1.1), sqrt(star.luminosity / 0.53)]
    star.gravity = (gravityConstant * star.mass) / (pow(star.radius, 2))

def generatePlanetDetails(planet: Planet):
    planet.name = str(planet.home_star.name) + "-" + str(len(planet.home_star.planets) + 1)

    # ******************** Location / Zone ******************** #

    rangeChanceX = uniform(0.1, 3)
    rangeChanceY = uniform(0.1, 3)
    rangeChanceZ = uniform(0.1, 3)
    offset = len(planet.home_star.planets) + 1

    planet.location = [
        planet.home_star.location[0] + uniform(-(rangeChanceX * uniform(0.01, uniform(0, 3 * offset))),
                                             rangeChanceX * uniform(0.01, uniform(0, 3 * offset))),  # X Pos
        planet.home_star.location[1] + uniform(-(rangeChanceY * uniform(0.01, uniform(0, 3 * offset))),
                                             rangeChanceY * uniform(0.01, uniform(0, 3 * offset))),  # Y Pos
        planet.home_star.location[2] + uniform(-(rangeChanceZ * uniform(0.01, uniform(0, 3 * offset))),
                                             rangeChanceZ * uniform(0.01, uniform(0, 3 * offset)))]  # Z Pos

    planet.distance_from_star = get_distance(planet.home_star, planet)

    if (planet.distance_from_star >= planet.home_star.habitableZone[0]) and (
            planet.distance_from_star <= planet.home_star.habitableZone[1]):
        planet.zone = "Green"
    elif (planet.distance_from_star < planet.home_star.habitableZone[0]):
        planet.zone = "Red"
    elif (planet.distance_from_star > planet.home_star.habitableZone[1]):
        planet.zone = "Blue"

    # ******************** Mass / Radii / Gravity ******************** #

    chance = randint(1, 1000)
    if chance == 1:
        planet.mass = uniform(1.0 * pow(10, 22), planet.home_star.mass)
        planet.radius = uniform(1000000, planet.home_star.radius)
    if 1 < chance <= 900:
        planet.mass = uniform(1.0 * pow(10, 22), planet.home_star.mass / 1000000)
        planet.radius = uniform(1000000, planet.home_star.radius / 100)
    if chance > 900:
        planet.mass = uniform(1.0 * pow(10, 22), planet.home_star.mass / 100)
        planet.radius = uniform(1000000, planet.home_star.radius / 1)

    planet.gravity = (gravityConstant * planet.mass) / (pow(planet.radius, 2))

    # ******************** Atmosphere / Temperature / Albedo ******************** #

    planet.atmosphericMass = uniform(planet.mass * 0.00000000000000000001, planet.mass * 0.00001)
    planet.atmosphereComponents = {}
    planet.meanMolecularMass = 0

    atmosphereCompounds = createAtmosphere(planet)

    planet.meanMolecularMass = planet.meanMolecularMass / len(atmosphereCompounds)

    remainingPercent = 100

    for i in range(len(atmosphereCompounds)):
        if i == len(atmosphereCompounds) - 1:
            planet.atmosphereComponents[atmosphereCompounds[i]] = str(remainingPercent) + "%"
            # self.meanMolecularMass += atomicMasses[atmosphereCompounds[i]] * self.atmosphericMass
        else:
            percentValue = uniform(0.000001, remainingPercent)
            planet.atmosphereComponents[atmosphereCompounds[i]] = str(percentValue) + "%"
            remainingPercent -= percentValue
            # self.meanMolecularMass += atomicMasses[atmosphereCompounds[i]] * self.atmosphericMass

    planet.atmosphereRadius = uniform(1080, planet.radius * 0.002)

    chance = randint(1, 100)
    if chance == 1: planet.albedo = uniform(0.01, 0.1)
    if 2 <= chance <= 90: planet.albedo = uniform(0.1, 0.4)
    if 91 <= chance <= 100: planet.albedo = uniform(0.4, 1)

    planet.surf_temp = 325 * pow(1 - planet.albedo, 0.25) * pow(get_distance(planet, planet.home_star), -0.5)
    planet.meanMolecularMass = uniform(2.5, 45)
    planet.atmosphericDensity = planet.atmosphericMass / (
                4.1888 * (pow(planet.radius + planet.atmosphereRadius, 3) - pow(planet.radius, 3)))
    planet.atmosphericPressure = (planet.atmosphericDensity * gasConstant * planet.surf_temp) / planet.meanMolecularMass

    if planet.atmosphericPressure > 1000:
        planet.type = "Gas Giant"
    else:
        planet.type = "Terrestrial"

    # temp_rng = 0

    planet.flora, planet.fauna = [], []
    match planet.type:
        case "Terrestrial":
            if planet.zone == "Green":
                count = randint(0, 5)
                for i in range(count):
                    planet.flora.append(Flora())
                count = randint(0, 5)
                for i in range(count):
                    planet.fauna.append(Fauna(planet))
            else:
                count = randint(0, 1)
                for i in range(count):
                    planet.flora.append(Flora())
                count = randint(0, 1)
                for i in range(count):
                    planet.fauna.append(Fauna(planet))

        case "Gas Giant":
            if planet.zone == "Green":
                count = randint(0, 1)
                for i in range(count):
                    planet.fauna.append(Fauna(planet))
            else:
                pass

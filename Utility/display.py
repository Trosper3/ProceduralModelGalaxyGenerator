from Objects import stars, starCount
from Objects.stellar_objects import Star
from Utility.input import setSeed, setGalaxyName

def displayStarInfo(starNum: int):
    print("\n" + str(stars[starNum].name) + ":\n" +
               "\tLocation - \t\t\t" + str(stars[starNum].location) + " AU\n" +
               "\tMass - \t\t\t\t" + str(stars[starNum].mass) + " kg\n" +
               "\tRadius - \t\t\t" + str(stars[starNum].radius) + " m\n" +
               "\tCore Temperature - \t\t" + str(stars[starNum].core_temp) + " K\n" +
               "\tGravity - \t\t\t" + str(stars[starNum].gravity) + " N\n" +
               "\tLuminosity - \t\t\t" + str(stars[starNum].luminosity) + " W\n\n"
               "Planets:")
    for j in range(0, len(stars[starNum].planets)):
        print("\t" + str(stars[starNum].planets[j].name) + ":\n" +
                   "\t\tDistance From Star - \t" + str(stars[starNum].planets[j].distance_from_star) + " AU\n" +
                   "\t\tZone - \t\t\t" + str(stars[starNum].planets[j].zone) + "\n" +
                   "\t\tType - \t\t\t" + str(stars[starNum].planets[j].type) + "\n" +
                   "\t\tSurface Temperature - \t" + str(stars[starNum].planets[j].surf_temp) + " K\n" +
                   "\t\tAlbedo - \t\t" + str(stars[starNum].planets[j].albedo) + "\n" +
                   "\t\tAtmosphere Pressure - \t" + str(stars[starNum].planets[j].atmosphericPressure) + "\n" +
                   "\t\tAtmosphere Density - \t" + str(stars[starNum].planets[j].atmosphericDensity) + "\n" +
                   "\t\tAtmosphere Mass - \t" + str(stars[starNum].planets[j].atmosphericMass) + "\n" +
                   "\t\tMean Molecular Mass - \t" + str(stars[starNum].planets[j].meanMolecularMass) + "\n" +
                   "\t\tMass - \t\t\t" + str(stars[starNum].planets[j].mass) + " kg\n" +
                   "\t\tRadius - \t\t" + str(stars[starNum].planets[j].radius) + " m\n" +
                   "\t\tGravity - \t\t" + str(stars[starNum].planets[j].gravity) + " N\n" +
                   "\t\tAtmosphere Makeup - \t" + str(stars[starNum].planets[j].atmosphereComponents) + "\n\n" +
                   "\t\tFlora:")
        if len(stars[starNum].planets[j].flora) > 0:
            for k in range(len(stars[starNum].planets[j].flora)):
                print("\t\t\t" + str(stars[starNum].planets[j].flora[k].name) + "\n" +
                           "\t\t\t\tDiet - " + str(stars[starNum].planets[j].flora[k].diet) + "")
        else:
            print("\t\t\tNone")

        print("\t\tFauna:")

        if len(stars[starNum].planets[j].fauna) > 0:
            for l in range(len(stars[starNum].planets[j].fauna)):
                print("\t\t\t" + str(stars[starNum].planets[j].fauna[l].name) + "\n" +
                           "\t\t\t\tDiet - " + str(stars[starNum].planets[j].fauna[l].diet) + "\n")
        else:
            print("\t\t\tNone\n")

    print("____________________________________________________________________________________________________\n")

def writeToFile(galaxyName, seedNum):

    seed = setSeed(seedNum)

    # """
    file = open("Galaxy Data/" + setGalaxyName(galaxyName) + " Galaxy", "w")
    # file = open("C:/Users/mtros/OneDrive/Desktop/" + galaxyName + " Galaxy", "w")
    stars.clear()
    file.write(
        galaxyName + " Galaxy\t\t\t\t\tSeed: " + str(seed) + "\n____________________________________________________________________________________________________\n")
    for i in range(starCount):
        stars.append(Star())
        file.write("\n" + str(stars[i].name) + ":\n" +
                   "\tLocation - \t\t\t" + str(stars[i].location) + " AU\n" +
                   "\tMass - \t\t\t\t" + str(stars[i].mass) + " kg\n" +
                   "\tRadius - \t\t\t" + str(stars[i].radius) + " m\n" +
                   "\tCore Temperature - \t\t" + str(stars[i].core_temp) + " K\n" +
                   "\tGravity - \t\t\t" + str(stars[i].gravity) + " N\n" +
                   "\tLuminosity - \t\t\t" + str(stars[i].luminosity) + " W\n\n"
                                                                        "Planets:\n")
        for j in range(0, len(stars[i].planets)):
            file.write("\n" + str(stars[i].planets[j].name) + ":\n" +
                       "\tDistance From Star - \t\t" + str(stars[i].planets[j].distance_from_star) + " AU\n" +
                       "\tZone - \t\t\t\t" + str(stars[i].planets[j].zone) + "\n" +
                       "\tType - \t\t\t\t" + str(stars[i].planets[j].type) + "\n" +
                       "\tSurface Temperature - \t\t" + str(stars[i].planets[j].surf_temp) + " K\n" +
                       "\tAlbedo - \t\t\t" + str(stars[i].planets[j].albedo) + "\n" +
                       "\tAtmosphere Pressure - \t\t" + str(stars[i].planets[j].atmosphericPressure) + "\n" +
                       "\tAtmosphere Density - \t\t" + str(stars[i].planets[j].atmosphericDensity) + "\n" +
                       "\tAtmosphere Mass - \t\t" + str(stars[i].planets[j].atmosphericMass) + "\n" +
                       "\tMean Molecular Mass - \t\t" + str(stars[i].planets[j].meanMolecularMass) + "\n" +
                       "\tMass - \t\t\t\t" + str(stars[i].planets[j].mass) + " kg\n" +
                       "\tRadius - \t\t\t" + str(stars[i].planets[j].radius) + " m\n" +
                       "\tGravity - \t\t\t" + str(stars[i].planets[j].gravity) + " N\n" +
                       "\tAtmosphere Makeup - \t\t" + str(stars[i].planets[j].atmosphereComponents) + "\n" +
                       "\tFlora:" + "\n")
            if len(stars[i].planets[j].flora) > 0:
                for k in range(len(stars[i].planets[j].flora)):
                    file.write("\t\t" + str(stars[i].planets[j].flora[k].name) + "\n" +
                               "\t\t\tDiet - " + str(stars[i].planets[j].flora[k].diet) + "\n\n")
            else:
                file.write("\t\t\tNone\n\n")

            file.write("\tFauna:" + "\n")

            if len(stars[i].planets[j].fauna) > 0:
                for l in range(len(stars[i].planets[j].fauna)):
                    file.write("\t\t" + str(stars[i].planets[j].fauna[l].name) + "\n" +
                               "\t\t\tDiet - " + str(stars[i].planets[j].fauna[l].diet) + "\n\n")
            else:
                file.write("\t\t\tNone\n\n")

        file.write(
            "____________________________________________________________________________________________________\n")

    file.close()
    # """
from random import randint, choices

# ******************** Atomic Masses ******************** #

atomicMasses = {'H':1.008, 'N':14.007, 'O':15.999, 'F':18.998, 'Cl':35.45, 'He': 4.003, 'Ne':20.180, 'Ar':39.95, 'Kr':83.798, 'Xe':131.293, 'Rn':222, 'C':12.011}

# ******************** Molecular Components ******************** #

gasElements = ['H','N','O','F','Cl','He','Ne','Ar','Kr','Xe','Rn','C']
nobleGases = ['He','Ne','Ar','Kr','Xe','Rn']
midGases = ['C','F','Cl']
freeGases = ['H','N']
gasCount = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

molecularMass = 0

# ******************** Molecular Creation ******************** #

def createMolecule():

    atomList = []
    createdAtom = ""
    moleculeMass = 0

    (countH, countN, countO, countF, countCl, countHe, countNe, countAr, countKr, countXe, countRn, countC) \
        = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    atomRef = {'H': countH, 'N': countN, 'O': countO, 'F': countF, 'Cl': countCl, 'He': countHe,
               'Ne': countNe, 'Ar': countAr, 'Kr': countKr, 'Xe': countXe, 'Rn': countRn, 'C': countC}

    gasNum = choices(gasCount, weights=[25000, 35000, 10000, 2048, 1024, 512, 128, 128, 32, 16, 16, 4, 2, 2])
    atomChoice = choices(gasElements, weights=[25000000, 50000000, 50000000, 1000, 1000, 5000, 20000, 1000000, 1000, 1000, 1000, 50000000], k=gasNum[0])

    #"""
    for i in range(len(atomChoice)):
        for element in gasElements:
            if atomChoice[i] == element:
                if element == 'He' or element == 'Ne' or element == 'Ar' or element == 'Kr' or element == 'Xe' or element == 'Rn':
                    if atomRef[element] != 0:
                        continue
                    else:
                        atomList.append(atomChoice[i])
                        atomRef[element] += 1
                if element == 'C' or element == 'F' or element == 'Cl':
                    if atomRef[element] != 0:
                        pass
                    else:
                        atomList.append(atomChoice[i])
                        atomRef[element] += 1
                if element == 'H' or element == 'N' or element == 'O':
                    if atomRef[element] != 0:
                        atomRef[element] += 1
                    else:
                        atomList.append(atomChoice[i])
                        atomRef[element] += 1

    #"""
    for i in range(len(atomList)):
        for gas in nobleGases:
            if atomList[i] == gas:
                createdAtom = gas
                moleculeMass += atomicMasses[gas]
                return createdAtom

        for gas in midGases:
            if atomList[i] == gas:
                moleculeMass += atomicMasses[gas]
                for free in freeGases:
                    if atomList[i-1] == free or atomList[i-1] == 'O':
                        temp = atomList[i-1]
                        atomList[i-1] = atomList[i]
                        atomList[i] = temp
                    """
                    try:
                        atomList[i-2]
                    except IndexError:
                        #status = False
                        continue
                    status = True
                    if status == True:
                        if atomList[i-2] == free or atomList[i-2] == 'O':
                            temp = atomList[i - 2]
                            atomList[i - 2] = atomList[i-1]
                            atomList[i-1] = temp
                    """

        for gas in freeGases:
            if atomList[i] == gas:
                moleculeMass += atomicMasses[gas]
                for mid in midGases:
                    if atomList[i-1] == mid:
                        pass
                    if atomList[i-1] == 'O':
                        temp = atomList[i-1]
                        atomList[i-1] = atomList[i]
                        atomList[i] = temp

    for i in range(len(atomList)):
        createdAtom += str(atomList[i]) + str(atomRef[atomList[i]])

    molecularMass = moleculeMass

    createdAtom = createdAtom.replace("1","")

    return createdAtom

# ******************** Atmosphere Creation ******************** #

def createAtmosphere(planet):

    compounds = []

    for i in range(randint(3,5)):
        compound = createMolecule()

        if compounds.__contains__(compound):
            pass
        else:
            compounds.append(compound)
        if compounds.__contains__('C'):
            index = compounds.index('C')
            compounds.pop(index)
            compounds.append(createMolecule())

    planet.meanMolecularMass = molecularMass

    return compounds

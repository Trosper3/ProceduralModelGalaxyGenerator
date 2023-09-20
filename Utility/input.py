from random import seed
from Utility.naming import produceName

galaxyName = ""
def setSeed(seedNum):
    if seedNum == 0 or seedNum == '0':
        seed()
        return None
    else:
        seed(int(seedNum))
        return int(seedNum)

def setGalaxyName(name):
    if name == "0":
        galaxyName = produceName()
    else:
        galaxyName = name

    return galaxyName

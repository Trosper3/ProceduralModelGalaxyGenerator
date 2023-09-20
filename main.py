#!/usr/bin/env python3

from Objects import starCount
from Utility.display import writeToFile, displayStarInfo

seedNum = input("\nEnter a Seed or Enter 0 To Omit Seed >> ")
print()
galaxyName = input("Enter a Galaxy Name or Enter 0 To Generate Random Name >> ")
print()

writeToFile(galaxyName, seedNum)

while True:
    starNum = input("Enter a Star Number Between 1 and " + str(starCount) + " To See Information >> ")
    print()
    if int(starNum) <= starCount:
        displayStarInfo(int(starNum))
    else:
        print("Enter a Number Less Than Or Equal To " + str(starCount) + "\n")







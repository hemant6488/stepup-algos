#!/bin/python

def countingValleys(n, s):
    valleyCounter = 0
    currentInclination = 0
    inValley = False

    for currentStep in s:
        if currentStep == "D":
            currentInclination -= 1
        if currentStep == "U":
            currentInclination += 1

        if not inValley and currentInclination < 0: 
            inValley = True
            valleyCounter += 1

        if inValley and currentInclination == 0:
            inValley = False

    return valleyCounter


if __name__ == '__main__':
    numberOfSteps = int(input())
    steps = list(input().strip())

    valleys = countingValleys(numberOfSteps, steps)

    print(valleys)

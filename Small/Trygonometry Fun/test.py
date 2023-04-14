###################
#  CONFIGURATION:
MaxPosition = int(100) # On left and right, so when inputting, it gets "doubled".
####################

import os, math
from _thread import start_new_thread
from time import sleep



#while True:
#    sleep(0.1)


CurrentPosition = 0


def inputNewPosition():

    PositionInput = input(str("Input a whole Number from -" + str(MaxPosition) + " to " + str(MaxPosition) + ": "))

    if PositionInput.isdigit() or PositionInput.split("-",1)[1].isdigit():
        PositionInput = int(PositionInput)

        if PositionInput > MaxPosition:
            PositionInput = MaxPosition
        elif PositionInput < -MaxPosition:
            PositionInput = -MaxPosition
        elif PositionInput == 0:
            return(inputNewPosition())

        return(PositionInput + MaxPosition)


def rangeWithNegativeSupport(IntVariable):

    if IntVariable > 0:
        return(0, range(IntVariable))
    elif IntVariable < 0:
        return(range(IntVariable), 0)
    else:
        return([])
        

def printPosition(LineCharacter):

    SpaceCharacters = []

    for i in range(CurrentPosition):

        SpaceCharacters.append(" ")

    print("".join(SpaceCharacters), LineCharacter)


def moveToAndPrint(Position):

    # The function 'cuts' the steps away from the inputted Position into two Parts - Part1 and Part2, because they have different 'visuals'.

    global CurrentPosition

    StepsInBetween = Position - CurrentPosition

    if StepsInBetween == -MaxPosition: # FOR SOME REASON THIS PASSES WHEN IT SHOULDN'T
        return 
    
    if StepsInBetween > 0:
        LineCharacter = "\\" # This will print '\', NOT '\\', because it's a special Python string.
    elif StepsInBetween < 0:
        LineCharacter = "/"
    else:
        LineCharacter = "|"

    HalfOfStepsInBetween = StepsInBetween / 2

    StepsLeftInPart1 = math.ceil(HalfOfStepsInBetween)
    StepsLeftInPart2 = math.floor(HalfOfStepsInBetween)

    Part1DestinationPosition = CurrentPosition + StepsLeftInPart1
    Part2DestinationPosition = Part1DestinationPosition + StepsLeftInPart2


    while CurrentPosition != Part1DestinationPosition:
        
        MoveBy = math.ceil(StepsLeftInPart1 * 0.1)

        CurrentPosition += MoveBy
        StepsLeftInPart1 -= MoveBy

        printPosition(LineCharacter)

        sleep(StepsLeftInPart1 * MoveBy / MaxPosition * 0.1)

    while CurrentPosition != Part2DestinationPosition:

        MoveBy = math.ceil()

        CurrentPosition += MoveBy
        StepsLeftInPart2 -= MoveBy

        printPosition(LineCharacter)

        sleep(StepsLeftInPart2 * MoveBy / MaxPosition * 0.1)


while True:
    moveToAndPrint(inputNewPosition())


# TODO:
# 1. Fix this
# 2. Optimise the functions buy using fewer variables.
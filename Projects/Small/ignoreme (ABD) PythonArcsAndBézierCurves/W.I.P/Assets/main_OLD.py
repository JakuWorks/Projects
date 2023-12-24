
def askQuadraticBezierCurve():

    CommonError = "Wrong Position Passed! Try Again!"

    # Questions:

    PositionsMode = askUntillOptionInput(["1", "2", "3"], PositionsModeFirstMessage, "No Mode of this Number found! Select Mode Again!")

    if PositionsMode == "1": # Custom

        StartingPositionX = askUntillFloatInput("Input Starting Point Position X (a number between -400 and 400).", CommonError, Min = -400, Max = 400, CanBeEqual = True)
        StartingPositionY = askUntillFloatInput("Input Starting Point Position Y (a number between -400 and 400).", CommonError, Min = -400, Max = 400, CanBeEqual = True)

        MovingTargetPositionX = askUntillFloatInput("Input Moving Target Point Position X (a number between -400 and 400).", CommonError, Min = -400, Max = 400, CanBeEqual = True)
        MovingTargetPositionY = askUntillFloatInput("Input Moving Target Point Position Y (a number between -400 and 400).", CommonError, Min = -400, Max = 400, CanBeEqual = True)

        EndPositionX = askUntillFloatInput("Input End Position X (a number between -400 and 400).", CommonError, Min = -400, Max = 400, CanBeEqual = True)
        EndPositionY = askUntillFloatInput("Input End Position Y (a number between -400 and 400).", CommonError, Min = -400, Max = 400, CanBeEqual = True)

    elif PositionsMode == "2": # Preview

        StartingPositionX = -400
        StartingPositionY = 0

        MovingTargetPositionX = 0
        MovingTargetPositionY = 400

        EndPositionX = 400
        EndPositionY = 0

    elif PositionsMode == "3": # Full Random

        StartingPositionX = randint(-400, 400)
        StartingPositionY = randint(-400, 400)

        MovingTargetPositionX = randint(-400, 400)
        MovingTargetPositionY = randint(-400, 400)

        EndPositionX = randint(-400, 400)
        EndPositionY = randint(-400, 400)

    else:

        clearTerminal()
        print("ERROR: WRONG POSITIONSMODE SELECTED!")


    StepSize = askUntillFloatInput("Input Step Size (A number between 0 and 1 that isn't 0 (i.e. 0.001))", "Wrong Step Size Passed! Try again!", Min = 0, Max = 1, NumBlacklist = [0])
    GreyLineFrequency = askUntillFloatInput("Input Grey Line Drawing Frequency (full number) (every X steps) OR 0 to Disable", "Wrong Grey Line Frequency Passed! Try again!", Min = 0)

    clearTerminal()

    print("Starting Animation in 4 seconds...")

    return(StepSize, GreyLineFrequency, StartingPositionX,StartingPositionY, MovingTargetPositionX,MovingTargetPositionY, EndPositionX,EndPositionY) # Tuple


def askDrawOption():

    FirstMessage = """Options:
    1 - Draw an Arc
    2 - Draw a Quadratic Bézier Curve
    
    To select an Option, type it's number from this List.
"""

    RetryMessage = "No Option of this Number found! Select Option Again!"

    Mode = askUntillOptionInput(["1","2"], FirstMessage, RetryMessage)

    if Mode == "1": # Draw an Arc

        drawArc(*askDrawArc())

    elif Mode == "2": # Draw a Quadratic Bezier Curve

        drawQuadraticBezierCurve(*askQuadraticBezierCurve())


askDrawOption()
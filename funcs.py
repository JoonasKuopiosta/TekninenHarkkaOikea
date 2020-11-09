import math


def multiplicProbability(probA, probB):
    prob = 1 - (1-probA) * (1-probB)
    return prob

def getPValue(Q, t):
    P = Q**(1/t)
    return P

# Gets the rotation for UNITCIRCLES!!!!
def getUnitCircleRads(position):
    x = position.x
    y = position.y

    # Math hax
    # Because of the nature of acos, where it mirrors values
    # to both sides of x-axis, we check if y is + or - to determine
    # which side of x-axis we actually at
    # No need to worry, there are test to make sure this works xd

    if (y >= 0): # Top part of unit circle
        rads = math.acos(x)
    else: # Bottom part of unit circle
        rads = 2*math.pi - math.acos(x)

    return rads


# Reduces the given sum to 0 - 2pi range
# Accepts negative values so substraction is thus possible
def sumRads(A, B):
    total = A + B

    if (total < 0):

        while (total > 0):
            total += 2*math.pi
    
    elif (total > 2*math.pi):

        while (total < 2*math.pi):
            total -= 2*math.pi
    
    return total


def getUnitCircleFromRads(rads):

    x = math.cos(rads)
    y = math.sin(rads)

    return [x, y]
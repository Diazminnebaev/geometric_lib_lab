import math

def area(r):
    if r < 0:
        raise ValueError("r must be non-negative")
    return math.pi * r * r

def perimeter(r):
    if r < 0:
        raise ValueError("r must be non-negative")
    return 2 * math.pi * r 

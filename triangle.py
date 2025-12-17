def area(a, h):
    if a < 0 or h < 0:
        raise ValueError("a and h must be non-negative")
    return a * h / 2

def perimeter(a, b, c):
    if a < 0 or b < 0 or c < 0:
        raise ValueError("sides must be non-negative")
    # чтобы не было "треугольника" из 1,2,100
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("invalid triangle")
    return a + b + c

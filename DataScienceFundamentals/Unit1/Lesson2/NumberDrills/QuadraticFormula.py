import math


def quadratic_formula(a, b, c):

    root1 = (-b - math.sqrt(b**2 - 4*a*c)) / (2 * a)

    root2 = (-b + math.sqrt(b**2 - 4*a*c)) / (2 * a)

    return [root1, root2]

from math import acos, sin

def triangle_area(side1, side2, side3):
    included_angle = acos((side1**2 + side2**2 - side3**2) / (2*side1*side2))   # Modified cos-sin rule formula
    area = 0.5 * side2 * side1 * sin(included_angle)

    return area

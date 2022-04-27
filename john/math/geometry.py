"""
Misc geometry routines

Mostly for area calculations.

functions:
    circle_area()
    rectangle_area()
"""
from math import pi

print("pi: {}\n".format(pi))


def circle_area(diameter):
    """
    Calculate area of circle

    :param diameter: diameter of circle
    :return: area of circle
    """
    radius = diameter / 2
    return pi * (radius ** 2)

def rectangle_area(length, width):
    """
    Calculate area of rectangle

    :param length: length of one side
    :param width: length of other side
    :return: area of rectangle
    """
    return length * width

# "private" or "protected"
def _spam():
    print("spam spam spam")

if __name__ == '__main__':  # if running as script (NOT imported)
    print("HELLO OUT THERE")

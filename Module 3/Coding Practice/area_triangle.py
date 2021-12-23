"""
returns the volume of the sphere.

Author: Yaozheng Wang
CS5001 Coding Practice
Module 3
question 6 Area of Triangle
2021-11-5
"""
# Import math to compute the root of number
import math


# Function: returns the area of a triangle
def area_triangle(side_one, side_two, side_three):
    """
    Functionl: returns the area of a triangle
    :param side_one: the first side of triangle
    :param side_two: the second side of triangle
    :param side_three: the third side of triangle
    :return: the area of a triangle
    """
    # Compute the half of the triangles perimeter
    perimeter = (side_one + side_two + side_three) / 2
    # Compute the area of triangle
    number_one = perimeter - side_one
    number_two = perimeter - side_two
    number_three = perimeter - side_three
    area = math.sqrt(perimeter * number_one * number_two * number_three)
    # Return the area triangle
    return area


def main():
    print(area_triangle(3, 4, 5))
    print(area_triangle(5, 5, 5))


if __name__ == "__main__":
    main()

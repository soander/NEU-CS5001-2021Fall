"""
returns the volume of the sphere.

Author: Yaozheng Wang
CS5001 Coding Practice
Module 3
question 5 Volume of a sphere
2021-11-4
"""


# Function: returns the volume of the sphere.
def volume_sphere(radius):
    """
    Function: volume_sphere
        returns the volume of the sphere.
    :param radius: the radius of sphere
    :return: the volume of sphere
    """
    pi = 3.14159
    volume_of_sphere = 4 * pi * radius ** 3 / 3
    return volume_of_sphere


def main():
    print(volume_sphere(6.0))


if __name__ == "__main__":
    main()

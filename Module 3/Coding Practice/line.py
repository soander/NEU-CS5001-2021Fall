"""
a function to return a string
that consists of 50 copies of the x character

Author: Yaozheng Wang
CS5001 Coding Practice
Module 3
question 1 Line
2021-11-4
"""


# Return a string that consists of 50 copies of the x character
def line():
    """
    Function: line
        returns a string that consists of 50 copies of the x character
    :return: A 50 x string
    """
    string = str(50 * "x")
    return string


def main():
    print(line())


if __name__ == "__main__":
    main()

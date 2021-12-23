"""
a function to returns true if they are
equal to one another, and false otherwise.

Author: Yaozheng Wang
CS5001 Coding Practice
Module 3
question 3 Equal
2021-11-4
"""


# a function to returns true if they are
# equal to one another, and false otherwise.
def is_equal(value_one, value_two):
    """
    Function: is_equal
        a function to returns true if they are
        equal to one another, and false otherwise.
    :param value_one:
        a number
    :param value_two:
        a number
    :return: True if two numbers are equal, otherwise false
    """
    return value_two == value_one


def main():
    print(is_equal(1, 1))
    print(is_equal(1, 3))


if __name__ == "__main__":
    main()

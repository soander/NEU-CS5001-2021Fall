"""
a function to add together
two values and returns the total

Author: Yaozheng Wang
CS5001 Coding Practice
Module 3
question 2 Plus
2021-11-4
"""


# a function to add together
# two values and returns the total
def plus(value_one, value_two):
    """
    Function: plus
        add together two values and returns the total
    :return: The total results of two values
    """
    total = value_one + value_two
    return total


def main():
    print(plus(1, 2))
    print(plus("10", "15"))
    print(plus("Eleanor", "Rigby"))


if __name__ == "__main__":
    main()

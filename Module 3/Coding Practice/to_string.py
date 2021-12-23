"""
takes any value as a parameter
returns the string equivalent
of that parameter.

Author: Yaozheng Wang
CS5001 Coding Practice
Module 3
question 8 To string
2021-11-5
"""


# returns the string equivalent
# of that parameter.
def to_string(parameter):
    """
    Function: takes any value as a parameter
        returns the string equivalent
        of that parameter.
    :param parameter: Any input parameter
    :return: A string equivalent to the parameter
    """
    string = str(parameter)
    return string


def main():
    print(to_string(1))
    print(type(to_string(1)))


if __name__ == "__main__":
    main()

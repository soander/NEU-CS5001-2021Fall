"""
two parameter values and returns the one that comes first
two numeric values, it would return the smaller of the two
two strings, it would return the one that comes first lexicographically

Author: Yaozheng Wang
CS5001 Coding Practice
Module 3
question 4 First
2021-11-4
"""


def first(parameter_one, parameter_two):
    """
    Funciton: first
        two parameter values and returns the one that comes first
        two numeric values, it would return the smaller of the two
        two strings, it would return the one that comes first lexicographically
    :param parameter_one: the first parameter
    :param parameter_two: the second parameter
    :return: the final result
    """
    # Case: two numeric values
    if isinstance(parameter_one and parameter_two, int or float):
        if parameter_one < parameter_two:
            return parameter_one
        else:
            return parameter_two
    # Case: two strings
    if isinstance(parameter_one and parameter_two, str):
        string = parameter_one + "\n" + parameter_two
        string_split = string.split()
        string_split.sort()
        return string_split[0]


def main():
    print(first(1, 2))
    print(first(2, 1))
    print(first("hello", "the"))
    print(first("the", "hello"))


if __name__ == "__main__":
    main()

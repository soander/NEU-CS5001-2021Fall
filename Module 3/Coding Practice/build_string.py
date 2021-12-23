"""
takes a string value, and three integer values
and returns a single string containing 3 lines.
One each line, the string value is repeated the
specified number of times.

Author: Yaozheng Wang
CS5001 Coding Practice
Module 3
question 9 Building a string
2021-11-5
"""


# takes a string value, and three integer values
# and returns a single string containing 3 lines.
# One each line, the string value is repeated the
# specified number of times.
def build_string(string, number_one, number_two, number_three):
    """
    Function:takes a string value, and three integer values
        and returns a single string containing 3 lines.
        One each line, the string value is repeated the
        specified number of times.
    :param string: Input a string
    :param number_one: the first line repeat time
    :param number_two: the second line repeat time
    :param number_three: the third line repeat time
    :return: a single string containing 3 lines.
    """
    # Create the empty result_string
    result_string = ""
    # Create the repeat times list
    time = [number_one, number_two, number_three]
    # Use for loop to create the result_string
    for line in range(3):
        result_string += string * time[line]
        if line != 2:
            result_string += "\n"
    # Return the result_string
    return result_string


def main():
    print(build_string("Love", 1, 2, 3))
    print(build_string("Love", 2, 1, 0))
    print(build_string("", 3, 3, 3))


if __name__ == "__main__":
    main()

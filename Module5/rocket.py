"""
a program can draw a rocket ship

Author: Yaozheng Wang
CS5001 homework04
2021-10-17
"""


# A function to draw tip_of_rocket
def tip_of_rocket(size):
    """
    Function: A function to draw tip_of_rocket
    :param size: The input size of rocket
    :return: A string representing the tip_of_rocket
    """
    # Create the empty tip_of_rocket
    the_tip_of_rocket = ""
    # Use while loop and if decision to draw the_tip_of_rocket
    height = 0
    while height < size * 2 - 1:
        width = 0
        while width < size * 4 + 2:
            if size * 2 - (height + 1) <= width < size * 2:
                the_tip_of_rocket += "/"
            elif width == size * 2 or width == size * 2 + 1:
                the_tip_of_rocket += "*"
            elif size * 2 + 1 < width <= size * 2 + (height + 2):
                the_tip_of_rocket += "\\"
            else:
                the_tip_of_rocket += " "
            width += 1
        the_tip_of_rocket += "\n"
        height += 1
    # Return the_tip_of_rocket
    return str(the_tip_of_rocket)


# A function to draw separator_of_rocket
def separator_of_rocket(size):
    """
    Function: A function to draw separator_of_rocket
    :param size: The input size of rocket
    :return: A string representing the separator_of_rocket
    """
    # Create the empty the_separator_of_rocket
    the_separator_of_rocket = ""
    # Use while loop and if decision to create the_separator_of_rocket
    width = 0
    while width < size * 4 + 2:
        if width % 2 != 0 and width != size * 4 + 1:
            the_separator_of_rocket += "="
        elif width % 2 == 0 and width != 0:
            the_separator_of_rocket += "*"
        else:
            the_separator_of_rocket += "+"
        width += 1
    the_separator_of_rocket += "\n"
    # Return the_separator_of_rocket
    return str(the_separator_of_rocket)


# A function to draw top and bottom_of_rocket
def top_and_bottom_of_rocket(size):
    """
    Function: A function to draw top_and_bottom_of_rocket
    :param size: The input size of rocket
    :return: A string representing the top_and_bottom_of_rocket
    """
    # Create the empty top_and_bottom_of_rocket
    the_top_and_bottom_of_rocket = ""
    height = 0
    # Use while loop to create top_and_bottom_of_rocket
    while 0 <= height < size:
        the_top_and_bottom_of_rocket += "|" + "." * height \
                                        + "\\/" * (size - height) \
                                        + "." * 2 * height \
                                        + "\\/" * (size - height) \
                                        + "." * height + "|\n"
        height += 1
    while size <= height < size * 2:
        the_top_and_bottom_of_rocket += "|" + "." * (size * 2 - 1 - height) \
                                        + "/\\" * (height - size + 1) \
                                        + "." * 2 * (size * 2 - 1 - height) \
                                        + "/\\" * (height - size + 1) \
                                        + "." * (size * 2 - 1 - height) + "|\n"
        height += 1
    # Return the top_and_bottom_of_rocket
    return str(the_top_and_bottom_of_rocket)


# A function to draw middle_of_rocket
def middle_of_rocket(size):
    """
    Function: A function to draw middle_of_rocket
    :param size: The input size of rocket
    :return: A string representing the middle_of_rocket
    """
    # Create the empty middle_of_rocket
    the_middle_of_rocket = ""
    # Use while loop to create middle_of_rocket
    height = 0
    while 0 <= height < size:
        the_middle_of_rocket += "|" + "." * (size - 1 - height) \
                                + "/\\" * (height + 1) \
                                + "." * 2 * (size - 1 - height) \
                                + "/\\" * (height + 1) \
                                + "." * (size - 1 - height) + "|\n"
        height += 1
    while size <= height < size * 2:
        the_middle_of_rocket += "|" + "." * (height - size) \
                                + "\\/" * (size * 2 - height) \
                                + "." * 2 * (height - size) \
                                + "\\/" * (size * 2 - height) \
                                + "." * (height - size) + "|\n"
        height += 1
    # Return the middle_of_rocket
    return str(the_middle_of_rocket)


# A function to draw the whole rocket ship
def rocket(size):
    """
    Function: A function to draw the whole rocket ship
    :param size: The input size of rocket
    :return: A string representing the whole rocket ship
    """
    # Use previous functions to create the whole rocket ship
    rocket_ship = tip_of_rocket(size) + separator_of_rocket(size) \
        + top_and_bottom_of_rocket(size) \
        + separator_of_rocket(size) \
        + middle_of_rocket(size) \
        + separator_of_rocket(size) \
        + top_and_bottom_of_rocket(size) \
        + separator_of_rocket(size) \
        + tip_of_rocket(size)
    return rocket_ship


# A function to get input and test rocket function
def main():
    """
    Function: A function to get input and test rocket function
    :return: The test results about rocket function
    """
    # Get the rocket size input and get the rocket
    size = int(input("Enter size: "))
    if size < 3:
        print("Rocket sizes must be at least 3")
    else:
        rocket(size)
        print(rocket(size))

    # Set the fail number counter
    fail_number = 0
    # Expected and actual results when its size is 3
    expected_tip_of_rocket = "     /**\\     \n" \
                             "    //**\\\\    \n" \
                             "   ///**\\\\\\   \n" \
                             "  ////**\\\\\\\\  \n" \
                             " /////**\\\\\\\\\\ \n"
    expected_separator_of_rocket = "+=*=*=*=*=*=*+\n"
    expected_top_and_bottom_of_rocket = "|\\/\\/\\/\\/\\/\\/|\n" \
                                        "|.\\/\\/..\\/\\/.|\n" \
                                        "|..\\/....\\/..|\n" \
                                        "|../\\..../\\..|\n" \
                                        "|./\\/\\../\\/\\.|\n" \
                                        "|/\\/\\/\\/\\/\\/\\|\n"
    expected_middle_of_rocket = "|../\\..../\\..|\n" \
                                "|./\\/\\../\\/\\.|\n" \
                                "|/\\/\\/\\/\\/\\/\\|\n" \
                                "|\\/\\/\\/\\/\\/\\/|\n" \
                                "|.\\/\\/..\\/\\/.|\n" \
                                "|..\\/....\\/..|\n"
    actual_tip_of_rocket = tip_of_rocket(3)
    actual_separator_of_rocket = separator_of_rocket(3)
    actual_top_and_bottom_of_rocket = top_and_bottom_of_rocket(3)
    actual_middle_of_rocket = middle_of_rocket(3)
    # Compare the function result with expected result
    if expected_tip_of_rocket == actual_tip_of_rocket:
        print("tip_of_rocket\n"
              "PASSED!\n")
    else:
        print("tip_of_rocket\n"
              "FAILED!\n")
        fail_number += 1
    if expected_separator_of_rocket == actual_separator_of_rocket:
        print("separator_of_rocket\n"
              "PASSED!\n")
    else:
        print("separator_of_rocket\n"
              "FAILED!\n")
        fail_number += 1
    if expected_top_and_bottom_of_rocket \
            == actual_top_and_bottom_of_rocket:
        print("top_and_bottom_of_rocket\n"
              "PASSED!\n")
    else:
        print("top_and_bottom_of_rocket\n"
              "FAILED!\n")
        fail_number += 1
    if expected_middle_of_rocket == actual_middle_of_rocket:
        print("middle_of_rocket\n"
              "PASSED!\n")
    else:
        print("middle_of_rocket\n"
              "FAILED!\n")
        fail_number += 1
    # Output the test result
    if fail_number == 0:
        print("All tests passed!")
    else:
        print("Some tests failed!")


if __name__ == "__main__":
    main()

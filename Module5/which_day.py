"""
Code to return the weekday according to number

Author: Yaozheng Wang
CS5001 lab05
lab05 Q4
2021-10-8
"""


# A function to return the weekday according to number
def which_day(number):
    """
    Function: A function to return the weekday according to number
    :param number: An integer 1 and 7 to represent weekday
    :return: The weekday corresponding number
    """
    # Make a list about weekday
    weekday = ["Sunday", "Monday", "Tuesday", "Wednesday",
               "Thursday", "Friday", "Saturday"]
    # Make a list about number
    integer = ["1", "2", "3", "4", "5", "6", "7"]
    # Set index for while loop
    index = 0
    # Use while loop to return weekday
    while index < len(integer):
        if number == int(integer[index]):
            return weekday[index]
        index += 1


def main():
    """
    Function: A function to test the which_day function
    :return: The test results of which_day function
    """
    # Make a list about weekday
    weekday = ["Sunday", "Monday", "Tuesday", "Wednesday",
               "Thursday", "Friday", "Saturday"]
    # Set a fail counter
    number_fail = 0
    # Use while loop to test all possible input
    test_number = 0
    while test_number < 7:
        expected = weekday[test_number]
        actual = which_day(test_number + 1)
        print("Test", test_number + 1,
              "\nExpected......", expected,
              "\nActual........", actual)
        # Compare the function result with expected test result
        if actual == expected:
            print("PASSED!\n")
        else:
            print("FAILED!\n")
        test_number += 1
    # Output the test result
    if number_fail == 0:
        print("All tests passed!")
    else:
        print("Some tests failed!")


if __name__ == "__main__":
    main()

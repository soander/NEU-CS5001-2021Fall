"""
Code to compute the average grade

Author: Yaozheng Wang
CS5001
lab05 Q1
2021-10-8
"""
# Import the random and math function to get random numbers and do math
import math
import random


# Make a function to compute the average of the grades
def average_grade(grade):
    """
    Function: A function to compute the average of the grades
    :param grade: A list of grades between 0 and 100
    :return: The average result of grades
    """
    # Make an empty variable for while loop
    a = 0
    # Make an empty summation result of grades
    summation = 0
    # Use while loop to add grades in the list
    while a < len(grade):
        summation += grade[a]
        a += 1
    # Compute the average grade of the list
    mean = summation / len(grade)
    # Return the average grade result
    return mean


# A function to test the average_grade function
def test_average_grade(grade):
    """
    Function: A function to test the average_grade function
    :param grade: A list of grades is prepared to be tested
    :return: The True or False result in test
    """
    # The excepted and actual results in test
    excepted = sum(grade) / len(grade)
    actual = average_grade(grade)
    # Use math to make the test decisions within a threshold
    if math.fabs(excepted - actual) < 0.001:
        print("\tThe average grade of grade_list",
              grade, "is", actual,
              "and it should have returned", excepted)
        print("\tExpected......", excepted)
        print("\tActual........", actual)
        print("PASSED!")
        return True
    else:
        print("FAILED!")
        return False


# A function to generate grade list and use the test_average_grade function
def main():
    """
    A function to generate grade list including 10 numbers between 0 and 100
    and use the average_grade function
    :return: The tests' result of function
    """
    # Set the number fail counter
    number_fail = 0
    # The test number
    test = 0
    number_of_test = 100
    # Make an empty grade list
    while test < number_of_test:
        grade_list = []
        # Use the random to get 10 numbers between 0 and 100 in a list
        while len(grade_list) < 10:
            grade_list.append(random.random() * 100)
        # Use the test_average_grade function to test the result
        passed = test_average_grade(grade_list)
        if not passed:
            number_fail += 1
            break
        test += 1

    # Output the test result
    if number_fail == 0:
        print("\nAll tests passed!")
    else:
        print("\nSome tests failed!")


if __name__ == "__main__":
    main()

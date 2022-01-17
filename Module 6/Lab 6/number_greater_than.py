"""
Code to get day string

Author: Yaozheng Wang
CS5001 lab06
lab05 Q2
2021-10-12
"""
# Import the random method to get the same and random length
import random


# A function to compare the same index items of list1 and list2
def number_greater_than(list1, list2):
    """
    Function: A function to compare the same index items of list1 and list2
    :param list1: A list of floats
    :param list2: A list of floats has the same length as list1
    :return: The number of element in first list that are bigger than list2
    """
    # Set the counter
    counter = 0
    # Use for loop to compare the item in list1 and list2
    for i in range(len(list1)):
        # Use if to decide the return number
        if list1[i] > list2[i]:
            counter += 1
    # Return the final result
    return counter


# Test case 1: the first list and second list are random
def case1_random_lists():
    # Set the fail number
    fail_number = 0
    # Use for loop to test the number_greater_than function 10 times
    for test in range(0, 10):
        # Case 1: the first list and second list are random
        list1 = []
        list2 = []
        # Use while loop to get the same length list1 and list2
        for index in range(random.randint(3, 6)):
            # Fill random float between 0 and 10 into the list1 and list2
            list1.append(random.random() * 10)
            list2.append(random.random() * 10)
        # The excepted and actual results in test
        bigger_number = []
        i = 0
        while i < len(list1):
            if list1[i] > list2[i]:
                bigger_number.append(list1[i])
            i += 1
        excepted = len(bigger_number)
        actual = number_greater_than(list1, list2)
        print("\nCase 1 Test", test + 1,
              "\nThe first list is", list1,
              "\nThe second list is", list2,
              "\nExcepted......", excepted,
              "\nActual........", actual)
        # Decide the test result
        if excepted == actual:
            print("PASSED!")
        else:
            print("FAILED!")
            fail_number += 1
    return fail_number


# Test case 2: the first list always smaller than the second list
def case2_first_always_smaller():
    # Set the test counter and fail number
    fail_number = 0
    # Use for loop to test the number_greater_than function 10 times
    for test in range(0, 10):
        # Case 2: the first list always smaller than the second list
        list1 = []
        list2 = []
        # Use while loop to get the same length list1 and list2
        for index in range(random.randint(3, 6)):
            # Fill random float between 0 and 10 into the list1 and list2
            list1.append(random.random() * 10)
            list2.append(list1[-1] + 0.0003 + random.random() * 5)
        # The excepted and actual results in test
        excepted = 0
        actual = number_greater_than(list1, list2)
        print("\nCase 2 Test", test + 1,
              "\nThe first list is", list1,
              "\nThe second list is", list2,
              "\nExcepted......", excepted,
              "\nActual........", actual)
        # Decide the test result
        if excepted == actual:
            print("PASSED!")
        else:
            print("FAILED!")
            fail_number += 1
    return fail_number


# Test case 3: the first list always bigger than the second list
def case3_first_always_bigger():
    # Set the test counter and fail number
    fail_number = 0
    # Use for loop to test the number_greater_than function 10 times
    for test in range(0, 10):
        list1 = []
        list2 = []
        # Use while loop to get the same length list1 and list2
        for index in range(random.randint(3, 6)):
            # Fill random float between 0 and 10 into the list1 and list2
            list1.append(random.random() * 10)
            list2.append(list1[-1] - 0.0003 - random.random() * 5)
        # The excepted and actual results in test
        excepted = len(list1)
        actual = number_greater_than(list1, list2)
        print("\nCase 3 Test", test + 1,
              "\nThe first list is", list1,
              "\nThe second list is", list2,
              "\nExcepted......", excepted,
              "\nActual........", actual)
        # Decide the test result
        if excepted == actual:
            print("PASSED!")
        else:
            print("FAILED!")
            fail_number += 1
    return fail_number


# A function to test the number_greater_than function
def main():
    """
    Function: A function to test the number_greater_than function
    :return: True or False of the test result of number_greater_than function
    """
    # Output the case1. case2 and case3 test result
    if case1_random_lists() & case2_first_always_smaller() \
            & case3_first_always_bigger() == 0:
        print("\nAll tests passed!")
    else:
        print("\nSome tests failed!")


if __name__ == "__main__":
    main()

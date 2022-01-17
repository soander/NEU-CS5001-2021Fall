"""
Code to add even integers in list

Author: Yaozheng Wang
CS5001 lab06
lab05 Q3
2021-10-13
"""
# Import random method to create random integer lists
import random


# A function adds all the even values in the list
def add_evens(list_of_integers):
    """
    Function: A function adds all the even values in the list
    :param list_of_integers: A list of integers as input
    :return: The summation of even values in the list
    """
    # Use for loop to filter the list_of_integers
    filtered_list = []
    for i in list_of_integers:
        if i % 2 == 0:
            filtered_list.append(i)
    # Use for loop to add all even integers in filtered_list
    summation = 0
    for a in filtered_list:
        summation += a
    return summation


# A function to test the add_even function
def main():
    """
    Function: A function to test the add_even function
    :return: Passed or Failed of tests
    """
    # Set the test counter and fail counter
    fail_number = 0
    test_number = 0
    test = 100
    # Use while loop to test the function
    while test_number < test:
        # Create random integer list with length between 10 and 20
        list_length = random.randint(10, 20)
        random_list = []
        while len(random_list) < list_length:
            random_list.append(random.randint(0, 100))
        print("\nTest", test_number + 1)
        print("The random integer list is", random_list)
        # Filter the odd numbers in random list
        even_random_list = list(filter(lambda x: x % 2 == 0, random_list))
        print("The filtered integer list is", even_random_list, end="")
        # Compare the excepted result and actual result
        excepted = sum(even_random_list)
        actual = add_evens(random_list)
        print("\nExcepted......", excepted,
              "\nActual........", actual)
        # Decide the test result
        if excepted == actual:
            print("PASSED!")
        else:
            print("FAILED!")
            fail_number += 1
        test_number += 1

    # Output the test result
    if fail_number == 0:
        print("\nAll tests passed!")
    else:
        print("\nSome tests failed!")


if __name__ == "__main__":
    main()

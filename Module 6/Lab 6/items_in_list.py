"""
Code to get day string

Author: Yaozheng Wang
CS5001 lab06
lab05 Q4
2021-10-13
"""
# Import random method to create random integer lists
import random


# A function to show a list containing values from another list
def items_in_list(list1, list2):
    """
    Function: A function to show a list containing values from another list
    :param list1: A list of integers
    :param list2: A list of integers
    :return: A list contains common elements
    """
    # Use for loop to remove duplicate elements
    filtered_list1 = []
    for a in list1:
        if a not in filtered_list1:
            filtered_list1.append(a)
    # Use for loop to remove duplicate elements
    filtered_list2 = []
    for b in list2:
        if b not in filtered_list2:
            filtered_list2.append(b)
    # Use for loop to select the common elements
    common_items = []
    for c in filtered_list1:
        for d in filtered_list2:
            if c == d:
                common_items.append(c)
    return common_items


# Test case 1: first list is bigger
def case1_first_list_is_bigger():
    # Set the test counter and fail number
    fail_number = 0
    # Use for loop to test the items_in_list 10 times
    for test in range(0, 10):
        list1_length = random.randint(5, 10)
        list2_length = random.randint(1, 4)
        list1 = []
        list2 = []
        while len(list1) < list1_length:
            list1.append(random.randint(30, 40))
        while len(list2) < list2_length:
            list2.append(random.randint(30, 40))
        print("\nCase 1 Test", test + 1)
        print("The first list is", list1,
              "\nThe second list is", list2, end="")
        # Compare the excepted result and actual result
        excepted = set(list1) & set(list2)
        actual = set(items_in_list(list1, list2))
        excepted_list = list(excepted)
        excepted_list.sort()
        actual_list = items_in_list(list1, list2)
        actual_list.sort()
        print("\nExcepted......", excepted_list,
              "\nActual........", actual_list)
        # Decide the test result
        if excepted == actual:
            print("PASSED!")
        else:
            print("FAILED!")
            fail_number += 1
    if fail_number == 0:
        print("\nAll tests passed!")
    else:
        print("\nSome tests failed!")


# Test case 2: first list is smaller
def case2_first_list_is_smaller():
    # Set the test counter and fail number
    fail_number = 0
    # Use for loop to test the items_in_list 10 times
    for test in range(0, 10):
        list1_length = random.randint(1, 4)
        list2_length = random.randint(5, 10)
        list1 = []
        list2 = []
        while len(list1) < list1_length:
            list1.append(random.randint(30, 40))
        while len(list2) < list2_length:
            list2.append(random.randint(30, 40))
        print("\nCase 2 Test", test + 1)
        print("The first list is", list1,
              "\nThe second list is", list2, end="")
        # Compare the excepted result and actual result
        excepted = set(list1) & set(list2)
        actual = set(items_in_list(list1, list2))
        excepted_list = list(excepted)
        excepted_list.sort()
        actual_list = items_in_list(list1, list2)
        actual_list.sort()
        print("\nExcepted......", excepted_list,
              "\nActual........", actual_list)
        # Decide the test result
        if excepted == actual:
            print("PASSED!")
        else:
            print("FAILED!")
            fail_number += 1
    if fail_number == 0:
        print("\nAll tests passed!")
    else:
        print("\nSome tests failed!")


# Test case 3: there are no matching items
def case3_no_matching_items():
    # Set the test counter and fail number
    fail_number = 0
    # Use for loop to test the items_in_list 10 times
    for test in range(0, 10):
        list_length = random.randint(5, 10)
        list1 = []
        list2 = []
        while len(list1) < list_length:
            list1.append(random.randint(50, 100))
        while len(list2) < list_length:
            list2.append(random.randint(1, 20))
        print("\nCase 3 Test", test + 1)
        print("The first list is", list1,
              "\nThe second list is", list2, end="")
        # Compare the excepted result and actual result
        excepted = set(list1) & set(list2)
        actual = set(items_in_list(list1, list2))
        excepted_list = list(excepted)
        excepted_list.sort()
        actual_list = items_in_list(list1, list2)
        actual_list.sort()
        print("\nExcepted......", excepted_list,
              "\nActual........", actual_list)
        # Decide the test result
        if excepted == actual:
            print("PASSED!")
        else:
            print("FAILED!")
            fail_number += 1
    if fail_number == 0:
        print("\nAll tests passed!")
    else:
        print("\nSome tests failed!")


# Test case 4: there are matching items
def case4_exist_matching_items():
    # Set the test counter and fail number
    fail_number = 0
    # Use for loop to test the items_in_list 10 times
    for test in range(0, 10):
        list_length = random.randint(10, 15)
        list1 = []
        list2 = []
        while len(list1) < list_length:
            list1.append(random.randint(15, 20))
        while len(list2) < list_length:
            list2.append(random.randint(15, 20))
        print("\nCase 4 Test", test + 1)
        print("The first list is", list1,
              "\nThe second list is", list2, end="")
        # Compare the excepted result and actual result
        excepted = set(list1) & set(list2)
        actual = set(items_in_list(list1, list2))
        excepted_list = list(excepted)
        excepted_list.sort()
        actual_list = items_in_list(list1, list2)
        actual_list.sort()
        print("\nExcepted......", excepted_list,
              "\nActual........", actual_list)
        # Decide the test result
        if excepted == actual:
            print("PASSED!")
        else:
            print("FAILED!")
            fail_number += 1
    if fail_number == 0:
        print("\nAll tests passed!")
    else:
        print("\nSome tests failed!")


# A function to test the items_in_list function
def main():
    """
    Function: A function to test the items_in_list function
    :return: The test results of items_in_list function
    """
    # Output the test result
    case1_first_list_is_bigger()
    case2_first_list_is_smaller()
    case3_no_matching_items()
    case4_exist_matching_items()


if __name__ == "__main__":
    main()

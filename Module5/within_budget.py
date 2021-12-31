"""
Code to check prices whether is in the budget

Author: Yaozheng Wang
CS5001 lab05
lab05 Q2
2021-10-8
"""
# Import the random to get the random prices and budget
import random


# A function to input a list of prices and
# filter the price that higher than budget
def within_budget(price, budget):
    """
    Function: A function to input a list of prices
    and filter the price higher than budget
    :param price: A list of prices
    :param budget: A number than prices can't exceed
    :return: The list with prices lower than budget
    """
    # Make a variable for while loop
    i = 0
    # Create the filtered_price list
    filtered_price = []
    # Use while loop to filter the price higher than budget
    while i < len(price):
        if price[i] <= budget:
            filtered_price.append(price[i])
        i += 1
    # Return the filtered price list
    return filtered_price


# A function to test within_budget function
def main():
    """
    Function: A function test within_budget function
    :return: The test result
    """
    # Set the number fail counter
    number_fail = 0
    # Set the test number
    test_number = 0
    number_of_test = 50
    # Make an empty grade list
    while test_number < number_of_test:
        price_list = []
        # Use the random.randint to get a random length (5~15 integer)
        while len(price_list) < random.randint(5, 10):
            price_list.append(random.uniform(1, 20))
        print("\nTest", test_number + 1,
              "\nPrice list......", price_list, end="")
        # Set a random budget between 5 and 10
        budget = random.uniform(5, 10)
        # Use the within_budget function to get the filtered price
        filtered_price = within_budget(price_list, budget)
        print("\nBudget..........", budget,
              "\nFiltered price..", filtered_price, "\n", end="")
        # Use while loop to decide whether filtered price less than budget
        a = 0
        while a < len(filtered_price):
            if filtered_price[a] < budget:
                a += 1
            else:
                number_fail += 1
                break
        print("PASSED!")
        # Output the whole test results
        test_number += 1
        if number_fail == 0:
            print("\nAll tests passed!")
        else:
            print("\nSome tests failed!")


if __name__ == "__main__":
    main()

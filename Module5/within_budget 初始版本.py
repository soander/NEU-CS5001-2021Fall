""""
Code to check prices whether is in the budget

Author: Yaozheng Wang
CS5001 lab05
lab05 Q2
2021-10-8
"""


# A function to input a list of prices and
# filter the price that higher than budget
def within_budget(budget):
    """
    Function: A function to input a list of prices
    and filter the price higher than budget
    :param budget: A number than prices can't exceed
    :return: The list with prices lower than budget
    """
    # Input prices in the price list
    price = input("Enter prices of a list separated by space:\n")
    price_list = price.split()
    # Use while loop to change price element to float type
    a = 0
    while a < len(price_list):
        price_list[a] = float(price_list[a])
        if price_list[a] > budget:
            price_list.pop(a)
        a += 1
    return price_list


# A function to test within_budget function
def main():
    """
    Function: A function test within_budget function
    :return: The test result
    """
    # Set a fail counter
    number_fail = 0
    # Test
    expected = [12.0, 23.0, 20.0]
    actual = within_budget(25)
    print("Testing points:", [12, 23, 34.5, 20, 38],
          "[12, 23, 20]")
    print("Expected......", expected)
    print("Actual........", actual)
    # Compare the function result with expected test result
    if [12.0, 23.0, 20.0] == actual:
        print("PASSED!\n")
    else:
        print("FAILED!\n")
        number_fail += 1
    # Output the test result
    if number_fail == 0:
        print("All tests passed!")
    else:
        print("Some tests failed!")


if __name__ == "__main__":
    main()

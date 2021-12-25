# Import random function the randint
from random import randint


# A function to check a number in Fibonacci sequence
def is_fibonacci(num):
    """
    function: A function to check a number in Fibonacci sequence
    :param num: An input number
    :return: Ture or False
    """
    if num == 0 or num == 1:
        return True
    # Use while loop to compare number with Fibonacci sequence
    a = 0
    b = 1
    while num > b:
        c = b + a
        a = b
        b = c
    return b == num


# A function to test is_fibonacci function
def main():
    """
   function: A function to test the is_fibonacci function
   :return: The test results: PASSED or FAILED
   """
    # A failure counter
    fail_num = 0
    # Set the test counter
    counter = 0
    # Use the while loop to test result
    while counter < 100:
        # Use random integers between 0 and 10000
        number = randint(0, 10000)
        # Make a fibonacci dictionary within 10000
        fibonacci = {0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,
                     233, 377, 610, 987, 1597, 2584, 4181, 6765}
        # Set the excepted result and actual result
        if number == fibonacci:
            excepted = True
        else:
            excepted = False
        actual = is_fibonacci(number)
        # Make the test decision
        if actual == excepted:
            print("\tis_fibonacci(", number, ") returned", actual,
                  "and it should have returned", excepted)
            print("\tExpected......", excepted)
            print("\tActual........", actual)
            print("PASSED!")
            counter += 1
        else:
            print("FAILED!")
            fail_num += 1
            counter += 1
    # The test result
    if fail_num == 0:
        print("All tests passed!")
    else:
        print("Some tests failed!")


if __name__ == '__main__':
    main()

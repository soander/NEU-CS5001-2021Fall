# Import the math
import math
import random


# Make a function to compare floats
def float_is_equal(float1, float2, threshold):
    """
    function: A function to compare floats whether they are close
    :param float1: A float point number
    :param float2: A float point number
    :param threshold: A value as a threshold
    :return: Ture or false about two float numbers within threshold
    """
    # Use while loop to decide whether
    while math.fabs(float1 - float2) <= threshold:
        return True
    else:
        return False


# A function to test float_is_equal function
def main():
    """
    function : A function to test float_is_equal function
    :return: The tests' result
    """
    # Make a failure counter
    num_fail = 0
    # Make a test loop
    counter = 0
    while counter < 1000:
        # Set the threshold
        threshold = 0.1
        # Make a random float between 0 and 1000
        float1 = random.random() * 1000
        float2 = float1 + threshold - 0.01
        # The excepted and actual results
        excepted = True
        actual = float_is_equal(float1, float2, threshold)
        # Make the test decisions
        if excepted == actual:
            print("\tfloat_is_equal(", float1, ",", float2,
                  ",", threshold, ") returned", actual,
                  "and it should have returned", excepted)
            print("\tExpected......", excepted)
            print("\tActual........", actual)
            print("PASSED!")
            counter += 1
        else:
            print("FAILED!")
            num_fail += 1
        counter += 1

    # The test result
    if num_fail == 0:
        print("All tests passed!")
    else:
        print("Some tests failed!")


if __name__ == "__main__":
    main()

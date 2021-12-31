"""
Code to check word whether is a palindrome

Author: Yaozheng Wang
CS5001 lab05
lab05 Q3
2021-10-8
"""


# A function to check words whether is palindrome
def is_palindrome(word):
    """
    Function: A function to check words whether is palindrome
    :param word: A word or set of words
    :return: True or False about a word regarding palindrome
    """
    # compute the length of word
    length = len(word)
    # Set an index for while loop
    index = 0
    # Use while loop to check word
    while index < length // 2:
        if word[index] == word[(-1 - index)]:
            pass
        else:
            return False
        index += 1
    return True


# A function to test is_palindrome function
def main():
    """
    Function: A function to test is_palindrome function
    :return: The test result of is_palindrome function
    """
    # Set a fail counter
    number_fail = 0
    # Test 1
    expected = True
    actual = is_palindrome("rotor")
    print("Testing points:", "rotor")
    print("Expected......", expected)
    print("Actual........", actual)
    # Compare the function result with expected test result
    if actual == expected:
        print("PASSED!\n")
    else:
        print("FAILED!\n")
        number_fail += 1

    # Test 2
    expected = False
    actual = is_palindrome("python")
    print("Testing points:", "python")
    print("Expected......", expected)
    print("Actual........", actual)
    # Compare the function result with expected test result
    if actual == expected:
        print("PASSED!\n")
    else:
        print("FAILED!\n")
        number_fail += 1

    # Test 3
    expected = True
    actual = is_palindrome("reviver")
    print("Testing points:", "reviver")
    print("Expected......", expected)
    print("Actual........", actual)
    # Compare the function result with expected test result
    if actual == expected:
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

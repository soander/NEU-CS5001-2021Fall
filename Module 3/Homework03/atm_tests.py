def atm_tests ():
    """
    function: A function to test the atm.py
    :return: The tests' result about atm.py
    """
    # A fail counter
    number_fail = 0

    # Test 1
    print("Testing points:", "98.22",
          "\n1 fifty\n2 twenties\n1 five\n1 toony\n1 loony\n2 dimes\n")
    print("Expected......", "\n""1 fifty\n2 twenties\n1 five\n1 toony\n1 loony\n2 dimes\n")
    print("Actual........\n" + dispense_the_money(98.22))
    # Compare the function result with expected test result
    if "1 fifty\n2 twenties\n1 five\n1 toony\n1 loony\n2 dimes\n" == dispense_the_money(98.22):
        print("PASSED!\n")
    else:
        print("FAILED!\n")
        number_fail += 1

        # Test 2
    print("Testing points:", "32.55",
          "\n1 twenty\n1 ten\n1 toony\n2 quarters\n1 nickle\n")
    print("Expected......", "\n""1 twenty\n1 ten\n1 toony\n2 quarters\n1 nickle\n")
    print("Actual........\n" + dispense_the_money(32.55))
    # Compare the function result with expected test result
    if "1 twenty\n1 ten\n1 toony\n2 quarters\n1 nickle\n" == dispense_the_money(32.55):
        print("PASSED!\n")
    else:
        print("FAILED!\n")
        number_fail += 1

        # Test 3
    print("Testing points:", "56.27",
          "\n1 fifty\n1 five\n1 loony\n1 quarter\n")
    print("Expected......", "\n""1 fifty\n1 five\n1 loony\n1 quarter\n")
    print("Actual........\n" + dispense_the_money(56.27))
    # Compare the function result with expected test result
    if "1 fifty\n1 five\n1 loony\n1 quarter\n" == dispense_the_money(56.27):
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

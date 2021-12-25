# A function to make a chessboard
def chessboard(width, height):
    """
    function: Get two positive integers to create a chessboard
    :param width: A positive represents width
    :param height: A positive represents height
    :return: A string about new chessboard
    """
    # Make a new empty chessboard
    make_chessboard = ""
    # Initialize i
    i = 0
    # Use while loop to make the chessboard height
    while i < height:
        # Initialize j
        j = 0
        # Use while loop to make the chessboard width
        while j < width:
            # Print B on the chessboard
            while (i + j) % 2 == 0 and j < width:
                make_chessboard += "B"
                # Iterate j
                j += 1
            # Print W on the chessboard
            while (i + j) % 2 != 0 and j < width:
                make_chessboard += "W"
                # Iterate j
                j += 1
        make_chessboard += "\n"
        # Iterate i
        i += 1
    return make_chessboard


# A function to test the chessboard function
def main():
    """
    function: A function to test the chessboard function
    :return: True or false test results
    """
    # A fail counter
    num_fail = 0

    # Test 1
    print("Testing points:", "(8, 4)",
          "\n""BWBWBWBW\n""WBWBWBWB\nBWBWBWBW\nWBWBWBWB\n")
    print("Expected......", "\n""BWBWBWBW\nWBWBWBWB\nBWBWBWBW\nWBWBWBWB\n")
    print("Actual........\n" + chessboard(8, 4))
    # Compare the function result with expected result
    if "BWBWBWBW\nWBWBWBWB\nBWBWBWBW\nWBWBWBWB\n" == chessboard(8, 4):
        print("PASSED!\n")
    else:
        print("FAILED!\n")
        num_fail += 1

    # Test 2
    print("Testing points:", "(5, 4)", "\n""BWBWB\nWBWBW\nBWBWB\nWBWBW\n")
    print("Expected......", "\n""BWBWB\nWBWBW\nBWBWB\nWBWBW\n")
    print("Actual........\n" + chessboard(5, 4))
    # Compare the function result with expected result
    if "BWBWB\nWBWBW\nBWBWB\nWBWBW\n" == chessboard(5, 4):
        print("PASSED!\n")
    else:
        print("FAILED!\n")
        num_fail += 1

    # Test 3
    print("Testing points:", "(8, 6)",
          "\n""BWBWBWBW\nWBWBWBWB\nBWBWBWBW\nWBWBWBWB\nBWBWBWBW\nWBWBWBWB\n")
    print("Expected......",
          "\n""BWBWBWBW\nWBWBWBWB\nBWBWBWBW\nWBWBWBWB\nBWBWBWBW\nWBWBWBWB\n")
    print("Actual........\n" + chessboard(8, 6))
    # Compare the function result with expected result
    if "BWBWBWBW\nWBWBWBWB\nBWBWBWBW\nWBWBWBWB\nBWBWBWBW\nWBWBWBWB\n" \
            == chessboard(8, 6):
        print("PASSED!\n")
    else:
        print("FAILED!\n")
        num_fail += 1
    # Output the test result
    if num_fail == 0:
        print("All tests passed!")
    else:
        print("Some tests failed!")


if __name__ == "__main__":
    main()

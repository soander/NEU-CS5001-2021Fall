# A function is to translate english to french days
def translate(day_in_english):
    """
    function: A function is to translate english to french days
    :param day_in_english: A day of the week in english
    :return: none
    """
    # Make a dictionary about french days
    day_in_french = {"monday": "lundi", "tuesday": "mardi",
                     "wednesday": "mercredi", "thursday": "jeudi",
                     "friday": "vendredi", "saturday": "samedi",
                     "sunday": "dimanche"}

    # Use the while loop
    while day_in_english.lower() in day_in_french:
        return day_in_french[day_in_english.lower()]
    else:
        return "It's a invalid day"


# A function to test translation function
def main():
    """
    function: A function to test translation function
    :return: none
    """
    # Make a failure counter
    num_fail = 0

    # Test 1
    print("Testing points:", "monday", "lundi")
    print("\tExpected......", "lundi")
    print("\tActual........", translate("monday"))
    if "lundi" == translate("monday"):
        print("PASSED!\n")
    else:
        print("FAILED!\n")
        num_fail += 1

    # Test 2
    print("Testing points:", "Tuesday", "mardi")
    print("\tExpected......", "mardi")
    print("\tActual........", translate("Tuesday"))
    if "mardi" == translate("Tuesday"):
        print("PASSED!\n")
    else:
        print("FAILED!\n")
        num_fail += 1

    # Test 3
    print("Testing points:", "Friday", "vendredi")
    print("\tExpected......", "vendredi")
    print("\tActual........", translate("Friday"))
    if "vendredi" == translate("Friday"):
        print("PASSED!\n")
    else:
        print("FAILED!\n")
        num_fail += 1

    # Test 4
    print("Testing points:", "Happy day", "It's a invalid day")
    print("\tExpected......", "It's a invalid day")
    print("\tActual........", translate("Happy day"))
    if "It's a invalid day" == translate("Happy day"):
        print("PASSED!\n")
    else:
        print("FAILED!\n")
        num_fail += 1
    # The test result
    if num_fail == 0:
        print("All tests passed!")
    else:
        print("Some tests failed!")


if __name__ == "__main__":
    main()

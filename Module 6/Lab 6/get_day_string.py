"""
Code to get day of the week in order string

Author: Yaozheng Wang
CS5001 lab06
lab05 Q1
2021-10-12
"""


# A function return the days of week in order
def get_day_string():
    """
    Function: A function return the days of week in order
    :return: A string contains all the days of the week in order
    """
    # Make a list about weekday
    weekday = ["Sunday", "Monday", "Tuesday", "Wednesday",
               "Thursday", "Friday", "Saturday"]
    # Set the empty days of the week
    days_of_week = " "
    # Use for loop to get days of the week string
    for i in weekday:
        days_of_week += i + " "
    # Use strip() method
    days_of_week = days_of_week.strip()
    return days_of_week


# A function to test the get_day_string function
def main():
    """
    Function: A function to test the get_day_string function
    :return: The test results Ture or False of function
    """
    # Set the days of week in order
    days_in_order = "Sunday Monday Tuesday Wednesday Thursday Friday Saturday"
    # Use while loop to decide the test result
    if days_in_order == get_day_string():
        print("PASSED!")
        return True
    else:
        print("FAILED!")
        return False


if __name__ == "__main__":
    main()

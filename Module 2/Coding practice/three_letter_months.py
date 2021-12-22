def main():
    month = input("Enter month: ")

    # Decision
    if month == "Feb" or month == "2" or month == "February":
        days = 28
    elif month == "Apr" or month == "4" or month == "April":
        days = 30
    elif month == "Jun" or month == "6" or month == "June":
        days = 30
    elif month == "Sep" or month == "9" or month == "September":
        days = 30
    elif month == "Nov" or month == "11" or month == "November":
        days = 30
    elif month == "Jan" or month == "1" or month == "January":
        days = 31
    elif month == "Mar" or month == "3" or month == "March":
        days = 31
    elif month == "May" or month == "5":
        days = 31
    elif month == "Jul" or month == "7" or month == "July":
        days = 31
    elif month == "Aug" or month == "8" or month == "August":
        days = 31
    elif month == "Oct" or month == "10" or month == "October":
        days = 31
    elif month == "Dec" or month == "12" or month == "December":
        days = 31
    else:
        days = "Unknown"

    # Output result
    print(month, "has", days, "days")


if __name__ == '__main__':
    main()

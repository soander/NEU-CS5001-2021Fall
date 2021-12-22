def main():
    # Input length in meters
    length = float(input("Enter length:"))

    # Process the conversion
    inches = length * 39.3701
    feet = inches / 12
    miles = feet / 5280

    # Output results
    print("The length in inches is", inches)
    print("The length in feet is ", feet)
    print("The length in miles is", miles)


if __name__ == '__main__':
    main()

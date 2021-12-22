def main():
    # Input float number
    num = float(input("Enter a floating point number:"))

    numerator = num * 100
    int_numerator = int(numerator)
    str_numerator = str(int_numerator)

    # Output result
    print(num, "is", str_numerator + "/100")


if __name__ == '__main__':
    main()

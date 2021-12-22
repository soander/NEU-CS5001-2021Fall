def main():

    # Input a number
    number = int(input("Enter value:"))

    # Clamping Decision
    if number > 100:
        print("Too big, clamping required\nValue is 100")
    elif number < 1:
        print("Too small, clamping required\nValue is 1")
    else:
        print("Value is", number)


if __name__ == '__main__':
    main()

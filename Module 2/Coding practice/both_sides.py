def main():
    # Input value
    value = int(input("Enter value:"))

    # Decision
    if value % 2 == 0:
        if value >= 0:
            print("even positive number")
        else:
            print("even negative number")
    else:
        if value < 0:
            print("odd negative number")
        else:
            print("odd positive number")


if __name__ == '__main__':
    main()

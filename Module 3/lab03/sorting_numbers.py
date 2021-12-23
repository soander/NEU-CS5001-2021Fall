def main():
    # Input numbers
    first_number = float(input("Input first number: "))
    second_number = float(input("Input second number: "))
    third_number = float(input("Input third number: "))

    # Use function
    sorting(first_number, second_number, third_number)


def sorting(num1, num2, num3):
    """
    function : Sort 3 numbers
    :param num1: A float number
    :param num2: A float number
    :param num3: A float number
    :return: none
    """
    if num1 > num2:
        if num2 > num3:
            print(f"{num3}, {num2}, {num1}")
        elif num2 < num3:
            if num1 > num3:
                print(f"{num2}, {num3}, {num1}")
            elif num1 < num3:
                print(f"{num2}, {num1}, {num3}")
    elif num1 < num2:
        if num1 > num3:
            print(f"{num3}, {num1}, {num2}")
        elif num1 < num3:
            if num2 > num3:
                print(f"{num1}, {num3}, {num2}")
            elif num2 < num3:
                print(f"{num1}, {num2}, {num3}")


if __name__ == '__main__':
    main()

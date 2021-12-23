def number_even(integer):
    """
    function: Decide an integer is a even or odd
    :param integer: An integer is inputted from keyboard
    :return: nothing
    """
    if integer % 2 == 0:
        print(integer, "is even")
    else:
        print(integer, "is odd")


def main():
    # Input a number
    number = int(input("Input number: "))
    number_even(number)


if __name__ == '__main__':
    main()

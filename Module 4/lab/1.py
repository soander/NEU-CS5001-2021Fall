# A function to check a number in Fibonacci sequence
def main ():
    """
    function: A function to check a number in Fibonacci sequence
    :param num: An input number
    :return: Ture or False
    """
    num = int(input("Enter a number"))

    if num == 0 or num == 1:
        print("True")
    # Make a Fibonacci sequence
    a = 0
    b = 1
    while num > b:
        c = b + a
        a = b
        b = c
    a = b == num
    print(a)


if __name__ == '__main__':
    main()

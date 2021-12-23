def main():
    # Input the first value
    first_value = input("Input first number: ")
    # Input the second value
    second_value = input("Input second number: ")

    # Input the operator
    opera = input("Input operator (+,-,*,/): ")

    if opera == "+":
        add(first_value, second_value)
    elif opera == "-":
        sub(first_value, second_value)
    elif opera == "*":
        mul(first_value, second_value)
    elif opera == "/":
        div(first_value, second_value)
    else:
        print("Invalid operator. Please use +,-,*,/. ")


def add(first_value, second_value):
    """
    function: Use input floats and operators to add
    :param first_value: A float
    :param second_value: A float
    :return: none
    """
    result = float(first_value) + float(second_value)
    print(first_value, "+", second_value, "=", result)


def sub(first_value, second_value):
    """
    function: Use input floats and operators to do subtraction
    :param first_value: A float
    :param second_value: A float
    :return: none
    """
    result = float(first_value) - float(second_value)
    print(first_value, "-", second_value, "=", result)


def mul(first_value, second_value):
    """
    function: Use input floats and operators to multiply
    :param first_value: A float
    :param second_value: A float
    :return: none
    """
    result = float(first_value) * float(second_value)
    print(first_value, "*", second_value, "=", result)


def div(first_value, second_value):
    """
    function: Use input floats and operators to do division
    :param first_value: A float
    :param second_value: A float
    :return: none
    """
    if float(second_value) == 0.0:
        print(first_value, "/", second_value, "= NaN")
    else:
        result = float(first_value) / float(second_value)
        print(first_value, "/", second_value, "=", result)


if __name__ == '__main__':
    main()

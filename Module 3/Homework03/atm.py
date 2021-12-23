def dispense_the_money(money):
    """
    function : It will dispense the money that customer input
    :param money: It's a float number
    :return: the dispense result of money
    """

    # Make lists about denominations and money words
    denominations = [5000, 2000, 1000, 500, 200, 100, 25, 10, 5]
    words = ["fifties", "fifty", "twenties", "twenty", "tens", "ten",
             "fives", "five", "toonies", "toony", "lonnies", "loony",
             "quarters", "quarter", "dimes", "dime", "nickles", "nickle"]

    # Convert money value to integer value
    money_integer = int(money * 100)
    # Create the change money value
    change_money = ""

    # A for loop decide the dispense
    for i in range(len(denominations)):
        if money_integer // denominations[i] != 0:
            if money_integer // denominations[i] > 1:
                change_money += str(money_integer // denominations[i]) \
                                + " " + words[i * 2] + "\n"
            else:
                change_money += str(money_integer // denominations[i]) \
                                + " " + words[i * 2 + 1] + "\n"
        money_integer = money_integer % denominations[i]

    # Use if to decide the nickle
    if 3 <= money_integer <= 4:
        change_money += "1 nickle\n"
    # Return the change_money result
    return change_money


def main():
    """
    Function: A function to use dispense_the_money
    function to dispense the money,
    and to do every designed test in atm_tests.txt.
    :return: The dispense result and tests' result.
    """
    # Get customers' input
    value = float(input("Input request: "))
    # Use dispense_the_money function
    print(dispense_the_money(value), end="")


if __name__ == "__main__":
    main()

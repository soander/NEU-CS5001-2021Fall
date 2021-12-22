def main():
    roman_numerals = {1: 'I', 5: 'V', 10: 'X',
                      50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    descending_order = [1000, 500, 100, 50, 10, 5, 1]

    # Input number
    num = int(input("Enter number:"))
    result = ""
    n = num

    if 1 <= n <= 4999:
        for x in descending_order:
            order = n // x

            if order != 0:
                result = result + order * roman_numerals[x]

            n = n % x

    print(num, "is", result)


if __name__ == '__main__':
    main()

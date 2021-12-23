def main():
    # Make a word list
    word_list = ["one", "two", "three", "four", "five"]

    # Input value and word
    value = int(input("Enter integer value:"))
    word = input("Enter word:")

    # Compare the result
    if word_list[value-1] == word:
        print(value, "and", word, "are the same number.")
    else:
        print(value, "and", word, "are NOT the same number.")


if __name__ == '__main__':
    main()

def main():
    i = 0
    while i < 100:
        print(i)
        i = i + 1
    for i in range(100):
        print(i)
    for i in range(-100, 0):
        print(i)
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    for i in data:
        print(i)
    text = "Welcome to the CS5001!"
    text_split = text.split()
    print(text_split)
    for i in text_split:
        print(i[0])


if __name__ == "__main__":
    main()

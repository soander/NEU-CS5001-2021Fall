def main():
    # Input numbers
    num_1 = int(input())
    num_2 = int(input())
    num_3 = int(input())
    num_4 = int(input())

    # Matching numbers
    if num_1 == num_2 and num_3 == num_4:
        print("two pairs")
    elif num_1 == num_3 and num_2 == num_4:
        print("two pairs")
    elif num_1 == num_4 and num_2 == num_3:
        print("two pairs")
    else:
        print("not two pairs")


if __name__ == '__main__':
    main()

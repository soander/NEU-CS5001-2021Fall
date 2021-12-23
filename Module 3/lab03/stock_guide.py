def main():
    # Input the rating
    rating = int(input("Input rating: "))
    rating_system(rating)


def rating_system(rank):
    """
    function : A rating system decide to invest stocks
    :param rank: The new stock rating
    :return: none
    """
    if rank > 100:
        print("Buy a lot")
    elif 100 >= rank > 76:
        print("Buy a little")
    elif 76 >= rank >= 50:
        print("Stay")
    elif 50 > rank > 25:
        print("Sell")
    else:
        print("Sell! Sell! Sell!")


if __name__ == '__main__':
    main()

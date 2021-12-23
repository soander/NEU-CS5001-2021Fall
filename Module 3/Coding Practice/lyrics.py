"""
print the lyrics for five
different animals (five verses)

Author: Yaozheng Wang
CS5001 Coding Practice
Module 3
question 10 Lyrics
2021-11-5
"""


# print the lyrics for five different animals (five verses)
def animal():
    """
    Function: print the lyrics for five different animals
        (five verses)
    :return: the lyrics with five different animals
    """
    # Set the five animals list
    animals = ["cow", "chicken", "pig", "horse", "goat"]
    voices = {"cow": "moo", "chicken": "kiki", "pig": "henhen",
              "horse": "yiyi", "goat": "meme"}
    # Use for loop to print the lyrics
    for times in range(5):
        print("Old MacDonald had a farm, ee-igh, ee-igh, oh!")
        print("And on that farm he had a " + animals[times], end="")
        print(", ee-igh, ee-igh, oh!")
        print("With a " + voices[animals[times]] + ", ", end="")
        print(voices[animals[times]], end="")
        print(" here and a " + voices[animals[times]] + ", ", end="")
        print(voices[animals[times]] + " there.")
        print("Here a " + voices[animals[times]], end="")
        print(", there a " + voices[animals[times]] + ", ", end="")
        print("everywhere a " + voices[animals[times]], end="")
        print(", " + voices[animals[times]] + ".")
        print("Old MacDonald had a farm, ee-igh, ee-igh, oh!\n")


def main():
    animal()


if __name__ == "__main__":
    main()

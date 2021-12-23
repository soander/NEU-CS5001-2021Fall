"""
receives a score and returns
the letter grade for that score.

Author: Yaozheng Wang
CS5001 Coding Practice
Module 3
question 7 Area of Triangle
2021-11-5
"""


# receives a score and returns
# the letter grade for that score.
def grade(score):
    """
    Function: receives a score and returns
        the letter grade for that score.
    :param score: The student score
    :return: the letter grade
    """
    # Use if decide the letter grade
    if 93.00 <= score <= 100.00:
        return "A"
    if 90.00 <= score <= 92.99:
        return "A-"
    if 86.00 <= score <= 89.99:
        return "B+"
    if 82.00 <= score <= 85.99:
        return "B"
    if 77.00 <= score <= 81.99:
        return "B-"
    if 73.00 <= score <= 76.99:
        return "C+"
    if 69.00 <= score <= 72.99:
        return "C"
    if 65.00 <= score <= 68.99:
        return "C-"
    if 0.00 <= score <= 64.99:
        return "F"


def main():
    print(grade(96))
    print(grade(92))
    print(grade(88))
    print(grade(83))
    print(grade(78))
    print(grade(74))
    print(grade(70))
    print(grade(66))
    print(grade(50))


if __name__ == "__main__":
    main()

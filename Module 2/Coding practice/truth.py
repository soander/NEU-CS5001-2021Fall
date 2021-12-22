def main():
    print("+---+---+---+---+---+")
    print("| p | q | r | A | B |")
    print("+---+---+---+---+---+")

    p1 = 0
    q1 = 0
    r1 = 0
    a1 = int((p1 and q1) or not r1)
    b1 = int(not (p1 and (q1 or not r1)))

    if a1 == 1:
        a1_1 = "T"
    else:
        a1_1 = "F"
    if b1 == 1:
        b1_1 = "T"
    else:
        b1_1 = "F"

    print("| F | F | F | " + a1_1 + " | " + b1_1 + " |")
    print("+---+---+---+---+---+")

    p2 = 0
    q2 = 0
    r2 = 1
    a2 = int((p2 and q2) or not r2)
    b2 = int(not (p2 and (q2 or not r2)))

    if a2 == 1:
        a2_2 = "T"
    else:
        a2_2 = "F"
    if b2 == 1:
        b2_2 = "T"
    else:
        b2_2 = "F"

    print("| F | F | T | " + a2_2 + " | " + b2_2 + " |")
    print("+---+---+---+---+---+")

    p3 = 0
    q3 = 1
    r3 = 0
    a3 = int((p3 and q3) or not r3)
    b3 = int(not (p3 and (q3 or not r3)))

    if a3 == 1:
        a3_3 = "T"
    else:
        a3_3 = "F"
    if b3 == 1:
        b3_3 = "T"
    else:
        b3_3 = "F"

    print("| F | T | F | " + a3_3 + " | " + b3_3 + " |")
    print("+---+---+---+---+---+")

    p4 = 0
    q4 = 1
    r4 = 1
    a4 = int((p4 and q4) or not r4)
    b4 = int(not (p4 and (q4 or not r4)))

    if a4 == 1:
        a4_4 = "T"
    else:
        a4_4 = "F"
    if b4 == 1:
        b4_4 = "T"
    else:
        b4_4 = "F"

    print("| F | T | T | " + a4_4 + " | " + b4_4 + " |")
    print("+---+---+---+---+---+")

    p5 = 1
    q5 = 0
    r5 = 0
    a5 = int((p5 and q5) or not r5)
    b5 = int(not (p5 and (q5 or not r5)))

    if a5 == 1:
        a5_5 = "T"
    else:
        a5_5 = "F"
    if b5 == 1:
        b5_5 = "T"
    else:
        b5_5 = "F"

    print("| T | F | F | " + a5_5 + " | " + b5_5 + " |")
    print("+---+---+---+---+---+")

    p6 = 1
    q6 = 0
    r6 = 1
    a6 = int((p6 and q6) or not r6)
    b6 = int(not (p6 and (q6 or not r6)))

    if a6 == 1:
        a6_6 = "T"
    else:
        a6_6 = "F"
    if b6 == 1:
        b6_6 = "T"
    else:
        b6_6 = "F"

    print("| T | F | T | " + a6_6 + " | " + b6_6 + " |")
    print("+---+---+---+---+---+")

    p7 = 1
    q7 = 1
    r7 = 0
    a7 = int((p7 and q7) or not r7)
    b7 = int(not (p7 and (q7 or not r7)))

    if a7 == 1:
        a7_7 = "T"
    else:
        a7_7 = "F"
    if b7 == 1:
        b7_7 = "T"
    else:
        b7_7 = "F"

    print("| T | T | F | " + a7_7 + " | " + b7_7 + " |")
    print("+---+---+---+---+---+")

    p8 = 1
    q8 = 1
    r8 = 1
    a8 = int((p8 and q8) or not r8)
    b8 = int(not (p8 and (q8 or not r8)))

    if a8 == 1:
        a8_8 = "T"
    else:
        a8_8 = "F"
    if b8 == 1:
        b8_8 = "T"
    else:
        b8_8 = "F"

    print("| T | T | T | " + a8_8 + " | " + b8_8 + " |")
    print("+---+---+---+---+---+")


if __name__ == '__main__':
    main()

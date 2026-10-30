son1 = float(input("1-sonni kiriting: "))
son2 = float(input("2-sonni kiriting: "))
son3 = float(input("3-sonni kiriting: "))


def eng_kattasini_top(son1, son2, son3):
    katta = son1
    if son2 > katta:
        katta = son2
    if son3 > katta:
        katta = son3
    print("Eng katta son:", katta)


eng_kattasini_top(son1, son2, son3)
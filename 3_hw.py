def nomer2(a, b):
    if a > b:
        print (a)
    elif b > a:
        print (b)
    else:
        print("Числа равны")

nomer2(10, 12)


def nomer3(a, b):
    if abs(a - b) == 135:
        print("yes")
    else:
        print("no")

nomer3(10, 10+135)


def nomer4(a):
    if 2 < a < 6:
        print("Vesna")
    elif 5 < a < 9:
        print("Leto")
    elif 8 <a < 12:
        print("Osen")
    elif 3 > a or 12:
        print("Zima")
    else:
        print("there is no such month")

nomer4(12)


def nomer5(a, b, c):
    if a>10 and b>10 and c>10:
        print("yes")
    else:
        print("no")

nomer5(83, 12, 53)
# coding=utf-8


def primeOrNot(n):
    if n == 1:
        return False
    for j in range(2, n + 1):
        check = False
        for i in range(2, int(j ** 0.5 + 1)):
            if j % i == 0:
                check = True
                break
        if not check:
            print (j, "is a prime number")


def primeOrNotInfinity():
    j = 3
    while True:
        check = False
        for i in range(2, int(j ** 0.5 + 1)):
            if j % i == 0:
                check = True
                break
        if not check:
            print (j, "is a prime number")
        j += 1


if __name__ == '__main__':
    print("Please input a number:")
    s = str(input())
    if not s:
        primeOrNotInfinity()
    else:
        n = int(s)
        primeOrNot(n)

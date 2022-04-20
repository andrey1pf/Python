# coding=utf-8

def binarization(n, a, b):
    a = a * 10 + n % 2
    b = n / 2
    if b != 1:
        return binarization(b, a, b)
    if b == 1:
        a = a * 10 + 1
        return a


def coup(n, a):
    a = a * 10 + n % 10
    if n / 10 != 0:
        coup(n / 10, a)
    if n / 10 == 0:
        print a


if __name__ == '__main__':
    print("Enter a number: ")
    n = int(input())
    k = binarization(n, 0, 0)
    coup(k, 0)

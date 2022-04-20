# coding=utf-8


def generator(n):
    for i in range(1, n + 1):
        if (i % 2):
            print(i, "is odd")
        else:
            print(i, "is even")


def generatorInfinity():
    i = 1
    while True:
        if (i % 2):
            print(i, "is odd")
        else:
            print(i, "is even")
        i += 1


if __name__ == '__main__':
    print('Enter N:')
    s = str(input())
    if not s:
        generatorInfinity()
    else:
        n = int(s)
        generator(n)

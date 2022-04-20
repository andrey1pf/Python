# coding=utf-8


def generator(n, func):
    q = 0;
    if(func == 1):
        for i in range(1, n + 1):
            print("The factorial of", i, "is", factorial(i))
    elif(func == 0):
        while True:
            print("The factorial of", q, "is", factorial(q))
            q += 1


def factorial(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == '__main__':
    print("Enter a number: ")
    s = str(input())
    if not s:
        generator(0, 0)
    else:
        n = int(s)
        generator(n, 1)

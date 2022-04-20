# coding=utf-8


def generator(n, check):
    if check == 1:
        for i in range(11, n + 1):
            count = 0
            number = i
            while i != 0:
                i /= 10
                count += 1
            if palindrom(number, count):
                print(number)
    else:
        i = 11
        while True:
            count = 0
            number = i
            while number != 0:
                number /= 10
                count += 1
            if palindrom(i, count):
                print(i)
            i += 1


def palindrom(n, count):
    if (n % 10) == (n / (10 ** (count - 1))) and count > 1:
        n = (n - (n / 10 ** (count - 1)) * (10 ** (count - 1))) / 10
        count -= 2
        return palindrom(n, count)
    if count == 1 or count == 0:
        return True
    return False

if __name__ == '__main__':
    print("Enter your number:")
    s = str(input())
    if not s:
        generator(0, 0)
    else:
        generator(int(s), 1)

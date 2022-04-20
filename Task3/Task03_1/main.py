# coding=utf-8

def binaryToDecimalConversion(binary):
    decimal = 0
    power = 0
    powerD = -1
    point = 0
    for i in range(len(binary)):
        if binary[i] == '.':
            point = i

    for i in binary[point - 1::-1]:
        decimal += int(i) * (2 ** power)
        power += 1

    for i in binary[point + 1::]:
        decimal += int(i) * (2 ** powerD)
        powerD -= 1
    return decimal


def decimalToBinaryConversion(decimal):
    ost = decimal % 1
    stringost = ''
    decimal = (int)(decimal - ost)
    binary = ''
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2

    while ost != 0:
        stringost += str(int(ost * 2))
        ost = ost * 2 - int(ost * 2)

    return binary + '.' + stringost


if __name__ == '__main__':
    print("Превод из двоичной в десятичную систему")
    binN = input()
    print(binaryToDecimalConversion(binN))
    print("Превод из десятичной в двоичную систему")
    n = float(input())
    print(decimalToBinaryConversion(n))


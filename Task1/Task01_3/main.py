



if __name__ == '__main__':
    number = (float)(input("Enter a number: "))
    numberZ = (int)(number)
    numberF = number - numberZ
    a = len(str(numberF)) - 2
    numberF *= (int)((10 ** a))
    count = 0

    while numberF > 0:
        a = numberF % 10
        count += a
        numberF -= a
        numberF /= 10
    while numberZ > 0:
        a = numberZ % 10
        count += a
        numberZ -= a
        numberZ /= 10

    print((int)(count))








# coding=utf-8



if __name__ == '__main__':
    a = (int)(input("Первое число: "))
    b = (int)(input("Второе число: "))
    check = False

    if a > b:
        for i in range(2, b + 1):
            if a % i == 0 and b % i == 0:
                print (str(a) + " и " + str(b) + " невзаимно простые")
                check = True
                break
        if check == False:
            print (str(a) + " и " + str(b) + " взаимно простые")
    else:
        for i in range(2, a + 1):
            if a % i == 0 and b % i == 0:
                print (str(a) + " и " + str(b) + " невзаимно простые")
                check = True
                break
        if check == False:
            print (str(a) + " и " + str(b) + " взаимно простые")
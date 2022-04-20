



if __name__ == '__main__':
    line = str(input())
    countZero = 0;
    countOne = 0;
    if len(line) == 0:
        print(0)
    else:
        for x in line:
            if x == '0':
                countZero += 1
            else:
                countOne += 1
        if countZero > countOne:
            print(countOne)
        else:
            print(countOne)



def coupLine(line):
    n = len(line)
    if n == 0:
        return False
    else:
        newLine = line[::-1]
        print(newLine, end="")


def readLine(line):
    j = 0
    check = False
    for i in range(0, len(line)):
        element = line[i]
        if element == ' ' or element == '\n' or element == ',' or element == '.' \
                or element == '!' or element == '?' or i == len(line) - 1:
            if i == len(line) - 1:
                newLine = line[j:i+1]
                coupLine(newLine)
                check = True
            else:
                newLine = line[j:i]
                coupLine(newLine)
                print(element, end="")
                check = True
                i += 1
        if check:
            j = i
            check = False


if __name__ == '__main__':
    print("Enter a line of text: ")
    line = str(input())
    readLine(line)


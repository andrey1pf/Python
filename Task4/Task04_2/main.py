

def frequencyOfOccurrence():
    resultline = ''
    resultword = ''
    check = False
    b = 0

    for line in f:
        resultline += line.casefold()
    linearray = resultline.split()
    for i in range(len(linearray)):
        count = 0
        n = len(linearray)
        j = i + 1

        while j < n:
            if linearray[i] == linearray[j]:
                count += 1
                linearray.pop(j)
                n -= 1
            else:
                j += 1

        if count > b:
            b = count
            resultword = linearray[i]
            check = False
        elif count == b:
            resultword += ', ' + linearray[i]
            check = True

    if b == 0:
        print('There is no word that occurs more than once.')
    elif check:
        print('The words that occurs most often are:', resultword)
    else:
        print('The word that occurs most often is:', resultword)


if __name__ == '__main__':
    f = open('input.txt', 'r')
    frequencyOfOccurrence()
    f.close()

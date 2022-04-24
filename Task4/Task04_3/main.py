

def searchForTheSameWordsInTheTwoFiles():
    resultLineOne = ''
    resultLineTwo = ''
    resultArray = []

    for line in fone:
        resultLineOne += line.casefold()

    for line in ftwo:
        resultLineTwo += line.casefold()

    lineOneArray = resultLineOne.split()
    lineTwoArray = resultLineTwo.split()
    for word in lineOneArray:
        for wordTwo in lineTwoArray:
            if word == wordTwo:
                resultArray.append(word)

    print(set(resultArray))


if __name__ == '__main__':
    fone = open('inputone.txt', 'r')
    ftwo = open('inputtwo.txt', 'r')

    searchForTheSameWordsInTheTwoFiles()

    fone.close()
    ftwo.close()
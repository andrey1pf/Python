



if __name__ == '__main__':
    number = int(input("Enter a number: "))
    sum = 0
    for i in range(2, number + 1):
        count = 0
        if number % i == 0:
            for j in range(2, i):
                if i % j == 0:
                    count += 1
                    break
            if count == 0:
                sum += i
    if(sum != 0):
        print("The sum of all the prime numbers below", number, "is", sum)
    else:
        print("There are no prime numbers below", number)

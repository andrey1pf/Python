
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    letter = str(input("Enter letter you are looking for\n"))
    line = str(input("Enter the string you are looking for\n"))
    if letter in line:
        print("found")
        #print("Буква" + letter + "встречается в строке" + string + " ")
    else:
        print("not found")
        #print("Буква" + letter + "не встречается в строке" + string + " ")


# -*- coding: utf-8 -*-


if __name__ == '__main__':
    letter = str(input("Enter letter you are looking for\n"))
    line = str(input("Enter the string you are looking for\n"))
    if letter in line:
        print("Буква " + letter + " встречается в строке " + line)
    else:
        print("Буква " + letter + " не встречается в строке " + line)

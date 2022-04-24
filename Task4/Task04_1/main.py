# coding=utf-8

def EncodingAndDecoding(string, morze, code):
    if code == 'encode':
        result = ''
        a = ' '
        for i in string:
            if i == ' ' and a == ' ':
                result += '   '
            elif i == ' ' and a != ' ':
                result += '  '
            else:
                result += morze[i] + ' '
            a = i

    else:
        result = ''
        word = ''
        i = 0
        while i < len(string):
            if string[i:i+3] == '   ':
                result += ' '
                i += 3
                continue
            if string[i] != ' ':
                word += string[i]
            if string[i+1:i+2] == ' ' or i == len(string)-1:
                for key, value in morze.items():
                    if value == word:
                        result += key
                        word = ''
                        break
            i += 1
    return result


if __name__ == '__main__':
    morze = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..',
             'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-',
             'r': '.-.','s': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--','z': '--..',
             '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
             '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
             }
    f = open('input.txt', '+r')
    encf = open('cod.input.txt', '+r')

    n = open('input2.txt', '+r')
    decf = open('cod.input2.txt', '+r')

    stringEncode = ''
    stringDecode = ''

    for stringEncode in f:
        line = stringEncode.strip()
        encf.write(EncodingAndDecoding(line, morze, 'encode') + '\n')

    for stringDecode in decf:
        line = stringDecode.strip()
        n.write(EncodingAndDecoding(line, morze, 'decode') + '\n')

    f.close()
    encf.close()
    n.close()
    decf.close()

def HackerEncode(plainText):
    leetCode = {
        'a': '4',
        'b': 'I3',
        'c': '[',
        'd': ')',
        'e': '3',
        'f': '|=',
        'g': '&',
        'h': '#',
        'i': '1',
        'j': ',_|',
        'k': '>|',
        'l': '1',
        'm': '/\\/\\',
        'n': '^/',
        'o': '0',
        'p': '|*',
        'q': '(_,)',
        'r': 'I2',
        's': '5',
        't': '7',
        'u': '(_)',
        'v': '\\/',
        'w': '\\/\\/',
        'x': '><',
        'y': 'j',
        'z': '2',
        '0': 'o',
        '1': 'L',
        '2': 'R',
        '3': 'E',
        '4': 'A',
        '5': 'S',
        '6': 'b',
        '7': 'T',
        '8': 'B',
        '9': 'g'
    }

    encryptedText = ""

    for letter in plainText:
        if letter in leetCode.keys():
            encryptedText += leetCode[letter]
        else:
            encryptedText += letter

    return encryptedText


print(HackerEncode("leet"))
print(HackerEncode("Mi nombre es Miguelex"))
print(HackerEncode("1234567890"))
print(HackerEncode("Hola Mundo!! Esto es una_prueba con caracteres extrañ@s"))

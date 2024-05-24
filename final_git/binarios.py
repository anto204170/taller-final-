def caracter_binario(char):
    byte_representation = format(ord(char), '08b')
    return byte_representation

def palabra_binario(word):
    byte_representation = ' '.join(format(ord(char), '08b') for char in word)
    return byte_representation

def binario_palabra(byte):
    ascii_representation = chr(int(byte, 2))
    return ascii_representation
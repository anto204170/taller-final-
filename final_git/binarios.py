def char_to_byte(char):
    byte_representation = format(ord(char), '08b')
    return byte_representation

def word_to_byte(word):
    byte_representation = ' '.join(format(ord(char), '08b') for char in word)
    return byte_representation

def byte_to_ascii(byte):
    ascii_representation = chr(int(byte, 2))
    return ascii_representation
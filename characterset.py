_charset = (None, None, 
' ', '!', '"', '£', '$', '%', '&', "'", '(', ')',
'*', '+', ',', '-', '.', '/', '0', '1', '2', '3',
'4', '5', '6', '7', '8', '9', ':', ';', '<', '=',
'>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '←',
'½', '→', '↑', '#', '-', 'a', 'b', 'c', 'd', 'e',
'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
'z', '¼', '|', '¾', '÷', '■', None, None)

def encode_char(char):
    try:
        return _charset.find(char)
    except ValueError:
        return 0

def decode_char(b):
    b = b % 128
    return _charset(b)

def encode(string):
    encoded = []
    for char in string:
        encoded += [encode_char(char)]
    return bytes(encoded)

def decode(bytestr):
    decoded = ""
    for b in bytestr:
        decoded += decode_char(b)
    

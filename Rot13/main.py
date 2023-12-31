# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in
# the alphabet. ROT13 is an example of the Caesar cipher.
# Create a function that takes a string and returns the string ciphered with Rot13.
# If there are numbers or special characters included in the string,
# they should be returned as they are. Only letters from the latin/english alphabet
# should be shifted, like in the original Rot13 "implementation".


import string


def make_rot_n():
    lc = string.ascii_lowercase
    uc = string.ascii_uppercase
    trans = str.maketrans(lc + uc,
                          lc[13:] + lc[:13] + uc[13:] + uc[:13])
    return lambda s: str.translate(s, trans)


rot13 = make_rot_n()

print(rot13('test'))
print(rot13('Test'))
print(rot13('aA bB zZ 1234 *!?%'))

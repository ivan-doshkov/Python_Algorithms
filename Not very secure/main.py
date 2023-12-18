# In this example you have to validate if a user input string is alphanumeric. The given string is not nil/null/NULL/
# None, so you don't have to check that.
# The string has the following conditions to be alphanumeric:
# At least one character ("" is not valid)
# Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
# No whitespaces / underscore


def alphanumeric(password):
    passw = 0
    if password == '':
        return False
    else:
        for char in password:
            alpha = char.isalpha()
            num = char.isnumeric()
            if not alpha and not num or char == " ":
                passw += -1
            else:
                passw += 1
        if len(password) > passw:
            return False
        elif len(password) == passw:
            return True


print(alphanumeric("hello world_"))
print(alphanumeric("PassW0rd"))
print(alphanumeric("     "))

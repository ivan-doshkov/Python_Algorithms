# Write a function named first_non_repeating_letter that takes a string input, and returns the first character that is
# not repeated anywhere in the string.
# For example, if given the input 'stress', the function should return 't', since the letter t only occurs once
# in the string, and occurs first in the string.
# If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.


def first_non_repeating_letter(s):
    countchar = 0
    s = s.lower()
    for char in s:
        countchar = s.count(char)
        if countchar == 1:
            return char

    return ""


print(first_non_repeating_letter("llle"))
print(first_non_repeating_letter("lll"))
print(first_non_repeating_letter("llsl"))
print(first_non_repeating_letter('abba'))
print(first_non_repeating_letter('aa'))
print(first_non_repeating_letter('hello'))

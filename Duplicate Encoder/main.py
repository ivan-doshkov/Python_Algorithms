# The goal of this exercise is to convert a string to a new string where each character in the new string is
# "(" if that character appears only once in the original string, or ")"
# if that character appears more than once in the original string.
# Ignore capitalization when determining if a character is a duplicate.

def duplicate_encode(word):
    word = word.lower()
    newstr = ""
    for char in word:
        charcounter = word.count(char)
        if char == " ":
            newstr += "("
        else:
            if charcounter >= 2:
                newstr += ")"
            else:
                newstr += "("
    return newstr


print(duplicate_encode("(( @"))
print(duplicate_encode("hello"))
print(duplicate_encode("hey man"))
print(duplicate_encode("bin"))

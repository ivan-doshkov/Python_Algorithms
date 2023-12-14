# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that
# occur more than once in the input string. The input string can be assumed to contain only alphabets
# (both uppercase and lowercase) and numeric digits.

def duplicate_count(text):
    text = text.lower()
    charcount = 0
    charduplicated = 0
    charpass = ""
    for char in text:
        if char in charpass:
            continue
        else:
            charpass += char
            charcount = text.count(char)
            if charcount > 1:
                charduplicated += 1
    if charduplicated > 0:
        return charduplicated
    else:
        return 0


print(duplicate_count("abcde"))
print(duplicate_count("aabbcde"))
print(duplicate_count("aabBcde"))
print(duplicate_count("indivisibility"))
print(duplicate_count("Indivisibilities"))
print(duplicate_count("aA11"))
print(duplicate_count("ABBA"))

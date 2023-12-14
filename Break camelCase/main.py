# Complete the solution so that the function will break up camel casing, using a space between words.


def solution(s):
    result = ""
    for c in s:
        if c.isupper():
            result += " " + c
        else:
            result += c

    return result


print(solution("camelCasing"))
print(solution("identifier"))
print(solution(""))

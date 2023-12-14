# You are given an array(list) strarr of strings and an integer k.
# Your task is to return the first longest string consisting of k consecutive strings taken in the array.
# n being the length of the string array, if n = 0 or k > n or k <= 0 return ""
# (return Nothing in Elm, "nothing" in Erlang).


def longest_consec(strarr, k):
    result = ""

    if 0 < k <= len(strarr):
        for index in range(len(strarr) - k + 1):
            s = ''.join(strarr[index:index + k])
            if len(s) > len(result):
                result = s

    return result


print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))
print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1))
print(longest_consec([], 3), "")
print(longest_consec(["itvayloxrp", "wkppqsztdkmvcuwvereiupccauycnjutlv", "vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2))
print(longest_consec(["wlwsasphmxx", "owiaxujylentrklctozmymu", "wpgozvxxiu"], 2))
print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2))
print(longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 3))
print(longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 15))
print(longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 0))

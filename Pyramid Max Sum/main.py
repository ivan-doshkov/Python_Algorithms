# Let's find the maximum sum of consecutive numbers from the top to the bottom of the pyramid.
# As you can see, the longest is
# /3/
# \7\,4
# 2,4,/6/
# 8,5\9\,3


def longest_slide_down(pyramid):
    sum = 0
    maxnum = 0
    for arr in pyramid:
        if len(arr) == 1:
            sum += arr[0]
        if len(arr) > 1:
            maxnum = max(arr)
            sum += maxnum
    return sum


print(longest_slide_down([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]))

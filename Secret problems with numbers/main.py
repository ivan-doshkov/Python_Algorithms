# The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in
# an array or list of integers:
# Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array.
# If the list is made up of only negative numbers, return 0 instead.
# Empty list is considered to have zero greatest sum.
# Note that the empty list or array is also a valid sublist/subarray.

def max_sequence(arr):
    negative = 0
    positive = 0

    for num in arr:
        if num >= 0:
            positive += num
        else:
            negative += num
    if positive == 0 or len(arr) < 0:
        return 0
    else:
        return negative + positive


print(max_sequence([-2, -1, -3, -4, -1, -2, -1, -5, -4]))
print(max_sequence([0]))
print(max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]))
print(max_sequence([]))
print(max_sequence([-5, -6, -9, -87, 20, 12, 11]))

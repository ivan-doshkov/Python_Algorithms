# Your task is to construct a building which will be a pile of n cubes. The cube at the bottom will have a volume of
# n**3 next will be (n-1)**3 and so on until the top which will have a volume of 1**3


def find_nb(m):
    n = 1
    volume = 0
    while volume < m:
        volume += n ** 3
        if volume == m:
            return n
        n += 1
    return -1


print(find_nb(4), -1)
print(find_nb(16), -1)
print(find_nb(4183059834009), 2022)
print(find_nb(24723578342962), -1)
print(find_nb(135440716410000), 4824)
print(find_nb(40539911473216), 3568)
print(find_nb(26825883955641), 3218)

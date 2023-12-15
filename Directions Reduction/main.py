# Once upon a time, on a way through the old wild mountainous west,…
# … a man was given directions to go from one point to another.
# The directions were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too.
# Going to one direction and coming back the opposite direction right away is a needless effort.
# Since this is the wild west, with dreadful weather and not much water, it's important to save yourself some energy,
# otherwise you might die of thirst!
# How I crossed a mountainous desert the smart way.
# The directions given to the man are, for example, the following (depending on the language):


def dir_reduc(arr):
    countNorth = 0
    countSouth = 0
    countEast = 0
    countWest = 0
    newarr = []
    if len(arr) == 0:
        return []
    for dir in arr:
        if dir == "NORTH":
            countNorth += 1
        elif dir == "SOUTH":
            countSouth += 1
        elif dir == "EAST":
            countEast += 1
        elif dir == "WEST":
            countWest += 1
        if countNorth == 1 and countEast == 1 and countSouth == 1 and countWest == 1:
            return arr
    if countNorth > countSouth:
        newarr.append("NORTH")
    elif countSouth > countNorth:
        newarr.append("SOUTH")
    if countEast > countWest:
        newarr.append("EAST")
    elif countWest > countEast:
        newarr.append("WEST")

    return newarr


print(dir_reduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
print(dir_reduc(["NORTH", "WEST", "SOUTH", "EAST"]))
print(dir_reduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
print(dir_reduc(["NORTH", "SOUTH", "EAST", "WEST", "NORTH", "NORTH", "SOUTH", "NORTH", "WEST", "EAST"]))
print(dir_reduc([]))
print(dir_reduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH"]))

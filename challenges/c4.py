# Don't add any more statements, just change existing ones
# Builds towers like this:
# n_floors = 6:
# [
#  "     *     ",
#  "    ***    ",
#  "   *****   ",
#  "  *******  ",
#  " ********* ",
#  "***********"
# ]
def tower_builder(n_floors):
    if n_floors == 0:
        return []

    result = []

    for i in range(1, n_floors):
        stars = "*" * (2 * (i - 1))
        space = " " * (n_floors - i)
        result.append(space + stars + space)
    return result

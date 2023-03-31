def tower_builder(n_floors):
    if n_floors == 0:
        return []

    result = []

    for i in range(1, n_floors + 1):
        stars = "*" * (2 * i - 1)
        space = " " * (n_floors - i)
        result.append(space + stars + space)
    return result

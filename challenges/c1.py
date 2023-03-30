count = 0


def increment_counter():
    global count
    count += 1


def reset_counter():
    count = 0


increment_counter()
increment_counter()
reset_counter()
increment_counter()


def c1():
    return count

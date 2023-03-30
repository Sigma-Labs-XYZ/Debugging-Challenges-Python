count = 0


def increment_counter():
    global count
    count += 1


def reset_counter():
    global count
    count = 0


increment_counter()
increment_counter()
reset_counter()
increment_counter()


def c1():
    # Should equal 1
    return count

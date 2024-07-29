import copy
import random


def change():
    door = random.randint(1, 3)
    choice = random.randint(1, 3)

    doors = [1, 2, 3]

    doors_ = copy.copy(doors)
    if choice == door:
        doors_.remove(choice)
        open_door = random.choice(doors_)
        # doors.remove(open_door)
    else:
        doors_.remove(choice)
        doors_.remove(door)
        open_door = doors_[0]

    doors.remove(choice)
    doors.remove(open_door)
    # choice = doors[0]
    if choice == door:
        return True

    return False


n = 1000
results = [change() for _ in range(n)]
print(sum(results) / n)

"""
1 2 3
"""

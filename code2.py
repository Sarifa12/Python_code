
import math
def print_pattern(number: int):
    half = math.ceil(number / 2)
    hor_pattern = ""
    for i in range(number):
        hor_pattern += "#"

    middle_space = number - 4
    space = 0
    for i in range(1, number + 1):
        # print(middle_space)
        if i == 1 or i == number:
            print(hor_pattern, end="\n")
        elif i < half:
            print("#", end="")
            for j in range(space):
                print(" ", end="")
            print("#", end="")
            for j in range(middle_space):
                print(" ", end="")
            print("#", end="")
            for j in range(space):
                print(" ", end="")
            print("#", end="")
            middle_space -= 2
            space += 1
            print("\n", end="")
        elif i == half:
            print("#", end="")
            for j in range(space):
                print(" ", end="")
            print("#", end="")
            for j in range(space):
                print(" ", end="")
            print("#", end="")
            space -= 1
            middle_space +=2
            print("\n", end="")

        elif i > half:
            print("#", end="")
            for j in range(space):
                print(" ", end="")
            print("#", end="")
            for j in range(middle_space):
                print(" ", end="")
            print("#", end="")
            for j in range(space):
                print(" ", end="")
            print("#", end="")
            space -= 1
            middle_space += 2
            print("\n", end="")


print_pattern(5)

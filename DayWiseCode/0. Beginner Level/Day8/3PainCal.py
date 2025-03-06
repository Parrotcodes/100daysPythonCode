# Paint coverage calculator

import math


# a = math.ceil(2.9)
# b = math.floor(2.9)
# c = round(2.6)

# print(f"Ceil value:  {a}")
# print(f"floor value: {b}")
# print(f"Round value: {c}")

# Task 1

def paint_calc( width, height, cover):
    number_of_cans = (width * height) / cover
    number_of_cans = math.ceil(number_of_cans)
    print(f"you'll need {number_of_cans} cans of paint.")
    

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
PiantboxLit = int(input("Coverage of paint: "))

paint_calc(height=test_h, width=test_w, cover=PiantboxLit)

# Task 2
# Develop the prev task with Price of paint box

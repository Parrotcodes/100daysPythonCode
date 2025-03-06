# Nested if else in python
# Nested if else is if else statement inside another if else statement.

# Syntax:
# if condition1:
#     if condition2:
#         statement2
#     else:
#         statement3
# else:
#     statement4

# Eg:
# Task 1: Write a program to check whether a number is even or odd.
# Task 2: Write a program to check whether a number is positive or negative.

# Nested if else
num = int(input("Enter the number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive")
else:
    print("Negative")

# split() method splits a string into a list.
# syntax: string.split(separator)
# You can specify the separator, default separator is any whitespace.
import random

# Task 3: Splitting the string
msg = "Hello, world, newyear"
print(msg)

new_msg = msg.split(',')
print(new_msg)

# choice() method returns a randomly selected element from the specified sequence.
# Syntax: random.choice(sequence)

# Task 4: Random choice
choice_msg_item = random.choice(new_msg)
print(choice_msg_item)



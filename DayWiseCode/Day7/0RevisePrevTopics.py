# Revision of previous topics

# For loop
list = [1, 2, 3, 4, 5]
for i in list:
    print(i)

# output
# 1 2 3 4 5

# While loop
i = 0
while i < 5:
    print(i)
    i += 1
# output 1 2 3 4
    
# Break Continue and Pass
for i in list:
    if i == 3:
        break
    print(i)  
# output 1 2  

for i in list:
    if i == 3:
        continue
    print(i)
# output 1 2 4 5

for i in list:
    if i == 3:
        pass
    print(i)
# output 1 2 3 4 5

def HangmanProject():
    pass


# Nested loop
for i in range(1, 4): # i = 1, 2, 3
    for j in range(1, 4): # j = 1, 2, 3
        print(i, j)

# output
# 1 1  -- first loop i = 1, second loop j = 1
# 1 2
# 1 3
# 2 1 -- first loop i = 2, second loop j = 1
# 2 2
# 2 3
# 3 1 -- first loop i = 3, second loop j = 1
# 3 2
# 3 3

# while netsted loop
i = 1
while i < 4: #i = 1
    j = 1 
    while j < 4: # j = 1
        print(i, j) # 1 1
        j += 1
    i += 1

# if else
a = 10
b = 20
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")

# List & its methods
list = [1, 2, 3, 4, 5]
print(list[0]) # 1
print(list[1]) # 2

print(list[-1]) # 5
print(list[-2]) # 4

for i in list:
    print(i)
# output 1 2 3 4 5
 

# String
string = "Hello World"
print(string[0]) # H
print(string[1]) # e

for i in string:
    print(i)
# output H e l l o   W o r l d

# split
string = "Hello World"
print(string.split(" ")) # ['Hello', 'World']

# join
list = ['Hello', 'World']
print(" ".join(list)) # Hello World

# slicing
string = "Hello World"
print(string[0:3]) # Hel

# Range
for i in range(1, 6):
    print(i)
# output 1
# 2 
# 3
# 4
# 5

list = [1, 2, 3, 4, 5]
length = len(list)

for i in range(length): # 0 1 2 3 4
    print(list[i])

#  skip 2 steps
for i in range(0, 10, 2):
    print(i)
# output 0 2 4 6 8

# Modules
import math
print(math.sqrt(25)) # 5.0

import random
print(random.randint(1, 10)) # 1 to 10
# output 5

from math import sqrt
print(sqrt(25)) # 5.0


# both are same
from random import *
print(randint(1, 10)) # 1 to 10

import random
print(random.randint(1, 10)) # 1 to 10


import random as r
print(r.randint(1, 10)) # 1 to 10

# Functions
def add(a, b):
    return a + b

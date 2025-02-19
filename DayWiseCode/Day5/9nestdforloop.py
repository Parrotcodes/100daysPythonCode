# nested loops -- loops inside another loops

# Column
print("---Columns---")
for i in range(0,5):
    print(i)


# Rows
print("---Rows---")
for i in range(0,5):
    print(i,end=' ')

# Patterns --- refer:geeksforgeeks for more tasks
# Nested Loop
print("---Pattern 1---")
print()
# * * * *
# * * * *
# * * * *
# * * * *

for i in range(1,5):
    for j in range(1,5):
        print("*",end=' ')
    print()
    

print("---Pattern 2---")
print()
# 1 1 1 1
# 2 2 2 2
# 3 3 3 3
# 4 4 4 4

# outer loop -- columns
for i in range(1,5):
    # inner loop -- rows
    for j in range(1,5):
        # main print out
        print(i,end=' ')
    # empty print to go next line
    print()

print("---Pattern 3 ---")
print()
# 1 2 3 4 
# 1 2 3 4 
# 1 2 3 4 
# 1 2 3 4 

for i in range(1,5):
    for j in range(1,5):
        print(j,end=' ')
    print()


print("---Pattern 4 ---")
print()
# *
# * *
# * * *
# * * * *

for i in range(1,5):
    for j in range(i):
        print("*",end=' ')
    print()


print("--- Pattern - 5")
print()
# printing numbers instead of "*"
for i in range(1,5):
    for j in range(i):
        print(i,end=' ')
    print()


# output:
# 1
# 2 2
# 3 3 3
# 4 4 4 4

print("--- Pattern - 6")
print()
# printing numbers instead of "*"
for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=' ')
    print()


# output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4



# Other Nested loops -- methods

# # way 1

# for i in range(0,4):
#     for j in range(0,4):
#         # synatax
#     for k in range(0,4):
#         # syntax


# # way 2

# for i in range(0,4):
#     for j in range(0,4):
#         for k in range(0,4):
#         # syntax
#     # syntax
# # syntax


# for loop
# Syntax:
# for variable in list:
#     # do something
#     print(variable)


# list of fruits
fruits = ["apple", "banana", "cherry"]
# print all the fruits in the list
for fruit in fruits:
    print(fruit)
    

# # # Methos to print all the elements in the list # # #

# length of the list -- len()
# sum of the list -- sum()
# range() function -- range(1, 10) -- 1, 2, 3, 4, 5, 6, 7, 8, 9
# max() function -- max(list)
# min() function -- min(list)
# sum() function -- sum(list)
# sorted() function -- sorted(list)
# list() function -- list(range(1, 10))
# list of fruits

print("###### Methods ####")
print("@ len()")
# len()
print(len(fruits))

# using for loop -- len() method

total_items = 0
for item in fruits:
    total_items += 1
print("@ len() without method")

print(total_items)
# sum()
nums = [1,2,3,4,5]

sum = 0
for num in nums:
    # sum = sum + num
    sum += num
print("@ sum()")
print(sum)


# total = sum(nums)
# print(total)


print("@ max()")
ages = [23,91,45,56,34,46,78]
# print(max(ages))

# without max() method
max_age =  91
for age in [23,45,56,34,91,46,78]:
    if max_age <= age:
        max_age = age
        
print(f"Maximum age from the list of ages: {max_age}")

print("@ min()")
# with min() method
# without min() method

print("@ sort()")
print(sorted(ages))
print(sorted(ages,reverse=True))

# list(range(0,4))
r = range(0,4)
#0
#1
#2
#3
l = list(r) #[0,1,2,3]
print(l)


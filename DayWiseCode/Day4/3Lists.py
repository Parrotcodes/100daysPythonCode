# Lists
# Syntax: list = [item1, item2, item3, ...]
# len(list) - length of list
import random


students = ["John", "Doe", "Jane", "Doe"]
# print(students[random.choice([0, 1, 2, 3])])
# print(students[random.randint(0, 3)])
# print(students[0]) --- returns first element
# print(students[3]) -- returns index 3 element
# print(students[-1]) --- returns last element
print(len(students)) # 4
# print(students[4]) # IndexError: list index out of range
print(students[0:4])

#          0  1  2  3  4, ..... n-1
# array = [1, 2, 3, 4, 5,.......n]
#  array2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

# print(students(0,len(students)-1)) # IndexError: list index out of range

# count()
print(students.count("Doe")) # 1

# Datastructure in Python
# Task: To-do list
# ordered collection of items (elements) -- To-do list


# list and array are different
# list can store any data type
# # Python Lists are used to store multiple items in a single variable. Lists are one of the most versatile data types in Python. A list can contain different types of data types. Lists are mutable, meaning their elements can be changed unlike string or tuple.
list_items = [1, 2, 3, "a", "b", "c", 1.1, 2.2, 3.3]

# array can store only one data type
# array = [1, 2, 3, 4, 5,.......n]
#  array2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]


# Track items from starting --- postivie index
# Track items from ending --- negative index


# Refeerence: https://www.w3schools.com/python/python_lists.asp

# Methods of List
# 1. append() - Adds an element at the end of the list
# 2. clear() - Removes all the elements from the list
# 3. copy() - Returns a copy of the list
# 4. count() - Returns the number of elements with the specified value
# 5. extend() - Add the elements of a list (or any iterable), to the end of the current list
# 6. index() - Returns the index of the first element with the specified value
# 7. insert() - Adds an element at the specified position
# 8. pop() - Removes the element at the specified position
# 9. remove() - Removes the first item with the specified value
# 10. reverse() - Reverses the order of the list
# 11. sort() - Sorts the list


# Example for each list methods in real life 
list_marks = [34,446,76,87,85]
list_marks.append(45)
print(list_marks)

# # append() --- adding a new student 
list_marks.append(45)

print(list_marks)


# clear --- add cart (clear all items)
list_marks.clear()
print(list_marks)

# copy() --- 
list_uk = ["india","rusiia"]
list_uk.append("japan")
list_uk.append("pakistan")

usa = list_uk.copy()

print(list_uk)
print(usa)


# count -- add items into cart (increasing the quantity)

# extend() --- adding new data + to the old data
old_data = [45,56,768,565]

new_data = ["a","b","c"]

old_data.extend(new_data)


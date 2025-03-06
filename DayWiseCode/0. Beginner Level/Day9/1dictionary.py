# list  = []  -- completed
#  pop ==> list.pop(5)  -- completed
# tuple = ()
# set   = {}
# dict  = {key:value} --- running

# Dictionary
# key:value
# key should be unique
# duplicate value is allowed

# dict = {key:value}

# Example

Definations ={
    "Bug":"An error in a program that prevents the program from running as expected.",
    "Function":"A named section of a program that performs a specific task.",
    "Loop":"The action of doing something over and over again.",
    "Dictionary":"A collection of key-value pairs."
}

print(Definations)
print(Definations["Dictionary"])

for key in Definations:
   # print(key)
    if key == "Function":
       print("Printing only Key : " + key)


Student = {
    "name":"John",
    "age":25,
    "course":"Python"
}

# list --- student[0]
# dict --- student["name"]

# get the value
print(Student["name"])
print(Student.get("name"))


# updating the value
Student["age"] = 32
print(Student)


print("Student Details of Student2")

# Nesting of List inside Dictionary
Student2 = {
    "name":"John",
    "age":25,
    "course":["Python"]
}
# updating courses to multiple
Student2["course"].append("Java")
Student2["course"].extend(["C","C++"])
print(Student2["course"])

# empty dictionary
Student2= {}
print(Student2)

Student2["name"] = "John"
print(Student2)

# C R U D -- Operations
# Create    --- Student2["name"] = "John"
# Read      --- Student2["name"]
# Update    --- Student2["name"] = "Hary"
# Delete    --- del Student2["name"] or Student2.pop("name") or Student2.clear() or Student2 = {}  #output : {}


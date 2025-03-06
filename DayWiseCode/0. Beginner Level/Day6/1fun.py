### Functions in Python ###

# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

# Syntax:
def sayHello():
  print("Hello from a function")
  
# Calling function
sayHello()


def getMilk():
  print("go straight")
  print("Move left")
  print("Buy milk")
  print("Move Right")
  print("go straight")
  print("Kept milk on the table")

getMilk()
print("-----------------------> Calling 2")
getMilk()
print("-----------------------> Calling 3")
getMilk()


print(len("Hello"))



# Functional parameter/arguments
def Person(name):
  print("Hello" + name)

# call by value & call by reference
Person(" Rakesh")


def Value(x):
  print(x)

# Call by reference
Value(5)
# Ref()
# recurssion

# def Bye():
#   print("Good Bye")
#   Bye()

# Bye()


import sys

# sys.setrecursionlimit(2000)
print(sys.getrecursionlimit)
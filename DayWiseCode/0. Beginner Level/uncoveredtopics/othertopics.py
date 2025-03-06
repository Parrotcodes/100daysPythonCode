# @@@@@@@@@@@@@@@@@@@@@@@@@@ Variable Naming Rules @@@@@@@@@@@@@@@@@@@@@@
# Rules for Python variables:
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.

# valid
new = 10
_new2 = 32

# not valid
# 1name = "hari"

# case-sensitive
name = "Honey"
Name = "Jhon"
NAME = "max"

print(name)
print(Name)
print(NAME)

a = 10
a = 20
print(a)

# var can include numbers, character 
namer456 = 89
g3reet23me = "helo"

# symobls are not allowed in varible naming declarations
# name& = 454
# $jdkf = 8898



# @@@@@@@@@@@@@@@@@@@@@@@@@@ Operators @@@@@@@@@@@@@@@@@@@@@@

# operators
    #  Membership Operator
    #  Identity Operator
    
# Membership Operators in Python
# The `in` Operator ==> True/False
# The `not in` Operator ==> True/False

# Eg: Membership operators in Python, such as “in” and “not in,” check if a value exists in a sequence like a list, tuple, or string.

# 'in' operator
fruits = ['apple', 'banana', 'cherry']
if 'banana' in fruits:
    print('Yes, banana is in the list')

# 'not in' operator
if 'banana' not in fruits: # (opposite meaing) True -> False // False -> True
    print('Yes, banana is in the list')
else:
    print("banaa is not there in your list")


# Identity Operator in Python
#  `is` operator
#  'is not' operator

# Eg: Identity operators “is” and “is not,” are used to compare the memory locations of two objects.

x = 5 # x = y => 5
y = 5
if x is y: # is ==> ==
    print('x and y are pointing to the same object')
    
a = 45
b = 56
if a is not b: # Condition: is --> False  //  is not ---> True (opposite meaing)
    print("both a and b variables are pointing to the same memory location or objects")
    
    
    

# @@@@@@@@@@@@@@@@@@@@@@@@@@ Under function ---> Scope and Local/Global Variables @@@@@@@@@@@@@@@@@@@@@@

# Scope and Local/Global Variables

# Block / Scope:  A variable is only available from inside the region it is created. This is called scope.

# if (a>b) {
#     a = 50
#     print(a)
# }

# function heelo(){
#     msg = "welcome"
#     print(msg)
# }

# msg = "hi how are you"
def Hello():
    msg = "welcome"
    msg2 = "new message"
    print(msg)
    print(msg2)

Hello()
# print(msg) # msg varibale not --> Error


# Local Variables:
# Scope: Accessible only within the function or block where they are defined.
# Declaration: Defined inside a function or block.
# Lifetime: Exists only during the function’s execution.

def num():
    i = 0 # memory ( i = 0 ) it's life ends once excution done
    print(i)

# print(i) --> Error
num() # it will work but after function excution, varibles values will earase from memory

# Global Variables:
# Scope: Accessible throughout the entire program or script, including all functions.
# Declaration: Defined outside any function or class.
# Lifetime: Exists for the duration of the program’s/ project execution.

PI = 3.14
SpeedOfLight = 2.99 * 10

name = "Rakesh" #global variables

def greet():
    msg = "welcome Mr."
    msg += name
    print(msg)
    
# print(msg)
greet()


name = "Raj"
greet()

# Real life Eg: profile / mobile apps 

# Eg:
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

# Eg:
x = "fantastic" # global
def myfunc2():
    y = "superb"  # local
    print("python is " + x + y)

myfunc2()

y = "new varibale"
print(y)


# Eg:
x = "fantastic" # global
def myfunc2():
    global z  # converting local to gloabl varibale using `global` keyword
    z = "superb"  # local
    print("python is " + x + y)

myfunc2()

print(z)
#####@@@@@@ Arbitrary Arguments are often shortened to *args in Python documentations.

# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

# Eg:
# Arbitrary Arguments are often shortened to *args in Python documentations.

def my_function(*kids):    
  print("The youngest child is " + kids[1])

# list -- []
# tupes -- ()
# sets -- {}
my_function("Emil","Rakesh","SreeRaj","Hary")


#@@@@@ Keyword Arguments
# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
def my_function(**kid):
  print("His last name is " + kid['lname'])

my_function(fname = "Tobias", lname = "Refsnes")
# my_function("Emil","Rakesh","SreeRaj","Hary")


# Return Values
# To let a function return a value, use the return statement:

# Example
# a = 4
# b = 6
# sum = a+b
# print(sum)

def add(a,b):
    return (a + b)

print(add(5,6))

print(add(50,40))

# method 2
# def Add(*a):
#     return ( a[0] +a[1])

# Add(50,50,67,79,43)

# Method 3

def Add(**a):
    return a['tel'] + a['hin'] + a['eng']

total = Add(tel=50,hin=50,eng=67)
print(f"your total score: {total}")

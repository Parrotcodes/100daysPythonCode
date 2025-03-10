#### Arguments ###

# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
# The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:


# Eg:
def my_function(fname):
  print("Hello, "+ fname)

my_function("Emil")
my_function("Tobias")
my_function("Linus")

# Parameters or Arguments?
# The terms parameter and argument can be used for the same thing: information that are passed into a function.

#@@@@ From a function's perspective:

# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.

#@@@ Number of Arguments
# By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.

# Eg:
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")


print()
print()
print()
print()

def Person2(name, age, addr, email):
  print("Name: " + name)
  print("Email: "+ email)
  print("Age: " + age)
  print("Addr: " + addr)

Person2("Rakesh","23","Hyderabad","abced@gmail.com")


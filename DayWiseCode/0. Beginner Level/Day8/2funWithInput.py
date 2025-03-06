# Write a program to take input from user and print the sum of all the numbers entered by user.
# stdent_data =[
#     {"name": "Rakesh", "id": 25,"marks": 90},
#     {"name": "Rahul", "id": 26,"marks": 80},
#     ]

# newMarks = []
# for marks in stdent_data["marks"]:
#     if marks < 50:
#         newMarks += 15     
#     else:
#         updatelist = marks["marks"] 
        
#     total_marks = updatelist["marks"] + newMarks["marks"]
    
# print(total_marks)


# with input function
def greeting(name):
    print(f"Hello {name}")

greeting("Rakesh")
greeting("Rahul")
greeting("Raj")

# # with input function
# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# sum = a + b
# print(f"Before function ={sum}")

def sumOfNumbers(a,b):
    sum = a + b
    print(f"Sum of {a} + {b} = {sum}")

sumOfNumbers(10,20)
sumOfNumbers(30,40)
sumOfNumbers(50,60)

# return functions 
def Add(a,b):
    return a + b

Add(90,90)
Add(100,100)  


# arrow function () => {}

# def add(a,b) => {a + b}


# Positional Argument
def Person(name, age):
    print(f"Name = {name} and Age = {age}")

# Person("Rakesh", 25)
# Person("Rahul", 26)
# Person("Raj", 27)

# follows the position of the argument
Person(23,"Rakesh")
Person(26,"Rahul")
Person(27,"Raj")

# Keyword Argument
def Person(name, age):
    print(f"Name = {name} and Age = {age}")

Person(age=25, name="Rakesh")
Person(age=26, name="Rahul")
Person(age=27, name="Raj")

# Default Argument
def Person(name, age=18):
    print(f"Name = {name} and Age = {age}")

Person("Rakesh")

def Person2(name="newUser", age=18):
    print(f"Name = {name} and Age = {age}")
    
Person2()

# Variable Length Argument
def sum(*args):
    sum = 0
    for i in args:
        sum += i
    print(f"Sum = {sum}")



# real life example like cards/componets eg:aribng, facebooks posts, youtube videos
def Card(img,favbtn,title,distance,date,price,rating):
    print(f"Image = {img}")
    print(f"Title = {title}")
    print(f"Distance = {distance}")
    print(f"Date = {date}")
    print(f"Price = {price}")
    print(f"Rating = {rating}")
    print(f"FavBtn = {favbtn}")


# card 1
Card("img/img1.jpg", "fav", "Ellijay", "2km", "12-12-2021", 3000, 4.9)
# card 2
Card("img/img2.jpg", "fav", "CherryLog", "2km", "12-12-2021", 2000, 4.5)

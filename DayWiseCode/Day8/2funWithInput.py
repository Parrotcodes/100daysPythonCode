# Write a program to take input from user and print the sum of all the numbers entered by user.
stdent_data =[
    {"name": "Rakesh", "id": 25,"marks": 90},
    {"name": "Rahul", "id": 26,"marks": 80},
    ]

newMarks = []
for marks in stdent_data["marks"]:
    if marks < 50:
        newMarks += 15
        
    else:
        updatelist = marks["marks"] 
        
    total_marks = updatelist["marks"] + newMarks["marks"]
    
print(total_marks)


# with input function
def greeting():
    print("Hello Rakesh")

greeting()
